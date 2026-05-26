"""Create-project form page object."""
from __future__ import annotations

import asyncio
from pathlib import Path

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
                   region: str | None = None, api_selection: str | None = None) -> None:
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

        # Sub-API selection (e.g. "Priceless Specials" on the priceless create-project page).
        if api_selection:
            logger.info("Selecting sub-API: {!r}", api_selection)
            # The portal renders a list of APIs as clickable cards or checkboxes.
            # Try label text first, then a broader :has-text match.
            sel = (
                f"label:has-text('{api_selection}'), "
                f"[role='checkbox']:has-text('{api_selection}'), "
                f"li:has-text('{api_selection}'), "
                f"div[class*='card']:has-text('{api_selection}'), "
                f"span:has-text('{api_selection}')"
            )
            loc = self.page.locator(sel).first
            if await loc.count() > 0:
                await loc.click()
                logger.info("Clicked sub-API: {!r}", api_selection)
            else:
                logger.warning("Sub-API {!r} not found on page — skipping selection", api_selection)

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
            # Step 2: wizard advanced to Project credentials (key alias + password)
            if await self.page.locator("[data-testid='key-alias-input']").count() > 0:
                logger.info("Wizard advanced to Step 2 (Project credentials) — {}", url)
                return "step2_credentials"

            # Open Finance "Service details" intermediate step — just click Proceed to continue.
            if not _service_details_clicked:
                service_heading = await self.page.locator(
                    "h1:has-text('Service details'), h2:has-text('Service details'), "
                    "[class*='heading']:has-text('Service details'), "
                    "div:has-text('Open Finance Sandbox API Credentials')"
                ).count()
                if service_heading > 0:
                    logger.info("Open Finance 'Service details' step detected — clicking Proceed")
                    await screenshot(self.page, "ofin_service_details")
                    # Scroll to bottom to expose the button on this step.
                    await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    await asyncio.sleep(0.5)
                    # JS-click the form's action button (not Exit/navigation buttons).
                    clicked = await self.page.evaluate("""
                        () => {
                            const SKIP = ['exit', 'back', 'cancel'];
                            const btns = Array.from(document.querySelectorAll('button'))
                                .filter(b => {
                                    const text = b.textContent.trim().toLowerCase();
                                    if (SKIP.some(s => text === s)) return false;
                                    const style = getComputedStyle(b);
                                    return style.display !== 'none' &&
                                           style.visibility !== 'hidden' &&
                                           !b.disabled &&
                                           b.getAttribute('aria-disabled') !== 'true' &&
                                           b.offsetParent !== null;
                                });
                            if (btns.length === 0) return null;
                            const btn = btns[0];
                            const text = btn.textContent.trim();
                            btn.click();
                            return text;
                        }
                    """)
                    logger.info("Service details — JS-clicked button: {!r}", clicked)
                    _service_details_clicked = True
                    await asyncio.sleep(1.0)
                    continue

            await asyncio.sleep(poll_interval)
            elapsed += poll_interval
        raise TimeoutError(f"No confirmation or project page appeared within {timeout_ms}ms — skipping")

    async def fill_step2_credentials(self, *, alias: str, password: str) -> None:
        """Fill ALL alias+password pairs in the Step 2 wizard.

        Some APIs (e.g. clarity, txnotify) have two key sections: a signing key
        AND an encryption key, each with their own alias + password fields.
        The encryption section may be collapsed; we use JS to set values and fire
        React synthetic events without needing visibility.
        """
        logger.info("Filling Step 2 credentials: alias={!r}", alias)

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
    ) -> str:
        """After Step 2 click, handle multi-step wizards and wait for final download/confirmation.

        Some APIs (e.g. clarity, txnotify) have a Step 3 "Additional credentials" that must be
        filled and submitted before the key download appears. This method detects Step 3 and
        handles it automatically.

        Returns: 'download' | 'open_project' | 'project_page'
        """
        deadline = timeout_ms / 1000
        poll_interval = 0.5
        elapsed = 0.0
        _step3_clicked = False  # guard against re-clicking step 3 button in rapid succession

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

            # Step 3 detection: check if "Additional credentials" step is visible.
            step3_heading = await self.page.locator("text=Additional credentials").count()
            if step3_heading > 0 and not _step3_clicked:
                logger.info("Step 3 (Additional credentials) detected")
                await screenshot(self.page, "step3_detected")
                
                # Check if this is a "no action needed" informational step (e.g., auto-generated encryption key).
                no_action_text = await self.page.locator("text=There are no actions needed").count()
                
                if no_action_text > 0:
                    # No inputs to fill — just click "Create project" or "Skip this step".
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
        logger.info("Clicking 'Download key file'")
        async with self.page.expect_download() as dl_info:
            await self.page.locator(ProjectCreatedSelectors.download_key_button).click()
        download = await dl_info.value
        original = download.suggested_filename or f"{filename_hint}.p12"
        dest = dest_dir / original
        await save_download(download, dest)
        logger.info("Downloaded key file: {}", dest)
        return dest

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

        # Pick the first option that contains "United States" or "Open Finance",
        # or just the first option if nothing specific matches.
        preferred = [o for o in options_text if "united states" in o.lower() or "open finance" in o.lower()]
        pick = preferred[0] if preferred else (options_text[0] if options_text else None)
        logger.info("Selecting API option: {!r}", pick)

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

            # Type to filter then click.
            await region_inp.press_sequentially("United States", delay=50)
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
