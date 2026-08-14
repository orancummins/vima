"""AU (CDR) Open Finance commands."""
from __future__ import annotations

from .common import emit, resolve_arg

REGION = "au"


def _auth_token(args, ctx) -> int:
    return emit(ctx.client.au.auth_token(), ctx, REGION)


def _customers_add_testing(args, ctx) -> int:
    return emit(
        ctx.client.au.add_testing_customer(
            args.username, first_name=args.first_name, last_name=args.last_name,
            email=args.email, phone=args.phone),
        ctx, REGION)


def _customers_list(args, ctx) -> int:
    return emit(ctx.client.au.list_customers(search=args.search or "", limit=args.limit),
                ctx, REGION)


def _institutions_list(args, ctx) -> int:
    return emit(
        ctx.client.au.list_institutions(search=args.search or "", limit=args.limit,
                                         supported_countries=args.supported_countries),
        ctx, REGION)


def _connect_generate(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    res = ctx.client.au.generate_connect_url(cid, webhook_url=args.webhook_url or "")
    return emit(res, ctx, REGION, open_link=args.open)


def _consents_list(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    return emit(ctx.client.au.list_consents(cid, status=args.status), ctx, REGION)


def _accounts_list(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    rcpt = resolve_arg(args, "consent_receipt_id", ctx, REGION, "consent_receipt_id",
                       label="consent-receipt-id")
    return emit(ctx.client.au.list_accounts(cid, rcpt), ctx, REGION)


def add_parser(subparsers) -> None:
    au = subparsers.add_parser("au", help="Open Finance Australia (CDR) commands.")
    sub = au.add_subparsers(dest="au_cmd", required=True)

    auth = sub.add_parser("auth", help="Authentication.")
    auth_sub = auth.add_subparsers(dest="auth_cmd", required=True)
    auth_sub.add_parser("token", help="Create an access token (smoke test).").set_defaults(func=_auth_token)

    cust = sub.add_parser("customers", help="Customer management.")
    cust_sub = cust.add_subparsers(dest="customers_cmd", required=True)
    c_add = cust_sub.add_parser("add-testing", help="Enrol a sandbox testing customer.")
    c_add.add_argument("--username", required=True)
    c_add.add_argument("--first-name", default="Alex", dest="first_name")
    c_add.add_argument("--last-name", default="Smith", dest="last_name")
    c_add.add_argument("--email", default="alex.smith@example.com")
    c_add.add_argument("--phone", default="+61400000000")
    c_add.set_defaults(func=_customers_add_testing)
    c_list = cust_sub.add_parser("list", help="List/search customers.")
    c_list.add_argument("--search", default="")
    c_list.add_argument("--limit", type=int, default=25)
    c_list.set_defaults(func=_customers_list)

    inst = sub.add_parser("institutions", help="Institutions.")
    inst_sub = inst.add_subparsers(dest="institutions_cmd", required=True)
    i_list = inst_sub.add_parser("list", help="List/search institutions.")
    i_list.add_argument("--search", default="")
    i_list.add_argument("--limit", type=int, default=25)
    i_list.add_argument("--supported-countries", default="au", dest="supported_countries")
    i_list.set_defaults(func=_institutions_list)

    conn = sub.add_parser("connect", help="CDR Connect.")
    conn_sub = conn.add_subparsers(dest="connect_cmd", required=True)
    c_gen = conn_sub.add_parser("generate", help="Generate a CDR Connect URL.")
    c_gen.add_argument("--customer-id")
    c_gen.add_argument("--webhook-url", dest="webhook_url")
    c_gen.add_argument("--open", action="store_true", help="Open the URL in a browser.")
    c_gen.set_defaults(func=_connect_generate)

    cons = sub.add_parser("consents", help="CDR data-sharing consents.")
    cons_sub = cons.add_subparsers(dest="consents_cmd", required=True)
    co_list = cons_sub.add_parser("list", help="List consents (captures consent-receipt-id).")
    co_list.add_argument("--customer-id")
    co_list.add_argument("--status", default="ACTIVE")
    co_list.set_defaults(func=_consents_list)

    acc = sub.add_parser("accounts", help="Accounts.")
    acc_sub = acc.add_subparsers(dest="accounts_cmd", required=True)
    a_list = acc_sub.add_parser("list", help="List accounts (needs a consent-receipt-id).")
    a_list.add_argument("--customer-id")
    a_list.add_argument("--consent-receipt-id", dest="consent_receipt_id")
    a_list.set_defaults(func=_accounts_list)
