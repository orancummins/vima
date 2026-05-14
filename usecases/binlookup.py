"""BIN Lookup use case — animated payment card visualiser.

Wraps the BIN Lookup API and shapes the response for the annotated,
animated payment card displayed in the Use Cases tab.
"""
from __future__ import annotations

from typing import Any, Dict, Tuple

MANIFEST: Dict[str, Any] = {
    "id": "binlookup",
    "name": "BIN Lookup",
    "description": (
        "The first digits of a card number unlock a wealth of intelligence. BIN Lookup "
        "instantly identifies the issuing bank, card network, product tier, funding source, "
        "issuing country, and over a dozen capability flags — enabling smarter checkout "
        "experiences, precision fraud detection, optimised payment routing, and personalised "
        "cardholder offers. This use case visualises every data point returned by the "
        "Mastercard BIN Lookup API."
    ),
    "apis": ["binlookup"],
    "render": "binlookup",
}

# ── acceptanceBrand → network ─────────────────────────────────────────────────
# Valid acceptanceBrand values per Mastercard docs:
# MCC=Mastercard® Credit, DMC=Debit Mastercard®, MSI=Maestro®, CIR=Cirrus®, PVL=Private Label
_ACCEPTANCE_BRAND_TO_NETWORK: Dict[str, str] = {
    "MCC": "Mastercard",
    "DMC": "Mastercard",
    "MSI": "Maestro",
    "CIR": "Cirrus",
    "PVL": "Other",
}

_ACCEPTANCE_BRAND_LABELS: Dict[str, str] = {
    "MCC": "Mastercard® Credit",
    "DMC": "Debit Mastercard®",
    "MSI": "Maestro®",
    "CIR": "Cirrus®",
    "PVL": "Private Label",
}

# ── Network gradient colours (dark → lighter, for CSS linear-gradient) ────────
_NETWORK_GRADIENTS: Dict[str, Tuple[str, str]] = {
    "Mastercard": ("#1a0808", "#8b0000"),
    "Maestro":    ("#1a0818", "#6b0060"),
    "Visa":       ("#0a1340", "#1A1F71"),
    "Amex":       ("#002060", "#0062cc"),
    "Discover":   ("#7a2000", "#cc4400"),
    "Other":      ("#1e293b", "#334155"),
    "Unknown":    ("#1e293b", "#334155"),
}

# ── ISO 3166-1 alpha-3 → alpha-2 (for flag emoji) ────────────────────────────
_ALPHA3_TO_ALPHA2: Dict[str, str] = {
    "USA": "US", "GBR": "GB", "DEU": "DE", "FRA": "FR", "JPN": "JP",
    "CAN": "CA", "AUS": "AU", "JOR": "JO", "ARG": "AR", "CHE": "CH",
    "SGP": "SG", "IND": "IN", "MEX": "MX", "BRA": "BR", "ZAF": "ZA",
    "ARE": "AE", "NLD": "NL", "ESP": "ES", "ITA": "IT", "RUS": "RU",
    "CHN": "CN", "KOR": "KR", "SWE": "SE", "NOR": "NO", "DNK": "DK",
    "POL": "PL", "BEL": "BE", "AUT": "AT", "PRT": "PT", "FIN": "FI",
    "IRL": "IE", "NZL": "NZ", "HKG": "HK", "TWN": "TW", "ISR": "IL",
    "NGA": "NG", "EGY": "EG", "MAR": "MA", "KEN": "KE", "THA": "TH",
    "IDN": "ID", "PHL": "PH", "VNM": "VN", "PAK": "PK", "BGD": "BD",
    "TUR": "TR", "SAU": "SA", "GHA": "GH", "CHL": "CL", "COL": "CO",
    "PER": "PE", "UKR": "UA", "ROU": "RO", "HUN": "HU", "CZE": "CZ",
    "SVK": "SK", "HRV": "HR", "BGR": "BG", "SRB": "RS", "GRC": "GR",
    "CYP": "CY", "MLT": "MT", "LUX": "LU", "EST": "EE", "LVA": "LV",
    "LTU": "LT", "SVN": "SI", "KAZ": "KZ", "UZB": "UZ", "AZE": "AZ",
    "GEO": "GE", "ARM": "AM", "MDA": "MD", "BLR": "BY", "MYS": "MY",
    "MMR": "MM", "KHM": "KH", "ETH": "ET", "TZA": "TZ", "UGA": "UG",
    "DZA": "DZ", "TUN": "TN", "LBY": "LY", "SDN": "SD", "CMR": "CM",
    "CIV": "CI", "SEN": "SN", "AGO": "AO", "ZMB": "ZM", "MOZ": "MZ",
    "ZWE": "ZW", "BWA": "BW", "NAM": "NA", "LSO": "LS", "SWZ": "SZ",
    "RWA": "RW", "MDG": "MG", "QAT": "QA", "KWT": "KW", "BHR": "BH",
    "OMN": "OM", "LBN": "LB", "IRQ": "IQ", "IRN": "IR", "SYR": "SY",
}


