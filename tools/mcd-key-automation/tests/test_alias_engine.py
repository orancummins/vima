from app.alias_engine import make_alias, make_filename


def test_alias_sandbox():
    a = make_alias(organization="Mastercard", environment="sandbox", project="BIN Lookup", api="binlookup")
    assert a == "mastercard-sbx-bin-lookup-binlookup-signing-v1"


def test_alias_production():
    a = make_alias(organization="mastercard", environment="production", project="ofin", api="ofin", purpose="encryption")
    assert a == "mastercard-prd-ofin-ofin-encryption-v1"


def test_filename():
    assert make_filename("mastercard-sbx-ofin-ofin-signing-v1", ".P12") == "mastercard-sbx-ofin-ofin-signing-v1.p12"
