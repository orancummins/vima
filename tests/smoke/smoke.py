"""tests/smoke/smoke.py — basic connectivity and home-screen render checks.

Validates that:
  - The home page (GET /app) returns 200 without a server error page
  - The HTML contains all top-level navigation panels
  - The API manifest endpoint (GET /explorer/apis) returns valid JSON
  - The API list is non-empty and contains a known API id
  - The platform tab's page and links load, and every link resolves
  - The platform's searchable catalogue reaches the page

Independently runnable::

    python tests/smoke/smoke.py --base-url http://localhost:9021
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from tests.lib.utils import (
    TestRunner, Summary,
    get, assert_status, assert_json, assert_field, assert_no_server_error,
)


def run(base_url: str = "http://127.0.0.1:9021") -> TestRunner:
    runner = TestRunner("Smoke — Home / APIs / Use Cases")

    # ── GET /app ───────────────────────────────────────────────
    runner.run("GET /app returns 200", lambda: assert_status(get(f"{base_url}/app"), 200))

    def _home_no_error():
        resp = assert_status(get(f"{base_url}/app"), 200)
        assert_no_server_error(resp.text, f"{base_url}/app")

    runner.run("GET /app has no server error", _home_no_error)

    def _home_nav_panels():
        resp = assert_status(get(f"{base_url}/app"), 200)
        html = resp.text
        for marker in ("panel-home", "panel-os", "panel-customers", "panel-apis", "panel-bundles", "panel-usecases"):
            assert marker in html, (
                f"Navigation panel marker {marker!r} not found in /app HTML. "
                f"The page may not have loaded correctly."
            )

    runner.run("GET /app contains all navigation panels", _home_nav_panels)

    # ── GET /explorer/apis ──────────────────────────────────────
    def _apis_200():
        assert_status(get(f"{base_url}/explorer/apis"), 200)

    runner.run("GET /explorer/apis returns 200", _apis_200)

    def _apis_json_list():
        resp = assert_status(get(f"{base_url}/explorer/apis"), 200)
        data = assert_json(resp)
        # Response may be a list or {"apis": [...]}
        items = data if isinstance(data, list) else data.get("apis", data)
        assert isinstance(items, list) and len(items) > 0, (
            f"/explorer/apis returned an empty or non-list response: {data}"
        )

    runner.run("GET /explorer/apis returns a non-empty list", _apis_json_list)

    def _apis_has_bin_lookup():
        resp = assert_status(get(f"{base_url}/explorer/apis"), 200)
        data = assert_json(resp)
        items = data if isinstance(data, list) else data.get("apis", data)
        ids = [a.get("id") for a in items]
        assert "bin_lookup" in ids, (
            f"'bin_lookup' not found in API list. Available ids: {ids}"
        )

    runner.run("GET /explorer/apis includes bin_lookup", _apis_has_bin_lookup)

    # ── Use Cases page marker (served from same /app SPA) ──────
    def _uc_panel():
        resp = assert_status(get(f"{base_url}/app"), 200)
        assert "panel-usecases" in resp.text, (
            "Use Cases panel marker not found in /app HTML."
        )

    runner.run("Use Cases panel marker present in /app", _uc_panel)

    # ── Platform tab (mcos/) ──────────────────────────────────────
    def _mcos_page():
        resp = assert_status(get(f"{base_url}/mcos/index.html"), 200)
        assert_no_server_error(resp.text, f"{base_url}/mcos/index.html")
        for marker in ('id="pic"', "mcos-theme.css", "mcos-bridge.js"):
            assert marker in resp.text, f"{marker!r} not found in /mcos/index.html"

    runner.run("GET /mcos/index.html serves the themed picture", _mcos_page)

    def _mcos_assets():
        for name in ("mcos-theme.css", "mcos-bridge.js"):
            assert_status(get(f"{base_url}/mcos/{name}"), 200)

    runner.run("GET /mcos/ theme and bridge assets return 200", _mcos_assets)

    def _mcos_links():
        data = assert_json(assert_status(get(f"{base_url}/mcos/links.json"), 200))
        assert not data.get("warnings"), f"Platform links no longer resolve: {data['warnings']}"
        products = data.get("products", {})
        assert "binlookup" in products, f"BIN Lookup has no product in the picture: {sorted(products)}"
        assert data.get("targets", {}).get("api", {}).get("bin_lookup") == "p-binlookup", (
            "bin_lookup should link to p-binlookup in the picture"
        )

    runner.run("GET /mcos/links.json resolves every link", _mcos_links)

    def _mcos_search_catalog():
        resp = assert_status(get(f"{base_url}/app"), 200)
        m = re.search(r"window\.__MCOS_SEARCH__ = (\[.*?\]);", resp.text)
        assert m, "window.__MCOS_SEARCH__ not found in /app HTML."
        entries = json.loads(m.group(1))
        kinds = {e["kind"] for e in entries}
        assert kinds >= {"layer", "area", "product", "outcome"}, (
            f"Platform search catalogue is missing kinds: {sorted(kinds)}"
        )
        by_id = {e["id"]: e for e in entries}
        assert by_id.get("binlookup", {}).get("target") == "p-binlookup", (
            "BIN Lookup's product should be searchable and open p-binlookup"
        )

    runner.run("/app carries the platform search catalogue", _mcos_search_catalog)

    # ── Customers tab (customers/) ────────────────────────────────
    def _customers_listed():
        resp = assert_status(get(f"{base_url}/app"), 200)
        m = re.search(r"window\.__CUSTOMERS__ = (\[.*?\]);", resp.text)
        assert m, "window.__CUSTOMERS__ not found in /app HTML."
        ids = {c["id"] for c in json.loads(m.group(1))}
        expected = {"snb", "citi", "citizens", "stripe", "boi", "itau", "capitalone", "jpmc", "fiserv",
                    "globalpayments", "santander", "barclays", "natwest", "synchrony", "hsbc", "bmo", "nubank",
                    "nexi", "worldline", "bofa", "bradesco", "unicredit", "adyen", "paypal", "bancodobrasil", "ing",
                    "lloyds", "bnpparibas", "wellsfargo", "revolut", "deutschebank", "checkout", "dbs", "amazon"}
        assert expected <= ids, f"Customers missing from the Customers tab: {sorted(expected - ids)}"
        assert 'data-customer-open="snb"' in resp.text, "No card opens Saudi National Bank."
        no_logo = sorted(c["id"] for c in json.loads(m.group(1)) if not c.get("logos"))
        assert not no_logo, f"Customers without a logo on their card: {no_logo}"
        logo = json.loads(m.group(1))[0]["logos"][0]["url"]
        assert_status(get(f"{base_url}{logo}"), 200)

    runner.run("/app lists the customers", _customers_listed)

    def _customer_page():
        resp = assert_status(get(f"{base_url}/customers/snb/"), 200)
        assert_no_server_error(resp.text, f"{base_url}/customers/snb/")
        for marker in ('id="pic"', "mcos-theme.css", "customers/snb/studio-theme.css", "mcos-bridge.js",
                       'SNB <span class="os">Platform</span>'):
            assert marker in resp.text, f"{marker!r} not found in /customers/snb/"

    runner.run("GET /customers/snb/ serves the themed picture", _customer_page)

    def _customer_standalone():
        resp = assert_status(get(f"{base_url}/customers/snb/SNB_Operating_System.html"), 200)
        assert "mcos-bridge.js" not in resp.text, "The standalone page should be served untouched."
        assert 'SNB <span class="os">Operating System</span>' in resp.text
        assert_status(get(f"{base_url}/customers/snb/__init__.py"), 404)

    runner.run("GET /customers/snb/ standalone page is served as-is, nothing else is", _customer_standalone)

    def _customer_links():
        data = assert_json(assert_status(get(f"{base_url}/customers/snb/links.json"), 200))
        assert not data.get("warnings"), f"SNB's Studio links no longer resolve: {data['warnings']}"
        products = data.get("products", {})
        assert "openbanking" in products, f"SNB open banking has nothing live in Studio: {sorted(products)}"
        assert any(a["id"] == "open_finance" for a in products["openbanking"]["apis"])

    runner.run("GET /customers/snb/links.json resolves every link", _customer_links)

    def _citi():
        resp = assert_status(get(f"{base_url}/customers/citi/"), 200)
        assert_no_server_error(resp.text, f"{base_url}/customers/citi/")
        assert 'Citi <span class="os">Platform</span>' in resp.text and "customers/citi/studio-theme.css" in resp.text
        assert_status(get(f"{base_url}/customers/citi/Citi_Platform.html"), 200)
        assert_status(get(f"{base_url}/customers/citi/build_page.py"), 404)
        data = assert_json(assert_status(get(f"{base_url}/customers/citi/links.json"), 200))
        assert not data.get("warnings"), f"Citi's Studio links no longer resolve: {data['warnings']}"
        assert "service" in data.get("products", {}), "Citi's disputes product should link to Consumer Clarity"

    runner.run("GET /customers/citi/ serves the page, its links and nothing else", _citi)

    def _citizens():
        resp = assert_status(get(f"{base_url}/customers/citizens/"), 200)
        assert_no_server_error(resp.text, f"{base_url}/customers/citizens/")
        assert 'Citizens <span class="os">Platform</span>' in resp.text
        assert_status(get(f"{base_url}/customers/citizens/Citizens_Platform.html"), 200)
        assert_status(get(f"{base_url}/customers/citizens/page_data.py"), 404)
        data = assert_json(assert_status(get(f"{base_url}/customers/citizens/links.json"), 200))
        assert not data.get("warnings"), f"Citizens' Studio links no longer resolve: {data['warnings']}"
        assert "switchpay" in data.get("products", {}), "Switch Payments should link to Studio's billing APIs"

    runner.run("GET /customers/citizens/ serves the page, its links and nothing else", _citizens)

    def _built_customers():
        for cid, page, product in (("stripe", "Stripe_Platform.html", "authboost"),
                                   ("boi", "Bank_of_Ireland_Platform.html", "creditcards"),
                                   ("itau", "Itau_Platform.html", "rede"),
                                   ("capitalone", "Capital_One_Platform.html", "spark"),
                                   ("jpmc", "JPMorgan_Chase_Platform.html", "applecard"),
                                   ("fiserv", "Fiserv_Platform.html", "merchantcloud"),
                                   ("globalpayments", "Global_Payments_Platform.html", "wpenterprise"),
                                   ("santander", "Santander_Platform.html", "getnet"),
                                   ("barclays", "Barclays_Platform.html", "bcpayments"),
                                   ("natwest", "NatWest_Group_Platform.html", "mcdebit"),
                                   ("synchrony", "Synchrony_Platform.html", "mcdual"),
                                   ("hsbc", "HSBC_Platform.html", "ukcredit"),
                                   ("bmo", "BMO_Platform.html", "bluecard"),
                                   ("nubank", "Nubank_Platform.html", "ccbr"),
                                   ("nexi", "Nexi_Platform.html", "acquiring"),
                                   ("worldline", "Worldline_Platform.html", "acquiring"),
                                   ("bofa", "Bank_of_America_Platform.html", "bizadvantage"),
                                   ("bradesco", "Bradesco_Platform.html", "mcblack"),
                                   ("unicredit", "UniCredit_Platform.html", "mcdeal"),
                                   ("adyen", "Adyen_Platform.html", "acquiring"),
                                   ("paypal", "PayPal_Platform.html", "ppdebit"),
                                   ("bancodobrasil", "Banco_do_Brasil_Platform.html", "ourocard"),
                                   ("ing", "ING_Platform.html", "bedebit"),
                                   ("lloyds", "Lloyds_Banking_Group_Platform.html", "curve"),
                                   ("bnpparibas", "BNP_Paribas_Platform.html", "nickelcard"),
                                   ("wellsfargo", "Wells_Fargo_Platform.html", "choice"),
                                   ("revolut", "Revolut_Platform.html", "cards"),
                                   ("deutschebank", "Deutsche_Bank_Platform.html", "milesmore"),
                                   ("checkout", "Checkout_com_Platform.html", "wholesale"),
                                   ("dbs", "DBS_Platform.html", "womans"),
                                   ("amazon", "Amazon_Platform.html", "amazonpay")):
            resp = assert_status(get(f"{base_url}/customers/{cid}/"), 200)
            assert_no_server_error(resp.text, f"{base_url}/customers/{cid}/")
            assert f"customers/{cid}/studio-theme.css" in resp.text
            assert '<div class="brand">' in resp.text, f"{cid}: no logo over the page's heading"
            assert_status(get(f"{base_url}/customers/{cid}/{page}"), 200)
            data = assert_json(assert_status(get(f"{base_url}/customers/{cid}/links.json"), 200))
            assert not data.get("warnings"), f"{cid}'s Studio links no longer resolve: {data['warnings']}"
            assert product in data.get("products", {}), f"{cid}: {product} should link to Studio"

    runner.run("GET /customers/<built customers>/ serve their pages and links", _built_customers)

    return runner


# ── Standalone entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vima smoke tests")
    parser.add_argument("--base-url", default="http://127.0.0.1:9021")
    args = parser.parse_args()

    runner = run(args.base_url)
    summary = Summary()
    summary.add(runner)
    runner.print_summary()
    summary.print_and_exit()