def do_action(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if action == "lookup":
        from apis.binlookup import api as bin_api
        result = bin_api.execute("lookup_bin", params)
        if not result.get("success"):
            return {"found": False, "error": result.get("error", "Lookup failed")}
        data = result.get("data") or {}
        items = data.get("items", [])
        if not items:
            return {
                "found": False,
                "bin": params.get("account_range", ""),
                "note": data.get("note", "No matching BIN found in the sandbox dataset."),
            }
        return {
            "found": True,
            "bin": params.get("account_range", ""),
            "card": _shape(items[0]),
        }
    return {"error": f"Unknown action: {action}"}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _flag(iso2: str) -> str:
    """Convert ISO 3166-1 alpha-2 code to flag emoji."""
    if len(iso2) != 2 or not iso2.isalpha():
        return ""
    base = 0x1F1E6
    return chr(base + ord(iso2[0].upper()) - ord("A")) + chr(base + ord(iso2[1].upper()) - ord("A"))


def _flag_from_alpha3(alpha3: str) -> str:
    """Convert ISO 3166-1 alpha-3 code to flag emoji via alpha-2 lookup."""
    alpha2 = _ALPHA3_TO_ALPHA2.get((alpha3 or "").strip().upper(), "")
    return _flag(alpha2) if alpha2 else ""
    return chr(base + ord(iso2[0].upper()) - ord("A")) + chr(base + ord(iso2[1].upper()) - ord("A"))


def _network_from_bin(bin_num: str) -> str:
    """Infer card network from BIN prefix as a fallback."""
    b = bin_num.lstrip("0") if bin_num else ""
    if not b:
        return "Unknown"
    if b[0] == "4":
        return "Visa"
    if b[:2] in ("34", "37"):
        return "Amex"
    if b[0] == "5" and len(b) >= 2 and b[1] in "12345":
        return "Mastercard"
    if len(b) >= 4:
        try:
            prefix4 = int(b[:4])
            if 2221 <= prefix4 <= 2720:
                return "Mastercard"
        except ValueError:
            pass
    if b[:4] == "6011" or b[:2] == "65":
        return "Discover"
    return "Unknown"


def _shape(item: Dict[str, Any]) -> Dict[str, Any]:
    # ── Network / acceptance brand ────────────────────────────────────────────
    acceptance_brand = (item.get("acceptanceBrand") or "").strip().upper()
    network = _ACCEPTANCE_BRAND_TO_NETWORK.get(acceptance_brand)
    if not network:
        network = _network_from_bin(str(item.get("binNum", "")))

    brand_label = _ACCEPTANCE_BRAND_LABELS.get(acceptance_brand, acceptance_brand or "Unknown")
    color1, color2 = _NETWORK_GRADIENTS.get(network, _NETWORK_GRADIENTS["Unknown"])

    # ── Product ───────────────────────────────────────────────────────────────
    product_code = (item.get("productCode") or "").strip().upper()
    product_desc = (item.get("productDescription") or "").strip().title()

    # ── Issuer ────────────────────────────────────────────────────────────────
    issuer_name = (item.get("customerName") or "Unknown Issuer").strip()
    affiliate   = (item.get("affiliate") or "").strip()
    display_name = affiliate or issuer_name

    # ── Country (nested object: {code, alpha3, name}) ─────────────────────────
    country_obj  = item.get("country") or {}
    country_a3   = (country_obj.get("alpha3") or "").strip().upper()
    country_name = (country_obj.get("name") or country_a3 or "Unknown").strip()

    # ── Funding & segment ─────────────────────────────────────────────────────
    funding_source = (item.get("fundingSource") or "").strip().upper()     # CREDIT/DEBIT/PREPAID/NONE
    consumer_type  = (item.get("consumerType")  or "CONSUMER").strip().upper()  # CONSUMER/CORPORATE/UNAVAILABLE
    consumer_label = {"CONSUMER": "Consumer", "CORPORATE": "Corporate", "UNAVAILABLE": "Unknown"}.get(
        consumer_type, consumer_type.title()
    )

    # Derive a readable product label (productDescription is authoritative when present)
    if product_desc:
        product_label = product_desc
    elif acceptance_brand == "MCC":
        product_label = "Credit"
    elif acceptance_brand == "DMC":
        product_label = "Debit"
    elif funding_source == "PREPAID":
        product_label = "Prepaid"
    elif funding_source == "DEBIT":
        product_label = "Debit"
    elif funding_source == "CREDIT":
        product_label = "Credit"
    else:
        product_label = "Card"

    # ── Capabilities ──────────────────────────────────────────────────────────
    local_use           = bool(item.get("localUse", False))
    auth_only           = bool(item.get("authorizationOnly", False))
    billing_currency    = (item.get("billingCurrencyDefault") or "").strip().upper()
    non_reloadable      = bool(item.get("nonReloadableIndicator", False))
    government_range    = bool(item.get("governmentRange", False))
    smart_data          = bool(item.get("smartDataEnabled", False))
    money_send_raw      = (item.get("moneySendIndicator") or "N").strip().upper()
    fast_fund_raw       = (item.get("fastFundIndicator")  or "N").strip().upper()
    dcc_indicator       = (item.get("cardholderCurrencyIndicator") or "").strip().upper()
    payment_acct_type   = (item.get("paymentAccountType") or "P").strip().upper()
    ica                 = (item.get("ica") or "").strip()

    return {
        # Card face
        "binNum":       str(item.get("binNum", "")),
        "binLength":    int(item.get("binLength", 6)),
        "issuerName":   issuer_name,
        "affiliate":    affiliate,
        "displayName":  display_name,
        # Network / brand
        "network":      network,
        "acceptanceBrand": acceptance_brand,
        "brandLabel":   brand_label,
        "color1":       color1,
        "color2":       color2,
        # Product
        "product":      product_label,
        "productCode":  product_code,
        # Country
        "countryAlpha3": country_a3,
        "countryName":   country_name,
        "flagEmoji":     _flag_from_alpha3(country_a3),
        # Funding / segment
        "fundingSource": funding_source,
        "consumerType":  consumer_type,
        "consumerLabel": consumer_label,
        # Capabilities
        "localUse":          local_use,
        "authorizationOnly": auth_only,
        "billingCurrency":   billing_currency,
        "nonReloadable":     non_reloadable,
        "governmentRange":   government_range,
        "smartData":         smart_data,
        "moneySend":         money_send_raw == "Y",
        "fastFund":          fast_fund_raw in ("Y", "D"),
        "fastFundDomesticOnly": fast_fund_raw == "D",
        "dccEnabled":        dcc_indicator == "D",
        "isToken":           payment_acct_type == "T",
        "ica":               ica,
        # Raw API response
        "raw": item,
    }
