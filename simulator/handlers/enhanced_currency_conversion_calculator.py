"""Simulator handler for Enhanced Currency Conversion Calculator (ECCC)."""
from flask import jsonify, request

from simulator.datastore import store

API = "enhanced_currency_conversion_calculator"


def register(bp):
    @bp.route("/enhanced_currency_conversion_calculator/summary-rates", methods=["GET"])
    def summary_rates():
        store.lazy_load(API)
        fx_date = request.args.get("fxDate") or "0000-00-00"
        trans = (request.args.get("transCurr") or "").upper()
        bill  = (request.args.get("crdhldBillCurr") or "").upper()
        try:
            trans_amt = float(request.args.get("transAmt") or "0")
        except ValueError:
            trans_amt = 0.0
        try:
            bank_fee = float(request.args.get("bankFee") or "0")
        except ValueError:
            bank_fee = 0.0
        try:
            bank_fee_pct = float(request.args.get("bankFeePct") or "0")
        except ValueError:
            bank_fee_pct = 0.0

        # Look up the pair in the fixture; fall back to a synthetic rate.
        rows = store.search(API, "summary_rates", [
            {"key": "transCurr", "value": trans},
            {"key": "crdhldBillCurr", "value": bill},
        ])
        if rows:
            base = dict(rows[0])
        else:
            base = {
                "transCurr": trans or "USD",
                "crdhldBillCurr": bill or "EUR",
                "conversionRate": 0.92,
                "ecbReferenceRate": 0.91,
                "ecbReferenceRateDate": "2026-05-27",
            }

        conv_rate = float(base.get("conversionRate", 0.92))
        ecb_rate  = float(base.get("ecbReferenceRate", 0.91))
        excl = round(trans_amt * conv_rate, 4)
        incl = round(excl + bank_fee + (excl * bank_fee_pct / 100.0), 4)
        eff_rate = round(incl / trans_amt, 6) if trans_amt else conv_rate
        pct_excl = round((conv_rate - ecb_rate) / ecb_rate * 100, 4) if ecb_rate else 0.0
        pct_incl = round((eff_rate - ecb_rate) / ecb_rate * 100, 4) if ecb_rate else 0.0

        return jsonify({
            "fxDate": fx_date,
            "transCurr": base.get("transCurr"),
            "crdhldBillCurr": base.get("crdhldBillCurr"),
            "transAmt": trans_amt,
            "conversionRate": conv_rate,
            "mastercardConvRateInclPctFee": eff_rate,
            "effectiveConversionRate": eff_rate,
            "crdhldBillAmtExclAllFees": excl,
            "crdhldBillAmtInclAllFees": incl,
            "ecbReferenceRate": ecb_rate,
            "ecbReferenceRateDate": base.get("ecbReferenceRateDate"),
            "pctDifferenceMastercardExclAllFeesAndEcb": pct_excl,
            "pctDifferenceMastercardInclAllFeesAndEcb": pct_incl,
        })

    @bp.route("/enhanced_currency_conversion_calculator/rate-statuses", methods=["GET"])
    def rate_statuses():
        store.lazy_load(API)
        fx_date = request.args.get("fxDate") or "0000-00-00"
        return jsonify({
            "fxDate": fx_date,
            "mastercardRateIssued": "Y",
            "ecbRateIssued": "Y",
        })

    @bp.route("/enhanced_currency_conversion_calculator/mc-currencies", methods=["GET"])
    def mc_currencies():
        store.lazy_load(API)
        rows = store.list(API, "mc_currencies")
        return jsonify({"currencies": rows})

    @bp.route("/enhanced_currency_conversion_calculator/ecb-currencies", methods=["GET"])
    def ecb_currencies():
        store.lazy_load(API)
        rows = store.list(API, "ecb_currencies")
        return jsonify({"currencies": rows})
