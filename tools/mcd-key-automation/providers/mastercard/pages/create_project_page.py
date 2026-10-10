"""Create-project form page object."""
from __future__ import annotations

import asyncio
import base64
import json
import os
import time
from pathlib import Path
from typing import Sequence

from loguru import logger
from playwright.async_api import Page

from browser.downloads import save_download
from browser.screenshots import capture as screenshot
from providers.mastercard.selectors import CreateProjectSelectors, ProjectCreatedSelectors


class CreateProjectPage:
    """Handles the multi-step create-project wizard."""

    def __init__(self, page: Page) -> None:
        self.page = page

    async def wait_for_form(self) -> None:
        await self.page.wait_for_selector(CreateProjectSelectors.name_input, timeout=20000)

    async def fill(self, *, project_name: str, on_behalf_of_company: bool = False,
                   region: str | None = None, api_selection: str | Sequence[str] | None = None) -> None:
        logger.info(
            "Filling create-project form: name={!r} on_behalf={} region={!r} api_selection={!r}",
            project_name, on_behalf_of_company, region, api_selection,
        )

        # Use triple_click + press_sequentially to fire React synthetic key events.
        # page.fill() sets the DOM value directly without key events, so React's onChange
        # never fires and the Proceed button stays aria-disabled="true".
        name_loc = self.page.locator(CreateProjectSelectors.name_input)
        await name_loc.click(click_count=3)  # select any existing text
        await name_loc.press_sequentially(project_name, delay=50)

        # On behalf of a company? Default No.
        label_text = "Yes" if on_behalf_of_company else "No"
        await self.page.locator(f"label:has-text('{label_text}')").first.click()

        # If company selected, the react-select becomes visible and needs a value.
        if on_behalf_of_company:
            raise NotImplementedError("Company selection not yet implemented")

        # Sub-API selection (e.g. "Priceless Specials" or ABU Push service cards).
        if api_selection:
            options = [api_selection] if isinstance(api_selection, str) else list(api_selection)
            logger.info("Selecting sub-API option(s): {!r}", options)

            selected = False
            for option in options:
                sel = (
                    f"label:has-text('{option}'), "
                    f"[role='checkbox']:has-text('{option}'), "
                    f"li:has-text('{option}'), "
                    f"div[class*='card']:has-text('{option}'), "
                    f"span:has-text('{option}')"
                )
                loc = self.page.locator(sel).first
                if await loc.count() > 0:
                    await loc.click()
                    logger.info("Clicked sub-API: {!r}", option)
                    selected = True
                    break

            if not selected:
                logger.warning("None of the sub-API options were found on page: {!r}", options)

        # Region dropdown (only present for some APIs e.g. Open Finance)
        if region:
            region_loc = self.page.locator(CreateProjectSelectors.region_select_input)
            if await region_loc.count() > 0:
                logger.info("Selecting region: {!r}", region)
                await region_loc.click()
                await self.page.locator(f"li:has-text('{region}'), [role='option']:has-text('{region}')").first.click()

    async def proceed(self) -> None:
        """Wait for the Proceed button to be enabled by React, then click it."""
        btn = self.page.locator(CreateProjectSelectors.proceed_button)

        # Wait up to 15s for React validation to enable the button.
        for i in range(30):
            aria_disabled = await btn.get_attribute("aria-disabled", timeout=2000)
            if aria_disabled != "true":
                logger.info("Proceed button enabled after {}s", i * 0.5)
                break
            await asyncio.sleep(0.5)
        else:
            logger.warning("Proceed button still aria-disabled after 15s — clicking anyway")

        logger.info("Clicking Proceed (url={})", self.page.url)
        # force=True bypasses Playwright's actionability checks (visibility/stability),
        # which avoids timeouts caused by React re-rendering the button mid-click.
        await btn.click(force=True)
        logger.info("Proceed clicked — url now: {}", self.page.url)

    async def wait_for_confirmation_or_project_page(self, timeout_ms: int = 45000) -> str:
        """
        Wait for the project creation to complete.

        Returns one of:
          'project_page'       — navigated directly to /project-details/<uuid>
          'step2_credentials'  — wizard advanced to Step 2 (key alias + password form)
          'download'           — confirmation page with 'Download key file' button (OAuth 1.0a)
          'open_project'       — confirmation page with 'Open project' button only (OAuth 2.0)

        Automatically handles intermediate wizard steps:
          - "Service details" (Open Finance Step 2): optional description page — auto-clicks Proceed.
        """
        deadline = timeout_ms / 1000
        poll_interval = 0.5
        elapsed = 0.0
        _service_details_clicked = False

        while elapsed < deadline:
            url = self.page.url
            if "/project-details/" in url and "/create-project" not in url:
                logger.info("Landed on project detail page — {}", url)
                return "project_page"
            if await self.page.locator(ProjectCreatedSelectors.download_key_button).count() > 0:
                logger.info("Confirmation page (OAuth 1.0a, download button present) — {}", url)
                return "download"
            if await self.page.locator(ProjectCreatedSelectors.open_project_button).count() > 0:
                logger.info("Confirmation page (OAuth 2.0, open-project button only) — {}", url)
                return "open_project"
            # Step 2: wizard advanced to Project credentials (key alias + password).
            # Use :visible to avoid firing when the input is pre-rendered (hidden) behind an
            # intermediate service-details form (e.g. Carbon Calculator Step 2).
            if await self.page.locator("[data-testid='key-alias-input']:visible").count() > 0:
                logger.info("Wizard advanced to Step 2 (Project credentials) — {}", url)
                return "step2_credentials"

            # Open Finance / Carbon Calculator "Service details" intermediate step.
            # Auto-fills required fields (e.g. CID for Carbon Calculator) then clicks Proceed.
            if not _service_details_clicked:
                service_heading = await self.page.locator(
                    "h1:has-text('Service details'), h2:has-text('Service details'), "
                    "[class*='heading']:has-text('Service details'), "
                    "div:has-text('Open Finance Sandbox API Credentials')"
                ).count()
                if service_heading > 0:
                    logger.info("Service details step detected — filling required fields then clicking Proceed")
                    await screenshot(self.page, "ofin_service_details")
                    # Scroll to bottom to expose the button on this step.
                    await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    await asyncio.sleep(0.5)
                    # Fill the mandatory Service-details fields (customer segment,
                    # intended-use checkboxes, description, numeric CID).
                    await self._fill_service_details_fields()
                    logger.info("Service details — filled segment/intended-use/description fields")
                    # Service details is its OWN wizard step — click Proceed to
                    # advance to the credentials (key alias + password) step. The
                    # button enables once the required fields above are satisfied.
                    await self._click_service_details_proceed()
                    _service_details_clicked = True
                    await asyncio.sleep(1.5)
                    continue

            await asyncio.sleep(poll_interval)
            elapsed += poll_interval
        raise TimeoutError(f"No confirmation or project page appeared within {timeout_ms}ms — skipping")

    async def _fill_dynamic_config_fields(self) -> bool:
        """Fill schema-driven config fields (the "Service details" step) with real interactions.

        Services with a config schema (e.g. BIN Lookup / 1800, Carbon Calculator
        / 283) render REQUIRED fields whose ``name`` is ``<schemaId>_<field>``
        (schemaId is a UUID). These must be committed to React state via genuine
        interactions — synthetic native-setter events do not commit, so the create
        POST ships an empty ``config`` and the backend rejects it ("Config is
        required for service ID <id>").

        Only acts when such a field is VISIBLE (i.e. the active config step); on
        later steps the same form exists hidden and re-touching it clears the
        already-committed config. Returns True if a config step was detected+filled.
        """
        page = self.page
        # Detect a VISIBLE schema-driven config field (name = "<uuid>_<field>").
        has_cfg = await page.evaluate(r"""
            () => Array.from(document.querySelectorAll('input,select,textarea'))
                .some(e => e.offsetParent !== null &&
                    /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}_/
                        .test(e.name || ''));
        """)
        if not has_cfg:
            return False

        logger.info("Dynamic-config (schema-driven) step detected — filling required fields")

        # 1) Customer segment react-select (BIN Lookup) — pick a valid enum option.
        seg = page.locator("[data-testid='customersegment-select']")
        if await seg.count() > 0 and await seg.first.is_visible():
            try:
                await seg.first.scroll_into_view_if_needed(timeout=3000)
                await seg.first.click()
                await asyncio.sleep(0.4)
                for label in ("Merchant", "Acquirer", "Issuer", "Other"):
                    opt = page.locator(
                        f"[role='option']:has-text('{label}'), "
                        f"[class*='option']:has-text('{label}')"
                    ).first
                    if await opt.count() > 0:
                        await opt.click(timeout=3000)
                        logger.info("Customer segment → {!r}", label)
                        break
            except Exception as exc:
                logger.debug("customer-segment select failed: {}", exc)

        # 2) Numeric text inputs (e.g. Carbon's customerId, placeholder
        #    "Enter Numeric value") — fill with a real value.
        try:
            nums = page.locator(
                "input[placeholder*='umeric'], "
                "[data-testid='customerid-text'], "
                "[data-testid*='customerid']"
            )
            for i in range(await nums.count()):
                el = nums.nth(i)
                if await el.is_visible() and not (await el.input_value()):
                    await el.fill("1")
                    logger.info("Numeric config input → '1'")
        except Exception as exc:
            logger.debug("numeric config input fill failed: {}", exc)

        # 3) Intended-use checkboxes (BIN Lookup) — tick the first via its label.
        try:
            boxes = page.locator("input[type=checkbox][data-testid*='intendedUse']")
            count = await boxes.count()
            already = False
            for i in range(count):
                if await boxes.nth(i).is_checked():
                    already = True
                    break
            if count > 0 and not already:
                first = boxes.first
                testid = await first.get_attribute("data-testid")
                label = page.locator(f"label[for='{testid}']")
                if await label.count() > 0:
                    await label.first.click()
                else:
                    await first.check(force=True)
                logger.info("Intended-use → checked first option")
        except Exception as exc:
            logger.debug("intended-use check failed: {}", exc)

        # 4) Use-case / outline textarea (BIN Lookup) — fill with a real value.
        #    (Only this specific textarea; other optional free-text config fields
        #    like Carbon's BINs must stay empty or they fail format validation.)
        try:
            ta = page.locator(
                "[data-testid='usecase-textarea'], textarea[name$='useCase']"
            ).first
            if await ta.count() > 0 and not (await ta.input_value()):
                await ta.click()
                await ta.fill(
                    "Sandbox integration testing and evaluation of this API for a "
                    "proof of concept."
                )
                logger.info("Use-case outline → filled")
        except Exception as exc:
            logger.debug("use-case textarea fill failed: {}", exc)

        # 5) Any remaining VISIBLE empty react-select (e.g. Carbon's Score
        #    Retention Period) — open and pick the first real option.
        try:
            rs_ids: list[str] = await page.evaluate("""
                () => Array.from(document.querySelectorAll('input[id^="react-select"]'))
                    .filter(el => el.offsetParent !== null && !el.value)
                    .filter(el => {
                        const c = el.closest("[class*='control']");
                        const t = (c && c.textContent || '').trim();
                        return !t || /^select/i.test(t);
                    })
                    .map(el => el.id)
            """)
        except Exception:
            rs_ids = []
        for rid in rs_ids:
            try:
                inp = page.locator(f"#{rid}").first
                await inp.evaluate("el => el.scrollIntoView({block: 'center', inline: 'center'})")
                await asyncio.sleep(0.2)
                control = page.locator(f"#{rid}").locator(
                    "xpath=ancestor::*[contains(@class,'control')][1]"
                )
                target = control.first if await control.count() > 0 else inp
                await target.click(force=True, timeout=3000)
                await asyncio.sleep(0.4)
                opt_texts: list[str] = await page.evaluate("""
                    () => Array.from(document.querySelectorAll(
                        "[role='option'], [class*='option']"
                    )).map(e => (e.textContent || '').trim()).filter(Boolean)
                """)
                if opt_texts:
                    pick = opt_texts[0]
                    await page.locator(
                        f"[role='option']:has-text({pick!r}), "
                        f"[class*='option']:has-text({pick!r})"
                    ).first.click(timeout=3000)
                    logger.info("react-select {} → {!r}", rid, pick)
                else:
                    await inp.press("ArrowDown")
                    await inp.press("Enter")
            except Exception as exc:
                logger.debug("react-select {} fill failed: {}", rid, exc)

        await asyncio.sleep(0.4)
        await screenshot(self.page, "service_details_after_fill")
        return True

    async def _fill_service_details_fields(self) -> None:
        """Fill the mandatory 'Service details' fields on the create-project wizard.

        Mastercard added a required Service-details section to the wizard:
          * a 'customer segment' react-select dropdown
          * one or more 'intended use of the data' checkboxes
          * a free-text description / outline textarea
          * (some APIs) a numeric Customer ID (CID) input
        Until these are satisfied the 'Create project' button stays disabled.

        Idempotent: only fills empty/unchecked controls, so it is safe to call
        from both the service-details detection branch and fill_step2_credentials.
        """
        page = self.page
        try:
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        except Exception:
            pass
        await asyncio.sleep(0.3)

        # Dynamic-config services (e.g. BIN Lookup, service 1800) render a
        # schema-driven "Additional information" form whose values must reach the
        # React/Formik state via REAL user interactions — synthetic native-setter
        # events do not commit, so the create POST ships an empty `config` and the
        # backend rejects it ("Config is required for service ID <id>"). Fill those
        # known fields with genuine Playwright actions. If this handled the config
        # step, skip the generic native-setter fill below (it would put junk into
        # optional free-text config fields, e.g. Carbon's BINs, and fail validation).
        if await self._fill_dynamic_config_fields():
            return

        # Checkboxes (intended use), textareas (description) and numeric inputs (CID).
        try:
            await page.evaluate(r"""
                () => {
                    const setNative = (el, val) => {
                        const proto = el.tagName === 'TEXTAREA'
                            ? window.HTMLTextAreaElement.prototype
                            : window.HTMLInputElement.prototype;
                        const setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
                        setter.call(el, val);
                        el.dispatchEvent(new Event('input', { bubbles: true }));
                        el.dispatchEvent(new Event('change', { bubbles: true }));
                        el.dispatchEvent(new Event('blur', { bubbles: true }));
                    };
                    // Intended-use checkboxes: tick the first if none are checked.
                    const checks = Array.from(document.querySelectorAll(
                        'input[type=checkbox][data-testid*="intendedUse"], '
                        + 'input[type=checkbox][name*="intendedUse"], '
                        + 'input[type=checkbox][id*="intendedUse"]'
                    ));
                    if (checks.length && !checks.some(c => c.checked)) {
                        checks[0].click();
                    }
                    // Description / outline textareas.
                    const areas = Array.from(document.querySelectorAll('textarea'))
                        .filter(t => t.offsetParent !== null && !t.value);
                    for (const t of areas) {
                        setNative(t, 'Sandbox integration testing and evaluation of this API for a proof of concept.');
                    }
                    // Numeric text inputs (e.g. Customer ID / CID).
                    const nums = Array.from(document.querySelectorAll(
                        'input:not([type=hidden]):not([type=checkbox]):not([type=radio])'
                    )).filter(i => i.offsetParent !== null && !i.value &&
                        (((i.placeholder||'').toLowerCase().includes('numeric')) ||
                         ((i.id||'').toLowerCase().includes('cid')) ||
                         ((i.name||'').toLowerCase().includes('cid'))));
                    for (const n of nums) setNative(n, '1');
                }
            """)
        except Exception as exc:
            logger.debug("service-details checkbox/textarea fill skipped: {}", exc)
        await asyncio.sleep(0.4)

        # Customer-segment (and any other empty) react-select dropdowns: pick the
        # first available option.
        try:
            rs_ids: list[str] = await page.evaluate("""
                () => Array.from(document.querySelectorAll('input[id^="react-select"]'))
                    .filter(el => el.offsetParent !== null && !el.value)
                    .filter(el => {
                        // Skip a react-select whose control already shows a chosen
                        // value (avoids clobbering a selection made by the
                        // dynamic-config filler above).
                        const ctrl = el.closest("[class*='control']");
                        const txt = (ctrl && ctrl.textContent || '').trim();
                        return !txt || /^select/i.test(txt);
                    })
                    .map(el => el.id)
            """)
        except Exception:
            rs_ids = []
        for rid in rs_ids:
            try:
                inp = page.locator(f"#{rid}").first
                # Center the element in the viewport via JS first — force=True clicks
                # still fail if the target sits outside the viewport, and these
                # react-select inputs often render below the fold.
                await inp.evaluate("el => el.scrollIntoView({block: 'center', inline: 'center'})")
                await asyncio.sleep(0.2)
                # Prefer clicking the react-select 'control' container (the visible
                # box) over the hidden dummy input.
                control = page.locator(f"#{rid}").locator(
                    "xpath=ancestor::*[contains(@class,'control')][1]"
                )
                target = control.first if await control.count() > 0 else inp
                await target.click(force=True, timeout=3000)
                await asyncio.sleep(0.5)
                # Read the option labels, then click the first REAL option by its
                # text (mirrors the proven fill_ofin approach — clicking .first can
                # grab a hidden/placeholder node, which submits an invalid value).
                opt_texts: list[str] = await page.evaluate("""
                    () => Array.from(document.querySelectorAll(
                        "[role='option'], [class*='option']"
                    )).map(e => (e.textContent || '').trim()).filter(Boolean)
                """)
                if opt_texts:
                    pick = opt_texts[0]
                    picker = page.locator(
                        f"[role='option']:has-text({pick!r}), "
                        f"[class*='option']:has-text({pick!r})"
                    ).first
                    await picker.click(timeout=3000)
                    logger.debug("react-select {} → selected {!r}", rid, pick)
                    await asyncio.sleep(0.3)
                else:
                    # Fallback: keyboard-select the first option.
                    await inp.press("ArrowDown")
                    await inp.press("Enter")
            except Exception as exc:
                logger.debug("react-select {} fill skipped: {}", rid, exc)
        await asyncio.sleep(0.4)
        await screenshot(self.page, "service_details_after_fill")

    async def _click_service_details_proceed(self) -> bool:
        """Submit the Service-details wizard step (button 'Proceed' or 'Create project').

        The button (a ``type=submit`` #submit / data-testid='proceed-btn') is
        sometimes reported "not visible" by Playwright due to a sticky footer,
        so we drive it with a direct JS click after confirming it is enabled.

        Open Finance generates a certificate when this step is submitted and the
        portal intermittently pops "An error has occurred — There was an issue
        trying to create the certificate". We detect that dialog, dismiss it, and
        re-click the button (up to 3 times) before giving up.
        Returns True once the step is submitted (or advanced).
        """
        page = self.page
        error_dialog = (
            "text=/issue trying to create the certificate/i, "
            "[role='dialog']:has-text('An error has occurred'), "
            "text=/An error has occurred/i"
        )
        close_btn = (
            "[role='dialog'] button:has-text('Close'), "
            "[role='dialog'] button:has-text('OK'), "
            "[role='dialog'] button:has-text('Dismiss'), "
            "button[aria-label='Close']"
        )

        async def _click_once() -> bool:
            # Wait until the submit button is present and enabled.
            for _ in range(30):
                state = await page.evaluate("""
                    () => {
                        const b = document.querySelector('[data-testid="proceed-btn"], button#submit');
                        if (!b) return null;
                        return { disabled: !!b.disabled, aria: b.getAttribute('aria-disabled') };
                    }
                """)
                if state and not state["disabled"] and state["aria"] != "true":
                    break
                await asyncio.sleep(0.5)
            # IMPORTANT: use a REAL (trusted) Playwright click, not an injected
            # JS ``element.click()``. The portal generates the certificate in the
            # browser on submit, and that path requires transient user activation
            # (a genuine user gesture). A synthetic JS click has no user
            # activation, so the cert step aborts with "There was an issue trying
            # to create the certificate". A real mouse click succeeds — this is
            # the same thing that works when a human clicks the button.
            # Deliver a REAL trusted click via mouse coordinates on the VISIBLE,
            # enabled submit button. There are several 'proceed-btn' elements in
            # the DOM (one per wizard step); Playwright's .first can resolve to a
            # hidden/disabled one and time out. Locating the visible enabled
            # button in JS, scrolling it to centre, then page.mouse.click at its
            # coordinates gives a genuine user gesture that properly SUBMITS the
            # step so its form values (e.g. the dynamic config) commit.
            box = await page.evaluate("""
                () => {
                    const btns = Array.from(document.querySelectorAll(
                        '[data-testid="proceed-btn"], button#submit, button[type="submit"]'));
                    const b = btns.find(x => x.offsetParent !== null
                        && x.getAttribute('aria-disabled') !== 'true' && !x.disabled);
                    if (!b) return null;
                    b.scrollIntoView({ block: 'center', inline: 'center' });
                    const r = b.getBoundingClientRect();
                    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
                }
            """)
            if box:
                try:
                    await asyncio.sleep(0.3)  # let scroll settle
                    await page.mouse.click(box["x"], box["y"])
                    return True
                except Exception as exc:
                    logger.debug("Service-details mouse click failed: {}", exc)
            logger.warning(
                "Service-details submit: no real click landed; using JS fallback "
                "(may not commit dynamic config)"
            )
            # Last-resort fallback only (loses user activation, may hit the cert
            # error) so the wizard doesn't stall entirely if the button can't be
            # clicked normally.
            try:
                clicked = await page.evaluate("""
                    () => {
                        const b = document.querySelector('[data-testid="proceed-btn"], button#submit');
                        if (!b) return false;
                        b.scrollIntoView({ block: 'center', inline: 'center' });
                        b.click();
                        return true;
                    }
                """)
                return bool(clicked)
            except Exception:
                return False


        for attempt in range(1, 4):
            if not await _click_once():
                logger.warning("Could not click Service-details submit button (attempt {})", attempt)
                await asyncio.sleep(1.0)
                continue
            logger.info("Clicked Service-details submit ('Proceed'/'Create project') attempt {}", attempt)

            # Watch for either the step advancing or the certificate error dialog.
            waited = 0.0
            while waited < 25.0:
                url = page.url
                if "/project-details/" in url and "/create-project" not in url:
                    return True
                if await page.locator(ProjectCreatedSelectors.download_key_button).count() > 0:
                    return True
                if await page.locator("[data-testid='key-alias-input']:visible").count() > 0:
                    return True  # advanced to the credentials step (oauth1)
                if await page.locator(
                    "h1:has-text('Creating your project'), h2:has-text('Creating your project')"
                ).count() > 0:
                    return True
                if await page.locator(error_dialog).count() > 0:
                    await screenshot(self.page, f"ofin_cert_error_attempt{attempt}")
                    logger.warning(
                        "Certificate error dialog after submit (attempt {}/3) — "
                        "dismissing and re-clicking 'Create project'", attempt,
                    )
                    try:
                        cb = page.locator(close_btn).first
                        if await cb.count() > 0:
                            await cb.click(force=True)
                    except Exception:
                        pass
                    await asyncio.sleep(2.0)
                    break  # re-click on next outer-loop iteration
                await asyncio.sleep(1.0)
                waited += 1.0
            else:
                # No error and no explicit advance signal within 25s — assume the
                # click took; let the caller's wait loop resolve the final state.
                return True

        logger.warning(
            "Service-details submit kept hitting the certificate error after 3 attempts "
            "(usually transient / VPN-related)"
        )
        return False

    async def fill_step2_credentials(self, *, alias: str, password: str) -> None:
        """Fill ALL alias+password pairs in the Step 2 wizard.

        Some APIs (e.g. clarity, txnotify) have two key sections: a signing key
        AND an encryption key, each with their own alias + password fields.
        The encryption section may be collapsed; we use JS to set values and fire
        React synthetic events without needing visibility.
        """
        logger.info("Filling Step 2 credentials: alias={!r}", alias)

        # The credentials page now also carries the mandatory Service-details
        # fields (customer segment, intended use, description). Fill them here too
        # so 'Create project' enables even when we reached this page directly.
        await self._fill_service_details_fields()

        # Helper: fill a React-controlled input by testid using JS (works even if hidden).
        async def fill_react_input(testid: str, value: str) -> bool:
            return await self.page.evaluate("""
                ([testid, value]) => {
                    const el = document.querySelector(`[data-testid="${testid}"]`);
                    if (!el) return false;
                    const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                        window.HTMLInputElement.prototype, 'value').set;
                    nativeInputValueSetter.call(el, value);
                    el.dispatchEvent(new Event('input', { bubbles: true }));
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                    el.dispatchEvent(new Event('blur', { bubbles: true }));
                    return true;
                }
            """, [testid, value])

        # Discover all alias inputs on the page (visible or not).
        alias_testids: list[str] = await self.page.evaluate("""
            () => Array.from(document.querySelectorAll('input[data-testid]'))
                .filter(el => el.dataset.testid.includes('alias'))
                .map(el => el.dataset.testid)
        """)
        logger.debug("Step 2 alias inputs detected: {}", alias_testids)

        for idx, testid in enumerate(alias_testids):
            suffix = f"-enc{idx}" if idx > 0 else ""
            fill_alias = f"{alias}{suffix}"
            # Try JS fill first (works for hidden elements too).
            ok = await fill_react_input(testid, fill_alias)
            if not ok:
                logger.warning("Alias input not found via JS: {}", testid)
            else:
                logger.debug("Filled alias[{}] testid={!r} value={!r}", idx, testid, fill_alias)

        # Discover all password inputs (excluding confirm-password).
        pw_testids: list[str] = await self.page.evaluate("""
            () => Array.from(document.querySelectorAll('input[type="password"][data-testid]'))
                .filter(el => !el.dataset.testid.includes('confirm'))
                .map(el => el.dataset.testid)
        """)
        logger.debug("Step 2 password inputs detected: {}", pw_testids)

        for testid in pw_testids:
            ok = await fill_react_input(testid, password)
            if not ok:
                logger.warning("Password input not found via JS: {}", testid)
            else:
                logger.debug("Filled password testid={!r}", testid)

        # Fill confirm-password if present.
        confirm_testids: list[str] = await self.page.evaluate("""
            () => Array.from(document.querySelectorAll('input[type="password"][data-testid]'))
                .filter(el => el.dataset.testid.includes('confirm'))
                .map(el => el.dataset.testid)
        """)
        for testid in confirm_testids:
            await fill_react_input(testid, password)
            logger.debug("Filled confirm-password testid={!r}", testid)

        # Log all input states to help diagnose remaining issues.
        inputs_info = await self.page.evaluate("""
            () => Array.from(document.querySelectorAll('input[data-testid]'))
                .map(el => ({ testid: el.dataset.testid, value: el.value ? '***' : '', type: el.type }))
        """)
        logger.debug("Step 2 inputs after fill: {}", inputs_info)

        # Extra pause to let React settle all validation state.
        await asyncio.sleep(1.5)

    async def _js_click_create_project(self) -> bool:
        """JS-click the 'Create project' button (bypasses CSS visibility). Returns True if found."""
        return await self.page.evaluate("""
            () => {
                const btn = Array.from(document.querySelectorAll('button'))
                    .find(b => b.textContent.trim() === 'Create project');
                if (btn) { btn.click(); return true; }
                return false;
            }
        """)

    async def _trusted_click_button(self, *texts: str) -> bool:
        """Deliver a REAL mouse click on the first VISIBLE, enabled button whose
        text contains one of ``texts``.

        Several wizard steps render duplicate buttons (one per step) in the DOM,
        so ``locator.first.click()`` can resolve to a hidden/covered element and
        time out. Locating the visible enabled button in JS, scrolling it to
        centre, then clicking its coordinates with ``page.mouse.click`` gives a
        genuine user gesture that also reliably lands. Returns True if clicked.
        """
        box = await self.page.evaluate("""
            (texts) => {
                const norm = (s) => (s || '').trim().toLowerCase();
                const wanted = texts.map(norm);
                const btns = Array.from(document.querySelectorAll('button, [role="button"]'));
                const b = btns.find(x => x.offsetParent !== null
                    && x.getAttribute('aria-disabled') !== 'true' && !x.disabled
                    && wanted.some(w => norm(x.textContent).includes(w)));
                if (!b) return null;
                b.scrollIntoView({ block: 'center', inline: 'center' });
                const r = b.getBoundingClientRect();
                return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
            }
        """, list(texts))
        if not box:
            return False
        try:
            await asyncio.sleep(0.3)  # let scroll settle
            await self.page.mouse.click(box["x"], box["y"])
            return True
        except Exception as exc:
            logger.debug("trusted button click {!r} failed: {}", texts, exc)
            return False

    async def _wait_for_create_button_enabled(self, *, max_wait_s: float = 20.0) -> None:
        """Poll until 'Create project' button is enabled (aria-disabled != true)."""
        btn = self.page.locator("button:has-text('Create project')").first
        for i in range(int(max_wait_s / 0.5)):
            aria_disabled = await btn.get_attribute("aria-disabled", timeout=2000)
            disabled = await btn.get_attribute("disabled", timeout=2000)
            if aria_disabled != "true" and disabled is None:
                logger.info("'Create project' button enabled after {}s", i * 0.5)
                return
            await asyncio.sleep(0.5)
        logger.warning("'Create project' button still disabled after {}s — clicking anyway", max_wait_s)

    async def _handle_match_service_details(self) -> bool:
        """Fill MATCH Pro's required intermediate service details screen.

        Some MATCH tenants show a post-Step2 form requiring company type,
        acquirer metadata, and replacement-id confirmation before the flow can
        continue to key generation/download screens.
        """
        form_signals = await self.page.evaluate("""
            () => {
                const count = (sel) => document.querySelectorAll(sel).length;
                const text = (document.body?.innerText || '').toLowerCase();
                const signals = {
                    companyTypeRadios: count("input[type='radio'][name$='_accessToBeUsedBy']"),
                    replacementRadios: count("input[type='radio'][name$='_isReplacingClientId']"),
                    icaInputs: count("input[data-testid='acquirerica-text'], input[name*='acquirer'][name*='ica' i], input[name*='ica' i]"),
                    emailInputs: count("input[type='email'], input[data-testid*='email' i], input[name*='email' i]"),
                    hasCompanyText: text.includes('company type') ? 1 : 0,
                    hasIcaText: text.includes('acquirer processing id/ica') ? 1 : 0,
                    hasContactEmailText: text.includes('acquirer contact email') ? 1 : 0,
                };
                const totalSignals = Object.values(signals).reduce((a, b) => a + Number(b || 0), 0);
                // STRONG signals uniquely identify the MATCH Pro service-details
                // form. Generic 'ica'/'email' substring inputs (icaInputs,
                // emailInputs) match unrelated fields — e.g. an oauth1_enc
                // project's Mastercard-encryption key alias — and must NOT
                // trigger MATCH handling on their own.
                const strongSignals =
                    Number(signals.companyTypeRadios) +
                    Number(signals.replacementRadios) +
                    Number(signals.hasCompanyText) +
                    Number(signals.hasIcaText) +
                    Number(signals.hasContactEmailText) +
                    count("input[data-testid='acquirerica-text']");
                return { ...signals, totalSignals, strongSignals };
            }
        """)
        # Gate on strong, MATCH-specific signals only — avoids false positives on
        # oauth1_enc combined flows (e.g. Transaction Notifications) whose
        # encryption-key alias inputs otherwise match the loose ica/email selectors.
        if int(form_signals.get("strongSignals", 0)) == 0:
            return False

        # If terminal controls are present, stop treating this as the active form.
        if await self.page.locator(ProjectCreatedSelectors.download_key_button).count() > 0:
            return False
        if await self.page.locator(ProjectCreatedSelectors.open_project_button).count() > 0:
            return False

        logger.info("MATCH service details screen detected — filling required fields (signals={})", form_signals)
        await screenshot(self.page, "match_service_details_detected")

        pause_match_form = os.environ.get("MCD_PAUSE_MATCH_FORM") == "1"

        # Resolve preferred contact email. If no explicit env is set, preserve portal's pre-filled value.
        requested_email = (
            os.environ.get("MCD_CONTACT_EMAIL", "").strip()
            or os.environ.get("MATCH_CONTACT_EMAIL", "").strip()
            or os.environ.get("MCD_USERNAME", "").strip()
        )
        if not requested_email:
            detected_email = await self.page.evaluate(
                """
                () => {
                    const text = document.body?.innerText || '';
                    const matches = text.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}/ig) || [];
                    return matches.length > 0 ? String(matches[0]).trim() : '';
                }
                """
            )
            requested_email = str(detected_email or "").strip()
        if not requested_email:
            requested_email = f"match-{int(time.time())}@example.com"
            logger.warning(
                "Could not detect logged-in email; using generated fallback email for MATCH form: {}",
                requested_email,
            )

        applied = await self.page.evaluate(
            """
            ({ requestedEmail }) => {
                const labels = Array.from(document.querySelectorAll('label'));

                const setReactInputValue = (input, value) => {
                    if (!input) return false;
                    const setter = Object.getOwnPropertyDescriptor(
                        window.HTMLInputElement.prototype,
                        'value'
                    )?.set;
                    if (setter) {
                        setter.call(input, value);
                    } else {
                        input.value = value;
                    }
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                    input.dispatchEvent(new Event('blur', { bubbles: true }));
                    return true;
                };

                const setRadioChecked = (input) => {
                    if (!input) return false;

                    if (input.id) {
                        try {
                            const safeId = (window.CSS && typeof window.CSS.escape === 'function')
                                ? window.CSS.escape(input.id)
                                : input.id.replace(/([#.;?+*~':"!^$[\\]()=>|/@])/g, '\\$1');
                            const label = document.querySelector(`label[for="${safeId}"]`);
                            if (label) {
                                label.click();
                            }
                        } catch (_e) {
                            // Ignore label-query failures and continue with direct click.
                        }
                    }

                    if (!input.checked) {
                        input.click();
                    }
                    if (!input.checked) {
                        input.checked = true;
                        input.dispatchEvent(new Event('input', { bubbles: true }));
                        input.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                    return !!input.checked;
                };

                const clickRadioFromLabel = (predicate) => {
                    const candidate = labels.find((l) => {
                        const id = l.getAttribute('for');
                        const input = id ? document.getElementById(id) : null;
                        return !!input && predicate((l.textContent || '').trim().toLowerCase());
                    });
                    if (!candidate) return false;
                    const id = candidate.getAttribute('for');
                    const input = id ? document.getElementById(id) : null;
                    return setRadioChecked(input);
                };

                const setInputFromLabelContains = (labelText, value) => {
                    const norm = labelText.toLowerCase();
                    const label = labels.find((l) => {
                        const id = l.getAttribute('for');
                        const input = id ? document.getElementById(id) : null;
                        return !!input && (l.textContent || '').trim().toLowerCase().includes(norm);
                    });
                    if (!label) return { ok: false, value: '' };
                    const id = label.getAttribute('for');
                    const input = id ? document.getElementById(id) : null;
                    if (!input) return { ok: false, value: '' };
                    input.focus();
                    input.value = value;
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                    return { ok: true, value: (input.value || '').trim() };
                };

                const getInputFromLabelContains = (labelText) => {
                    const norm = labelText.toLowerCase();
                    const label = labels.find((l) => {
                        const id = l.getAttribute('for');
                        const input = id ? document.getElementById(id) : null;
                        return !!input && (l.textContent || '').trim().toLowerCase().includes(norm);
                    });
                    if (!label) return { ok: false, value: '' };
                    const id = label.getAttribute('for');
                    const input = id ? document.getElementById(id) : null;
                    if (!input) return { ok: false, value: '' };
                    return { ok: true, value: (input.value || '').trim() };
                };

                const setNoForReplacementQuestion = () => {
                    const questionNode = Array.from(document.querySelectorAll('*')).find((el) => {
                        const t = (el.textContent || '').trim().toLowerCase();
                        return t.includes('is this client id replacing') && t.includes('client id');
                    });
                    if (!questionNode) {
                        return clickRadioFromLabel((txt) => txt === 'no');
                    }
                    let scope = questionNode.parentElement;
                    for (let i = 0; i < 4 && scope; i += 1) {
                        const noLabel = Array.from(scope.querySelectorAll('label')).find(
                            (l) => {
                                const id = l.getAttribute('for');
                                const input = id ? document.getElementById(id) : null;
                                return (l.textContent || '').trim().toLowerCase() === 'no' && !!input;
                            }
                        );
                        if (noLabel) {
                            const id = noLabel.getAttribute('for');
                            const input = id ? document.getElementById(id) : null;
                            return setRadioChecked(input);
                        }
                        scope = scope.parentElement;
                    }
                    return clickRadioFromLabel((txt) => txt === 'no');
                };

                const companySet = clickRadioFromLabel(
                    (txt) => txt.includes('internal') && txt.includes('mastercard') && txt.includes('partner')
                );

                const setAllEmailInputs = (value) => {
                    const candidates = Array.from(document.querySelectorAll('input')).filter((i) => {
                        if (i.disabled || i.readOnly) return false;
                        const t = (i.getAttribute('type') || '').toLowerCase();
                        const n = (i.getAttribute('name') || '').toLowerCase();
                        const d = (i.getAttribute('data-testid') || '').toLowerCase();
                        const p = (i.getAttribute('placeholder') || '').toLowerCase();
                        return t === 'email' || n.includes('email') || d.includes('email') || p.includes('email');
                    });
                    for (const input of candidates) {
                        setReactInputValue(input, value);
                    }
                    return {
                        count: candidates.length,
                        values: candidates.map((i) => (i.value || '').trim()),
                    };
                };

                // Deterministic fallback for MATCH company-type radio.
                const companyRadio = document.querySelector(
                    "input[type='radio'][name$='_accessToBeUsedBy'][value='Internal MasterCard Partner']"
                );
                let companyRadioSet = false;
                if (companyRadio) {
                    companyRadioSet = setRadioChecked(companyRadio);
                }

                let ica = setInputFromLabelContains('acquirer processing id/ica', '123456789');
                if (!ica.ok) {
                    const testidInput = document.querySelector("input[data-testid='acquirerica-text']");
                    if (testidInput) {
                        setReactInputValue(testidInput, '123456789');
                        ica = { ok: true, value: (testidInput.value || '').trim() };
                    }
                }

                let email = requestedEmail
                    ? setInputFromLabelContains('acquirer contact email', requestedEmail)
                    : getInputFromLabelContains('acquirer contact email');
                if (!email.ok) {
                    const emailInput = document.querySelector("input[data-testid='acquirercontactemail-text']");
                    if (emailInput) {
                        if (requestedEmail) {
                            setReactInputValue(emailInput, requestedEmail);
                        }
                        email = { ok: true, value: (emailInput.value || '').trim() };
                    }
                }
                let emailBulk = { count: 0, values: [] };
                if (requestedEmail) {
                    emailBulk = setAllEmailInputs(requestedEmail);
                    if (!email.value && emailBulk.values.length > 0) {
                        email.value = emailBulk.values[0] || '';
                    }
                }

                const replaceNoSet = setNoForReplacementQuestion();
                const replaceNoRadio = document.querySelector(
                    "input[type='radio'][name$='_isReplacingClientId'][value='No']"
                );
                let replaceNoRadioSet = false;
                if (replaceNoRadio) {
                    replaceNoRadioSet = setRadioChecked(replaceNoRadio);
                }

                const domSnapshot = {
                    labels: labels
                        .map((l) => ({
                            text: (l.textContent || '').trim(),
                            forId: l.getAttribute('for') || '',
                        }))
                        .filter((x) => x.text)
                        .slice(0, 40),
                    inputs: Array.from(document.querySelectorAll('input')).map((i) => ({
                        id: i.id || '',
                        name: i.getAttribute('name') || '',
                        type: i.getAttribute('type') || '',
                        testid: i.getAttribute('data-testid') || '',
                        value: (i.value || '').trim(),
                    })),
                };

                return {
                    companySet: companySet || companyRadioSet,
                    icaSet: ica.ok,
                    icaValue: ica.value,
                    emailSet: (email.ok && !!email.value) || emailBulk.values.some((v) => !!v),
                    emailValue: email.value,
                    emailFieldCount: emailBulk.count,
                    replaceNoSet: replaceNoSet || replaceNoRadioSet,
                    domSnapshot,
                };
            }
            """,
            {"requestedEmail": requested_email},
        )

        logger.info(
            "MATCH service details applied: company_internal={} ica_set={} ica='{}' email_set={} email='{}' email_fields={} replace_no={}",
            applied.get("companySet"),
            applied.get("icaSet"),
            applied.get("icaValue"),
            applied.get("emailSet"),
            applied.get("emailValue"),
            applied.get("emailFieldCount"),
            applied.get("replaceNoSet"),
        )
        logger.debug("MATCH service details DOM snapshot: {}", applied.get("domSnapshot"))

        # Some tenants render email later after company type selection; do a second pass.
        if requested_email and not applied.get("emailSet"):
            for _ in range(8):
                await asyncio.sleep(0.5)
                email_probe = await self.page.evaluate(
                    """
                    ({ requestedEmail }) => {
                        const setReactInputValue = (input, value) => {
                            if (!input) return false;
                            const setter = Object.getOwnPropertyDescriptor(
                                window.HTMLInputElement.prototype,
                                'value'
                            )?.set;
                            if (setter) {
                                setter.call(input, value);
                            } else {
                                input.value = value;
                            }
                            input.dispatchEvent(new Event('input', { bubbles: true }));
                            input.dispatchEvent(new Event('change', { bubbles: true }));
                            input.dispatchEvent(new Event('blur', { bubbles: true }));
                            return true;
                        };

                        const candidates = Array.from(document.querySelectorAll('input')).filter((i) => {
                            const t = (i.getAttribute('type') || '').toLowerCase();
                            const n = (i.getAttribute('name') || '').toLowerCase();
                            const d = (i.getAttribute('data-testid') || '').toLowerCase();
                            return (
                                t === 'email' ||
                                n.includes('email') ||
                                n.includes('acquirercontactemail') ||
                                n.includes('contactemail') ||
                                d.includes('acquirercontactemail') ||
                                d.includes('contactemail')
                            );
                        });

                        if (candidates.length === 0) {
                            return { found: false, value: '' };
                        }

                        const input = candidates[0];
                        setReactInputValue(input, requestedEmail);
                        return { found: true, value: (input.value || '').trim() };
                    }
                    """,
                    {"requestedEmail": requested_email},
                )
                if email_probe.get("found") and email_probe.get("value") == requested_email:
                    applied["emailSet"] = True
                    applied["emailValue"] = email_probe.get("value")
                    logger.info("MATCH email second-pass set to requested value")
                    break

        if requested_email and not applied.get("emailSet"):
            logger.warning(
                "MATCH email field was not present/set in this tenant form variant; proceeding without explicit email fill"
            )
        if not requested_email and not applied.get("emailValue"):
            logger.warning(
                "MATCH email remains blank; set MCD_CONTACT_EMAIL (or MATCH_CONTACT_EMAIL) to force the logged-in user email"
            )

        # Optional manual takeover for diagnosing tenant-specific MATCH forms.
        # Pause AFTER automated field fill so operators can verify what was set.
        if pause_match_form:
            pause_ctx = await self.page.evaluate("""
                () => {
                    const candidates = Array.from(document.querySelectorAll(
                        "input[type='email'], input[data-testid='acquirerica-text'], " +
                        "input[type='radio'][name$='_accessToBeUsedBy'], input[type='radio'][name$='_isReplacingClientId']"
                    ));
                    if (candidates.length > 0) {
                        candidates[0].scrollIntoView({ behavior: 'instant', block: 'center' });
                    }
                    return {
                        url: location.href,
                        candidateCount: candidates.length,
                        inputNames: candidates.slice(0, 12).map((el) => ({
                            id: el.id || '',
                            name: el.getAttribute('name') || '',
                            type: el.getAttribute('type') || '',
                            testid: el.getAttribute('data-testid') || '',
                            value: (el.value || '').trim(),
                            checked: !!el.checked,
                        })),
                    };
                }
            """)
            logger.info("MATCH post-fill pause context: {}", pause_ctx)
            await screenshot(self.page, "match_service_details_postfill_pause")
            logger.warning(
                "MCD_PAUSE_MATCH_FORM=1 — paused after auto-fill on MATCH form. "
                "Review/adjust fields and click Proceed in the browser, then press Enter here to resume."
            )
            await asyncio.get_event_loop().run_in_executor(
                None,
                input,
                ">>> Press Enter after reviewing MATCH auto-fill... ",
            )
            return False

        # Proceed button can be blocked by overlays; prefer direct JS click.
        clicked = await self.page.evaluate("""
            () => {
                const btn =
                    document.querySelector("button[data-testid='proceed-btn']") ||
                    document.querySelector("button#submit") ||
                    Array.from(document.querySelectorAll('button')).find(
                        b => (b.textContent || '').trim() === 'Proceed'
                    );
                if (!btn) return false;
                if (btn.disabled) return false;
                if ((btn.getAttribute('aria-disabled') || '').toLowerCase() === 'true') return false;
                btn.click();
                return true;
            }
        """)
        if clicked:
            logger.info("Submitted MATCH service details screen")
            await asyncio.sleep(2.0)
            return True

        logger.warning("MATCH service details detected but Proceed button was not actionable")
        return False

    async def create_key_step2(self) -> None:
        """Wait for Step 2 'Create project' to enable, log state, and JS-click it."""
        await self._wait_for_create_button_enabled()
        btn_info = await self.page.evaluate("""
            () => {
                const btn = Array.from(document.querySelectorAll('button'))
                    .find(b => b.textContent.trim() === 'Create project');
                if (!btn) return { found: false };
                return {
                    found: true,
                    disabled: btn.disabled,
                    ariaDisabled: btn.getAttribute('aria-disabled'),
                    display: getComputedStyle(btn).display,
                    visibility: getComputedStyle(btn).visibility,
                };
            }
        """)
        logger.info("'Create project' button state: {}", btn_info)
        await screenshot(self.page, "step2_before_submit")

        # Optional manual takeover before leaving Step 2.
        if os.environ.get("MCD_PAUSE_BEFORE_STEP2_CREATE") == "1":
            logger.warning(
                "MCD_PAUSE_BEFORE_STEP2_CREATE=1 — paused before Step 2 submit. "
                "Use the browser to click Create project and continue manually, then press Enter to resume."
            )
            await asyncio.get_event_loop().run_in_executor(
                None,
                input,
                ">>> Press Enter after manual Step 2 submit... ",
            )
            return

        logger.info("Clicking 'Create project' on Step 2")
        clicked = await self._js_click_create_project()
        if not clicked:
            logger.warning("'Create project' button not found via JS — falling back to locator click")
            await self.page.locator("button:has-text('Create project')").first.click(force=True)

    async def wait_for_download_after_step2(
        self,
        *,
        alias: str,
        password: str,
        timeout_ms: int = 90000,
        skip_step3: bool = False,
    ) -> str:
        """After Step 2 click, handle multi-step wizards and wait for final download/confirmation.

        Some APIs (e.g. clarity, txnotify) have a Step 3 "Additional credentials" that must be
        filled and submitted before the key download appears. This method detects Step 3 and
        handles it automatically.

        If ``skip_step3`` is True, click the "Skip this step" button instead of filling/creating
        on Step 3 (used by APIs whose Step 3 offers an optional Mastercard-side encryption key
        we don't want, e.g. Transaction Notifications).

        Returns: 'download' | 'open_project' | 'project_page'
        """
        deadline = timeout_ms / 1000
        poll_interval = 0.5
        elapsed = 0.0
        _step3_clicked = False  # guard against re-clicking step 3 button in rapid succession
        _creds_resubmitted = False  # guard for re-detection of credentials form (separate from step3)
        _match_form_submit_attempts = 0

        while elapsed < deadline:
            url = self.page.url

            # Terminal: navigated to project details page.
            if "/project-details/" in url and "/create-project" not in url:
                logger.info("Landed on project detail page — {}", url)
                return "project_page"
            if "dashboard" in url and "/create-project" not in url:
                logger.info("Redirected to dashboard — {}", url)
                return "project_page"

            # Terminal: confirmation page.
            if await self.page.locator(ProjectCreatedSelectors.download_key_button).count() > 0:
                logger.info("Download key button appeared — {}", url)
                return "download"
            if await self.page.locator(ProjectCreatedSelectors.open_project_button).count() > 0:
                logger.info("Open project button appeared — {}", url)
                return "open_project"

            # Handle MATCH intermediate service-details form only after checking
            # terminal states; the form can coexist in DOM with post-submit
            # controls and should not preempt download/open-project handling.
            if await self._handle_match_service_details():
                _match_form_submit_attempts += 1
                if _match_form_submit_attempts > 3:
                    raise RuntimeError(
                        "MATCH service details form did not advance after 3 submissions; "
                        "check required field bindings/selectors"
                    )
                continue

            # Re-detection: some APIs (e.g. Carbon Calculator) have an intermediate
            # "Service details" step before the credentials form. The wizard may have
            # advanced us to Step 3 (Project credentials) without us clicking Create project
            # on it. Detect this and submit the credentials form using a native pointer click.
            # Use a separate flag so _step3_clicked (for Step 4 detection) is not blocked.
            if not _creds_resubmitted and elapsed >= 1.0:
                key_alias_visible = await self.page.locator("[data-testid='key-alias-input']:visible").count() > 0
                if key_alias_visible:
                    logger.info(
                        "Re-detected credentials form during polling "
                        "(elapsed={:.1f}s) — clicking 'Create project'", elapsed
                    )
                    await self._wait_for_create_button_enabled(max_wait_s=5.0)
                    await self.page.locator("button:has-text('Create project')").first.click()
                    logger.info("Clicked 'Create project' on re-detected credentials form")
                    _creds_resubmitted = True
                    await asyncio.sleep(2.0)
                    continue

            # MATCH/portal variant: final wizard step can expose a visible
            # "Skip this step" button and "Create project" CTA without the
            # literal "Additional credentials" heading.
            skip_btn_visible = await self.page.locator("button:has-text('Skip this step')").count()
            create_btn_visible = await self.page.locator("button:has-text('Create project')").count()
            # Guard: Step 3 "Project credentials" form also has "Skip this step" (CSR path)
            # and "Create project". Do NOT fire this detection while that form is still on
            # screen. Use the key-alias-input's visibility to detect whether we're on the
            # credentials step (True on Step 3; False once wizard advances to Step 4+).
            on_creds_step = await self.page.locator("[data-testid='key-alias-input']:visible").count() > 0
            if skip_btn_visible > 0 and create_btn_visible > 0 and not _step3_clicked and not on_creds_step:
                logger.info("Final key step detected via visible 'Skip this step' + 'Create project' buttons")
                await screenshot(self.page, "step3_detected_via_skip")

                if skip_step3:
                    # The final "Additional credentials" step only offers to
                    # generate an Encryption Key that "will be generated when your
                    # project is created" — no user action is required. The most
                    # reliable completion is to click the primary 'Create project'
                    # CTA with a TRUSTED click, which creates the project (with the
                    # signing key from Step 3 + auto-generated encryption key).
                    # 'Skip this step' opens an extra "add credentials later?"
                    # confirmation that is flakier, so we avoid it.
                    logger.info("Final key step — clicking 'Create project' (enc key auto-generated)")
                    await self._wait_for_create_button_enabled(max_wait_s=8.0)
                    if not await self._trusted_click_button("Create project"):
                        logger.warning(
                            "Create project: no visible enabled button — JS fallback"
                        )
                        await self._js_click_create_project()
                else:
                    # MATCH-specific behavior: proceed with "Create project".
                    await self._wait_for_create_button_enabled(max_wait_s=8.0)
                    clicked = await self._js_click_create_project()
                    logger.info("Clicked 'Create project' on final key step — found={}", clicked)

                _step3_clicked = True
                await asyncio.sleep(1.0)
                continue

            # Step 3 detection: check if "Additional credentials" step is visible.
            # Guard: sidebar shows "Additional credentials" label even when on Step 3 (Project
            # credentials). Only fire when the key-alias-input form is no longer visible.
            step3_heading = await self.page.locator("text=Additional credentials").count()
            on_creds_step = await self.page.locator("[data-testid='key-alias-input']:visible").count() > 0
            if step3_heading > 0 and not _step3_clicked and not on_creds_step:
                logger.info("Step 3 (Additional credentials) detected")
                await screenshot(self.page, "step3_detected")

                # Optional manual takeover: when MCD_PAUSE_STEP3=1, block here
                # so the operator can drive the browser by hand and observe
                # the actual portal flow (used for diagnosing wizards like
                # Transaction Notifications). Resume by pressing Enter in the
                # terminal once the wizard is finished and a key has been
                # downloaded / the project page is reached.
                if os.environ.get("MCD_PAUSE_STEP3") == "1":
                    logger.warning(
                        "MCD_PAUSE_STEP3=1 — pausing on Step 3. "
                        "Drive the wizard manually in the browser, then press Enter here to resume."
                    )
                    await asyncio.get_event_loop().run_in_executor(
                        None, input, ">>> Press Enter to resume automation after manual Step 3 walkthrough... "
                    )
                    # After manual takeover, re-poll the page state instead of
                    # re-clicking — the user may already be on the download or
                    # project-details page.
                    _step3_clicked = True
                    await asyncio.sleep(0.5)
                    continue

                # Per-API override: skip filling encryption-key fields on the Additional
                # credentials step. If "Create project" exists on this step, click it without
                # filling. If there is no "Create project" (e.g. Carbon Calculator Step 4 only
                # shows "Skip this step"), click "Skip this step" and handle the confirmation
                # dialog so the wizard lands on the project page.
                if skip_step3:
                    _create_count = await self.page.locator("button:has-text('Create project')").count()
                    if _create_count > 0:
                        logger.info(
                            "Step 3 has skip_step3=True — clicking 'Create project' without filling encryption fields"
                        )
                        await self._wait_for_create_button_enabled(max_wait_s=5.0)
                        clicked = await self._js_click_create_project()
                        logger.info("Clicked 'Create project' on Step 3 (skip_step3) — found={}", clicked)
                    else:
                        # No 'Create project' — fall back to 'Skip this step' + confirm dialog.
                        _skip_loc = self.page.locator("button:has-text('Skip this step')")
                        if await _skip_loc.count() > 0:
                            logger.info(
                                "Step 3 skip_step3=True, no 'Create project' — clicking 'Skip this step'"
                            )
                            await _skip_loc.first.click()
                            await asyncio.sleep(0.5)
                            _dialog = self.page.locator(
                                "[role='dialog']:visible, [role='alertdialog']:visible"
                            )
                            if await _dialog.count() > 0:
                                for _ct in ("Skip", "Yes", "Confirm", "Continue", "OK"):
                                    _cb = _dialog.first.locator(f"button:has-text('{_ct}')")
                                    if await _cb.count() > 0:
                                        logger.info(
                                            "Skip confirmation dialog (step3_heading) — clicking {!r}", _ct
                                        )
                                        await _cb.first.click()
                                        break
                            else:
                                for _ct in ("Yes", "Confirm", "Continue", "OK"):
                                    _cb = self.page.locator(f"button:has-text('{_ct}'):visible")
                                    if await _cb.count() > 0:
                                        logger.info(
                                            "Skip confirmation (no dialog role, step3_heading) — clicking {!r}", _ct
                                        )
                                        await _cb.first.click()
                                        break
                        else:
                            logger.warning("skip_step3=True but neither 'Create project' nor 'Skip this step' found on Step 3")
                    _step3_clicked = True
                    await asyncio.sleep(1.0)
                    continue

                # Check if this is a "no action needed" informational step (e.g., auto-generated encryption key).
                no_action_text = await self.page.locator("text=There are no actions needed").count()

                if no_action_text > 0:
                    if skip_step3:
                        # skip_step3=True means we don't want to download the auto-generated cert.
                        # Try the 'Skip this step' button; fall back to 'Create project' if absent.
                        skip_loc = self.page.locator("button:has-text('Skip this step')")
                        if await skip_loc.count() > 0:
                            logger.info("Step 3 'no actions needed' + skip_step3=True — clicking 'Skip this step'")
                            await skip_loc.first.click()
                        else:
                            logger.info("Step 3 'no actions needed' + skip_step3=True — no skip button, clicking 'Create project'")
                            await self._wait_for_create_button_enabled(max_wait_s=5.0)
                            await self._js_click_create_project()
                    else:
                        # No inputs to fill — just click 'Create project'.
                        logger.info("Step 3 has no inputs (auto-generated key) — clicking 'Create project'")
                        await self._wait_for_create_button_enabled(max_wait_s=5.0)
                        clicked = await self._js_click_create_project()
                        logger.info("Clicked 'Create project' on Step 3 (no-action) — found={}", clicked)
                else:
                    # Step 3 has inputs — fill them.
                    logger.info("Step 3 has inputs — filling credentials")
                    await self.fill_step2_credentials(alias=alias, password=password)
                    await self._wait_for_create_button_enabled(max_wait_s=10.0)
                    await screenshot(self.page, "step3_before_submit")
                    clicked = await self._js_click_create_project()
                    logger.info("Clicked 'Create project' on Step 3 (with inputs) — found={}", clicked)
                
                _step3_clicked = True
                await asyncio.sleep(1.0)
                continue

            # Detect inline portal error — ignore single-char strings like '*'.
            error_loc = self.page.locator(
                "[role='alert']:visible, "
                ".alert-danger:visible, "
                ".toast-error:visible, "
                "[class*='toast']:visible"
            )
            if await error_loc.count() > 0:
                err_text = (await error_loc.first.inner_text()).strip()
                if len(err_text) > 3:
                    logger.warning("Portal error after Step submit: {!r}", err_text)
                    raise RuntimeError(f"Portal error on Step submit: {err_text!r}")

            await asyncio.sleep(poll_interval)
            elapsed += poll_interval

        raise TimeoutError(f"Download/Open project button not found within {timeout_ms}ms after Step 2")

    async def download_key_file(self, *, dest_dir: Path, filename_hint: str = "key") -> Path:
        """Click 'Download key file' and save the file."""
        before_files = {p.name for p in dest_dir.glob("*") if p.is_file()}
        logger.info("Clicking 'Download key file'")
        try:
            async with self.page.expect_download(timeout=90000) as dl_info:
                await self.page.locator(ProjectCreatedSelectors.download_key_button).click()
            download = await dl_info.value
            original = download.suggested_filename or f"{filename_hint}.p12"
            # If a filename_hint was supplied, prepend it to the saved name so that
            # downstream artifact classification (enc vs signing) can rely on tokens
            # like "-enc" being present in the stem. Portal-suggested names (e.g.
            # MCD_Sandbox_*_API_Keys.zip) do not carry that distinction.
            if filename_hint and filename_hint != "key":
                ext = Path(original).suffix or ".zip"
                saved_name = f"{filename_hint}{ext}"
            else:
                saved_name = original
            dest = dest_dir / saved_name
            await save_download(download, dest)
            logger.info("Downloaded key file: {}", dest)
            return dest
        except Exception as err:
            logger.warning("Download event not captured: {} — checking filesystem fallback", err)
            # Some portal variants trigger browser-managed downloads without
            # Playwright download events; poll destination for newly created files.
            for _ in range(20):
                await asyncio.sleep(1.0)
                candidates = [
                    p for p in dest_dir.glob("*")
                    if p.is_file() and p.name not in before_files and p.suffix.lower() in {".zip", ".p12", ".pem", ".crt"}
                ]
                if candidates:
                    newest = max(candidates, key=lambda p: p.stat().st_mtime)
                    logger.info("Using filesystem fallback downloaded file: {}", newest)
                    return newest
            raise

    async def open_project(self) -> str:
        """Click 'Open project' and return the resulting URL."""
        async with self.page.expect_navigation():
            await self.page.locator(ProjectCreatedSelectors.open_project_button).click()
        logger.info("Opened project — at {}", self.page.url)
        return self.page.url

    # ------------------------------------------------------------------
    # Isolated per-API fill methods (no shared optional-param branching)
    # ------------------------------------------------------------------

    async def fill_ofin(self, *, project_name: str, region: str) -> None:
        """Fill the Open Finance (OAuth 2.0) create-project form.

        Step 1 has two separate selects:
          1. "APIs *" react-select — choose the ofin offering (e.g. "US Open Finance")
          2. "Region *" react-select — appears AFTER API selection; choose "United States of America"

        Strategy: open the APIs dropdown without typing, pick the first option (or the one
        whose text best matches the desired region), then handle the Region dropdown if it appears.
        """
        logger.info("fill_ofin: name={!r} region={!r}", project_name, region)

        name_loc = self.page.locator(CreateProjectSelectors.name_input)
        await name_loc.click(click_count=3)
        await name_loc.press_sequentially(project_name, delay=50)

        await self.page.locator("label:has-text('No')").first.click()

        # Scroll to reveal the "Select at least one API" section.
        await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(0.8)

        # ----------------------------------------------------------------
        # Step A: Open the "APIs *" react-select and pick the right option.
        # ----------------------------------------------------------------
        api_input = self.page.locator("#react-select-2-input").first
        await api_input.scroll_into_view_if_needed()
        await api_input.click()
        await asyncio.sleep(0.6)

        # Log all visible options so we can pick the right one.
        options_text: list[str] = await self.page.evaluate("""
            () => Array.from(document.querySelectorAll(
                "[class*='option'], [id*='react-select'][id*='option'], [role='option']"
            )).map(el => el.textContent.trim()).filter(Boolean)
        """)
        logger.info("APIs dropdown options: {}", options_text)
        await screenshot(self.page, "ofin_apis_dropdown_open")

        # Pick the API offering whose label best matches the requested region.
        # Examples seen in the portal:
        #   "US Open Finance"        -> region "United States of America"
        #   "Australia Open Finance" -> region "Australia"
        # We try a few region-derived hints (full name, country word, ISO-ish prefix)
        # and fall back to a generic "Open Finance" match, then the first option.
        region_lower = (region or "").lower()
        region_hints: list[str] = []
        if region_lower:
            region_hints.append(region_lower)
            # First word of the region, e.g. "australia", "united"
            region_hints.append(region_lower.split()[0])
        # Known country-code shorthands used in portal labels
        country_aliases = {
            "united states of america": ["us", "u.s.", "usa", "united states"],
            "australia": ["au", "aus", "australian"],
            "united kingdom": ["uk", "u.k.", "gb"],
            "canada": ["ca", "can"],
        }
        region_hints.extend(country_aliases.get(region_lower, []))

        def _option_matches(option: str, hint: str) -> bool:
            text = option.lower()
            # Match short hints as whole tokens to avoid e.g. "au" matching "auth".
            if len(hint) <= 3:
                import re as _re
                return bool(_re.search(rf"\b{_re.escape(hint)}\b", text))
            return hint in text

        pick = None
        for hint in region_hints:
            for opt in options_text:
                if _option_matches(opt, hint):
                    pick = opt
                    break
            if pick:
                break
        if not pick:
            generic = [o for o in options_text if "open finance" in o.lower()]
            pick = generic[0] if generic else (options_text[0] if options_text else None)
        logger.info("Selecting API option: {!r} (region={!r})", pick, region)

        if pick:
            option_loc = self.page.locator(
                f"[role='option']:has-text('{pick}'), "
                f"[class*='option']:has-text('{pick}')"
            ).first
            await option_loc.click(timeout=8000)
            logger.info("Clicked API option: {!r}", pick)
        else:
            logger.warning("No options found in APIs dropdown — proceeding without selection")

        await asyncio.sleep(0.8)
        await screenshot(self.page, "ofin_after_api_selection")

        # ----------------------------------------------------------------
        # Step B: Handle Region dropdown if it appeared after API selection.
        # ----------------------------------------------------------------
        # Check if a second react-select input appeared (react-select-3-input or similar).
        region_inputs: list[dict] = await self.page.evaluate("""
            () => Array.from(document.querySelectorAll('input[id*="react-select"]'))
                .filter(el => el.offsetParent !== null)  // only visible
                .map(el => ({ id: el.id, value: el.value }))
        """)
        logger.info("Visible react-select inputs after API selection: {}", region_inputs)

        # If more than one react-select is visible, the second one is likely Region.
        region_rs_inputs = [r for r in region_inputs if r["id"] != "react-select-2-input"]
        if region_rs_inputs:
            region_sel = f"#{region_rs_inputs[0]['id']}"
            logger.info("Region react-select found: {!r}", region_sel)
            region_inp = self.page.locator(region_sel).first
            await region_inp.scroll_into_view_if_needed()
            # Use force=True — a decorative .check overlay div intercepts pointer events
            # on the react-select container, blocking normal clicks.
            await region_inp.click(force=True)
            await asyncio.sleep(0.5)

            # Log region options.
            region_opts: list[str] = await self.page.evaluate("""
                () => Array.from(document.querySelectorAll(
                    "[class*='option'], [role='option']"
                )).map(el => el.textContent.trim()).filter(Boolean)
            """)
            logger.info("Region dropdown options: {}", region_opts)
            await screenshot(self.page, "ofin_region_dropdown_open")

            # Type the first word of the requested region to filter, then click
            # the option whose visible text matches the full region name.
            filter_text = (region or "").split()[0] if region else ""
            if filter_text:
                await region_inp.press_sequentially(filter_text, delay=50)
                await asyncio.sleep(0.8)

            region_option = self.page.locator(
                f"[role='option']:has-text('{region}'), "
                f"[class*='option']:has-text('{region}')"
            ).first
            try:
                await region_option.click(timeout=8000)
                logger.info("Region {!r} selected", region)
            except Exception:
                await screenshot(self.page, "ofin_region_dropdown_fail")
                raise RuntimeError(f"Could not select region {region!r} — check screenshot")
        else:
            logger.info("No separate region dropdown appeared — region may be embedded in API option")

    async def fill_priceless(self, *, project_name: str, api_selection: str) -> None:
        """Fill the Priceless Cities create-project form.

        Step 1 requires:
          1. Project name
          2. 'No' for company
          3. Select the 'Priceless Specials' sub-API card/checkbox
        """
        logger.info("fill_priceless: name={!r} api_selection={!r}", project_name, api_selection)

        name_loc = self.page.locator(CreateProjectSelectors.name_input)
        await name_loc.click(click_count=3)
        await name_loc.press_sequentially(project_name, delay=50)

        await self.page.locator("label:has-text('No')").first.click()

        # The "Select at least one API" section uses the same react-select dropdown as ofin.
        # Scroll to reveal it, open the dropdown, and pick "Priceless Specials".
        await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(0.6)

        api_input = self.page.locator("#react-select-2-input").first
        await api_input.scroll_into_view_if_needed()
        await api_input.click()
        await asyncio.sleep(0.6)

        await screenshot(self.page, "priceless_apis_dropdown_open")

        # Type to filter to "Priceless Specials".
        await api_input.press_sequentially("Priceless", delay=60)
        await asyncio.sleep(0.8)

        option_loc = self.page.locator(
            f"[role='option']:has-text('{api_selection}'), "
            f"[class*='option']:has-text('{api_selection}')"
        ).first
        try:
            await option_loc.click(timeout=8000)
            logger.info("Selected API: {!r}", api_selection)
        except Exception:
            await screenshot(self.page, "priceless_api_select_fail")
            raise RuntimeError(f"Could not select {api_selection!r} from dropdown — check screenshot")

        # Close the dropdown so Proceed is not blocked.
        await api_input.press("Escape")
        await asyncio.sleep(0.4)

    # ------------------------------------------------------------------
    # MATCH (Pro) end-to-end provisioning
    # ------------------------------------------------------------------

    async def _detect_logged_in_email(self) -> str:
        """Best-effort detection of the portal's logged-in user email.

        Strategy:
          1. Decode the ``auth_token`` JWT cookie — its payload contains
             ``alias`` set to the user's email (verified empirically against
             developer.mastercard.com sessions).
          2. Fall back to scraping common header/profile DOM regions.
        """
        # --- Strategy 1: parse auth_token JWT cookie -----------------------
        try:
            cookies = await self.page.context.cookies()
            for cookie in cookies:
                if cookie.get("name") != "auth_token":
                    continue
                token = cookie.get("value", "")
                parts = token.split(".")
                if len(parts) != 3:
                    continue
                payload = parts[1] + "=" * (-len(parts[1]) % 4)
                try:
                    body = base64.urlsafe_b64decode(payload).decode("utf-8", "ignore")
                    data = json.loads(body)
                except Exception:
                    continue
                for key in ("alias", "email", "preferred_username", "sub"):
                    val = data.get(key)
                    if isinstance(val, str) and "@" in val:
                        return val.strip()
        except Exception as err:
            logger.debug("auth_token JWT scrape failed: {}", err)

        # --- Strategy 2: scrape DOM ---------------------------------------
        try:
            email = await self.page.evaluate(
                r"""
                () => {
                    const re = /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i;
                    const candidates = [
                        ...document.querySelectorAll(
                            "[data-testid*='user' i], [data-testid*='profile' i], " +
                            "[class*='user' i], [class*='profile' i], header, nav"
                        ),
                    ];
                    for (const el of candidates) {
                        const t = el.textContent || '';
                        const m = t.match(re);
                        if (m) return m[0];
                    }
                    const body = document.body ? (document.body.innerText || '') : '';
                    const m = body.match(re);
                    return m ? m[0] : '';
                }
                """
            )
            return (email or "").strip()
        except Exception:
            return ""

    async def _resolve_contact_email(self) -> str:
        """Resolve the email used for the MATCH 'Acquirer contact email' field.

        Order of precedence:
          1. ``MCD_CONTACT_EMAIL`` env var
          2. ``MATCH_CONTACT_EMAIL`` env var
          3. Detected email from the logged-in portal session (auth_token JWT
             ``alias`` claim, or DOM scrape)
          4. ``MCD_USERNAME`` env var (last resort — may be a username, not email)
          5. Generated fallback ``match-test-<ts>@example.com``
        """
        for env_key in ("MCD_CONTACT_EMAIL", "MATCH_CONTACT_EMAIL"):
            val = (os.environ.get(env_key) or "").strip()
            if val and "@" in val:
                logger.info("MATCH contact email source={} value={}", env_key, val)
                return val
        detected = await self._detect_logged_in_email()
        if detected and "@" in detected:
            logger.info("MATCH contact email source=session value={}", detected)
            return detected
        mcd_user = (os.environ.get("MCD_USERNAME") or "").strip()
        if mcd_user and "@" in mcd_user:
            logger.info("MATCH contact email source=MCD_USERNAME value={}", mcd_user)
            return mcd_user
        fallback = f"match-test-{int(time.time())}@example.com"
        logger.warning("MATCH contact email source=fallback value={}", fallback)
        return fallback

    async def _click_proceed_btn(self) -> bool:
        """Click ``button[data-testid='proceed-btn']`` if visible and enabled."""
        return await self.page.evaluate(
            """
            () => {
                const btn = document.querySelector("button[data-testid='proceed-btn']");
                if (!btn) return false;
                if (btn.disabled) return false;
                if ((btn.getAttribute('aria-disabled') || '').toLowerCase() === 'true') return false;
                btn.scrollIntoView({ behavior: 'instant', block: 'center' });
                btn.click();
                return true;
            }
            """
        )

    async def _wait_for_proceed_enabled(self, timeout_ms: int = 20000) -> None:
        """Wait until ``proceed-btn`` is mounted and not disabled."""
        await self.page.wait_for_function(
            """
            () => {
                const btn = document.querySelector("button[data-testid='proceed-btn']");
                if (!btn) return false;
                if (btn.disabled) return false;
                if ((btn.getAttribute('aria-disabled') || '').toLowerCase() === 'true') return false;
                return true;
            }
            """,
            timeout=timeout_ms,
        )

    async def _click_radio_label(self, name_suffix: str, value: str, timeout_ms: int = 10000) -> bool:
        """Click a radio (or its associated label) using a real Playwright click.

        Strategy: locate the radio's id, then try in order:
          1. Click the radio input directly (the recording shows the user
             clicked the input itself for the Yes/No radios).
          2. Click the associated ``label[for=id]`` (used for the longer
             company-type labels).
          3. JS click + dispatch change as a final fallback.
        """
        id_value = await self.page.evaluate(
            """
            ({ nameSuffix, value }) => {
                const radio = Array.from(document.querySelectorAll("input[type='radio']"))
                    .find((r) =>
                        (r.getAttribute('name') || '').endsWith(nameSuffix) &&
                        (r.getAttribute('value') || '') === value
                    );
                return radio ? radio.id : '';
            }
            """,
            {"nameSuffix": name_suffix, "value": value},
        )
        if not id_value:
            return False

        async def _is_checked() -> bool:
            return bool(await self.page.evaluate(
                "(id) => { const el = document.getElementById(id); return !!(el && el.checked); }",
                id_value,
            ))

        # Strategy 1: click the input directly (force=True since custom UI
        # often hides the native input behind a styled wrapper).
        try:
            input_loc = self.page.locator(f"input[id='{id_value}']").first
            await input_loc.scroll_into_view_if_needed()
            await input_loc.click(force=True, timeout=timeout_ms)
            await asyncio.sleep(0.3)
            if await _is_checked():
                return True
        except Exception as err:
            logger.debug("input click failed for {}={}: {}", name_suffix, value, err)

        # Strategy 2: click the associated label.
        try:
            label_loc = self.page.locator(f"label[for='{id_value}']").first
            await label_loc.wait_for(state="visible", timeout=timeout_ms)
            await label_loc.scroll_into_view_if_needed()
            await label_loc.click()
            await asyncio.sleep(0.3)
            if await _is_checked():
                return True
        except Exception as err:
            logger.debug("label click failed for {}={}: {}", name_suffix, value, err)

        # Strategy 3: JS click + change event.
        await self.page.evaluate(
            """
            (id) => {
                const el = document.getElementById(id);
                if (!el) return;
                try { el.click(); } catch (_e) {}
                if (!el.checked) {
                    el.checked = true;
                    el.dispatchEvent(new Event('input', { bubbles: true }));
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                }
            }
            """,
            id_value,
        )
        await asyncio.sleep(0.3)
        return await _is_checked()

    async def _set_react_value(self, selector: str, value: str) -> bool:
        """Set a React-controlled input's value and dispatch realistic events."""
        return await self.page.evaluate(
            """
            ({ selector, value }) => {
                const input = document.querySelector(selector);
                if (!input) return false;
                const setter = Object.getOwnPropertyDescriptor(
                    window.HTMLInputElement.prototype,
                    'value'
                )?.set;
                if (setter) {
                    setter.call(input, value);
                } else {
                    input.value = value;
                }
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
                input.dispatchEvent(new Event('blur', { bubbles: true }));
                return true;
            }
            """,
            {"selector": selector, "value": value},
        )

    async def _check_radio_by_name_value(self, name_suffix: str, value: str) -> bool:
        """Check a radio whose ``name`` ends with ``name_suffix`` and value == ``value``."""
        return await self.page.evaluate(
            """
            ({ nameSuffix, value }) => {
                const radio = Array.from(document.querySelectorAll("input[type='radio']"))
                    .find((r) =>
                        (r.getAttribute('name') || '').endsWith(nameSuffix) &&
                        (r.getAttribute('value') || '') === value
                    );
                if (!radio) return false;
                if (radio.id) {
                    try {
                        const safeId = (window.CSS && typeof window.CSS.escape === 'function')
                            ? window.CSS.escape(radio.id)
                            : radio.id;
                        const label = document.querySelector(`label[for="${safeId}"]`);
                        if (label) label.click();
                    } catch (_e) {}
                }
                if (!radio.checked) {
                    try { radio.click(); } catch (_e) {}
                }
                if (!radio.checked) {
                    radio.checked = true;
                    radio.dispatchEvent(new Event('input', { bubbles: true }));
                    radio.dispatchEvent(new Event('change', { bubbles: true }));
                }
                return !!radio.checked;
            }
            """,
            {"nameSuffix": name_suffix, "value": value},
        )

    async def provision_match(
        self,
        *,
        project_name: str,
        alias: str,
        password: str,
        dest_dir: Path,
        filename_hint: str,
        ica: str = "123456789",
        company_type: str = "Internal MasterCard Partner",
        is_replacing: str = "No",
    ) -> tuple[Path, str]:
        """Drive the entire MATCH create-project flow in one page.

        Mirrors the manual recording at logs/recordings/.../trace.jsonl:
          1. fill project-name
          2. click proceed-btn (form Step 1)
          3. fill MATCH service-details (company radio, ICA, contact email,
             isReplacingClientId='No')
          4. click proceed-btn (form Step 2)
          5. fill key-alias-input + key-store-password-input
          6. click proceed-btn (label becomes 'Create project')
          7. click download-key-action-project-creation, save zip
          8. click proceed-button-create-new-project (Open project)
          9. wait for /project-details/<uuid>

        Returns ``(downloaded_zip_path, project_uuid)``.
        """
        logger.info(
            "provision_match: name={!r} alias={!r} ica={!r} company={!r} replacing={!r}",
            project_name, alias, ica, company_type, is_replacing,
        )

        # ---- Step 1: project name -----------------------------------------
        name_loc = self.page.locator("input[data-testid='project-name']")
        await name_loc.wait_for(state="visible", timeout=15000)
        await name_loc.click()
        await asyncio.sleep(0.3)
        await name_loc.fill("")
        await name_loc.press_sequentially(project_name, delay=50)
        await name_loc.press("Tab")
        await asyncio.sleep(0.6)

        contact_email = await self._resolve_contact_email()

        # Wait for Proceed to be enabled before clicking (signals form valid).
        await self._wait_for_proceed_enabled(timeout_ms=15000)
        await asyncio.sleep(0.4)
        clicked = await self._click_proceed_btn()
        logger.info("MATCH step1 proceed clicked={}", clicked)
        try:
            await self.page.wait_for_selector(
                "input[name$='_accessToBeUsedBy']", timeout=15000
            )
        except Exception:
            await screenshot(self.page, "match_step1_no_service_form")
            raise

        # ---- Step 2: MATCH service details --------------------------------
        # Allow React time to mount the radio group.
        await asyncio.sleep(1.5)

        # 1. Company-type radio FIRST — selecting this reveals ICA, contact
        #    email, and the isReplacingClientId radios.
        company_ok = await self._click_radio_label(
            "_accessToBeUsedBy", company_type
        )
        await asyncio.sleep(1.2)

        # Wait for the conditional fields to mount.
        try:
            await self.page.wait_for_selector(
                "input[data-testid='acquirerica-text']", timeout=15000
            )
            await self.page.wait_for_selector(
                "input[data-testid='acquirercontactemail-text']", timeout=15000
            )
            await self.page.wait_for_selector(
                "input[name$='_isReplacingClientId'][value='No']", timeout=15000
            )
        except Exception:
            await screenshot(self.page, "match_conditional_fields_missing")
            raise
        await asyncio.sleep(0.6)

        # 2. ICA — real keystrokes
        ica_loc = self.page.locator("input[data-testid='acquirerica-text']")
        await ica_loc.scroll_into_view_if_needed()
        await ica_loc.click()
        await asyncio.sleep(0.3)
        await ica_loc.fill("")
        await ica_loc.press_sequentially(ica, delay=90)
        await ica_loc.press("Tab")
        await asyncio.sleep(0.6)
        ica_val = await ica_loc.input_value()
        ica_ok = ica_val == ica

        # 3. Contact email — real keystrokes (slow on the email field per user request)
        email_loc = self.page.locator("input[data-testid='acquirercontactemail-text']")
        await email_loc.scroll_into_view_if_needed()
        await email_loc.click()
        await asyncio.sleep(0.5)
        await email_loc.fill("")
        await email_loc.press_sequentially(contact_email, delay=90)
        await email_loc.press("Tab")
        await asyncio.sleep(0.8)
        email_val = await email_loc.input_value()
        email_ok = email_val == contact_email

        # 4. isReplacingClientId = No (real label click)
        replace_ok = await self._click_radio_label(
            "_isReplacingClientId", is_replacing
        )
        await asyncio.sleep(0.8)

        logger.info(
            "MATCH service-details set: company={} ica={} (got={!r}) email={} (got={!r}) replacing={}",
            company_ok, ica_ok, ica_val, email_ok, email_val, replace_ok,
        )
        if not (company_ok and ica_ok and email_ok and replace_ok):
            await screenshot(self.page, "match_service_details_set_failed")
            raise RuntimeError(
                f"MATCH service details set failed (company={company_ok}, "
                f"ica={ica_ok}, email={email_ok}, replacing={replace_ok})"
            )
        await screenshot(self.page, "match_service_details_filled")

        # Wait for Proceed to become enabled — signals the whole form is valid.
        await self._wait_for_proceed_enabled(timeout_ms=15000)
        await asyncio.sleep(0.6)

        clicked = await self._click_proceed_btn()
        logger.info("MATCH step2 proceed clicked={}", clicked)
        try:
            await self.page.wait_for_selector(
                "input[data-testid='key-alias-input']", timeout=15000
            )
        except Exception:
            await screenshot(self.page, "match_step2_no_key_form")
            raise
        # Let the key form fully mount before typing.
        await asyncio.sleep(1.2)

        # ---- Step 3: key alias + password ---------------------------------
        alias_loc = self.page.locator("input[data-testid='key-alias-input']")
        await alias_loc.click()
        await asyncio.sleep(0.3)
        await alias_loc.fill("")
        await alias_loc.press_sequentially(alias, delay=70)
        await alias_loc.press("Tab")
        await asyncio.sleep(0.5)

        pwd_loc = self.page.locator("input[data-testid='key-store-password-input']")
        await pwd_loc.click()
        await asyncio.sleep(0.3)
        await pwd_loc.fill("")
        await pwd_loc.press_sequentially(password, delay=70)
        await pwd_loc.press("Tab")
        await asyncio.sleep(0.8)

        await screenshot(self.page, "match_key_form_filled")
        # Wait for Proceed (now "Create project") to be enabled.
        await self._wait_for_proceed_enabled(timeout_ms=15000)
        await asyncio.sleep(0.6)
        clicked = await self._click_proceed_btn()
        logger.info("MATCH step3 'Create project' clicked={}", clicked)

        # ---- Step 4: download key file ------------------------------------
        # The portal shows a "Creating your project" loader with 3 stages
        # (generating keys → creating project → getting keys ready). This can
        # take well over a minute on busy days, so allow up to 4 minutes.
        try:
            await self.page.wait_for_selector(
                "button[data-testid='download-key-action-project-creation']",
                timeout=240000,
            )
        except Exception:
            await screenshot(self.page, "match_no_download_button")
            raise

        before_files = {p.name for p in dest_dir.glob("*") if p.is_file()}
        try:
            async with self.page.expect_download(timeout=120000) as dl_info:
                await self.page.locator(
                    "button[data-testid='download-key-action-project-creation']"
                ).click()
            download = await dl_info.value
            original = download.suggested_filename or f"{filename_hint}.zip"
            dest = dest_dir / original
            await save_download(download, dest)
            logger.info("MATCH key downloaded: {}", dest)
            downloaded = dest
        except Exception as err:
            logger.warning(
                "MATCH download event missed ({}) — polling filesystem fallback", err
            )
            downloaded = None
            for _ in range(30):
                await asyncio.sleep(1.0)
                new_files = [
                    p for p in dest_dir.glob("*")
                    if p.is_file()
                    and p.name not in before_files
                    and p.suffix.lower() in {".zip", ".p12", ".pem"}
                ]
                if new_files:
                    downloaded = max(new_files, key=lambda p: p.stat().st_mtime)
                    logger.info("MATCH key downloaded (fs fallback): {}", downloaded)
                    break
            if downloaded is None:
                raise

        # ---- Step 5: open project -----------------------------------------
        try:
            await self.page.wait_for_selector(
                "button[data-testid='proceed-button-create-new-project']", timeout=20000
            )
            await self.page.locator(
                "button[data-testid='proceed-button-create-new-project']"
            ).click()
        except Exception:
            logger.warning("'Open project' button not found after MATCH key download")

        for _ in range(40):
            if "/project-details/" in self.page.url:
                break
            await asyncio.sleep(0.5)
        if "/project-details/" not in self.page.url:
            await screenshot(self.page, "match_no_project_details_redirect")
            raise RuntimeError(
                f"MATCH provisioning did not land on /project-details/ — at {self.page.url}"
            )

        uuid = self.page.url.split("/project-details/")[-1].split("/")[0]
        logger.info("MATCH project provisioned uuid={} zip={}", uuid, downloaded)
        return downloaded, uuid
