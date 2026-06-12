"""US (Finicity) Open Finance commands."""
from __future__ import annotations

from .common import emit, parse_account_ids, resolve_arg

REGION = "us"


# -- handlers ---------------------------------------------------------------
def _auth_token(args, ctx) -> int:
    return emit(ctx.client.us.auth_token(), ctx, REGION)


def _customers_add_testing(args, ctx) -> int:
    return emit(ctx.client.us.add_testing_customer(args.username), ctx, REGION)


def _customers_list(args, ctx) -> int:
    return emit(ctx.client.us.list_customers(search=args.search or "", limit=args.limit),
                ctx, REGION)


def _customers_get(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    return emit(ctx.client.us.get_customer(cid), ctx, REGION)


def _customers_use(args, ctx) -> int:
    """Set the active customer id in local state (no API call)."""
    ctx.state.set(REGION, "customer_id", args.customer_id)
    ctx.state.save()
    ctx.printer.info(f"active US customer set to {args.customer_id}")
    return 0


def _connect_generate(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    res = ctx.client.us.generate_connect_url(cid, experience=args.experience)
    return emit(res, ctx, REGION, open_link=args.open)


def _accounts_list(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    return emit(ctx.client.us.list_accounts(cid), ctx, REGION)


def _accounts_refresh(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    return emit(ctx.client.us.refresh_accounts(cid), ctx, REGION)


def _balance(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    aid = resolve_arg(args, "account_id", ctx, REGION, "account_id")
    return emit(ctx.client.us.get_balance(cid, aid), ctx, REGION)


def _transactions_list(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    return emit(
        ctx.client.us.list_transactions(cid, from_date=args.from_date,
                                         to_date=args.to_date, limit=args.limit),
        ctx, REGION)


def _reports_voa(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    return emit(ctx.client.us.generate_voa(cid, account_ids=parse_account_ids(args.account_ids)),
                ctx, REGION)


def _reports_voi(args, ctx) -> int:
    cid = resolve_arg(args, "customer_id", ctx, REGION, "customer_id")
    return emit(ctx.client.us.generate_voi(cid, account_ids=parse_account_ids(args.account_ids)),
                ctx, REGION)


# -- parser -----------------------------------------------------------------
def add_parser(subparsers) -> None:
    us = subparsers.add_parser("us", help="Open Finance US (Finicity) commands.")
    sub = us.add_subparsers(dest="us_cmd", required=True)

    # auth token
    auth = sub.add_parser("auth", help="Authentication.")
    auth_sub = auth.add_subparsers(dest="auth_cmd", required=True)
    auth_sub.add_parser("token", help="Create an access token (smoke test).").set_defaults(func=_auth_token)

    # customers
    cust = sub.add_parser("customers", help="Customer management.")
    cust_sub = cust.add_subparsers(dest="customers_cmd", required=True)
    c_add = cust_sub.add_parser("add-testing", help="Enrol a sandbox testing customer.")
    c_add.add_argument("--username", required=True)
    c_add.set_defaults(func=_customers_add_testing)
    c_list = cust_sub.add_parser("list", help="List/search customers.")
    c_list.add_argument("--search", default="")
    c_list.add_argument("--limit", type=int, default=25)
    c_list.set_defaults(func=_customers_list)
    c_get = cust_sub.add_parser("get", help="Get a customer by id (or active).")
    c_get.add_argument("--customer-id")
    c_get.set_defaults(func=_customers_get)
    c_use = cust_sub.add_parser("use", help="Set the active customer id in local state.")
    c_use.add_argument("customer_id")
    c_use.set_defaults(func=_customers_use)

    # connect
    conn = sub.add_parser("connect", help="Data Connect.")
    conn_sub = conn.add_subparsers(dest="connect_cmd", required=True)
    c_gen = conn_sub.add_parser("generate", help="Generate a Data Connect URL.")
    c_gen.add_argument("--customer-id")
    c_gen.add_argument("--experience", help="Optional Connect experience id.")
    c_gen.add_argument("--open", action="store_true", help="Open the URL in a browser.")
    c_gen.set_defaults(func=_connect_generate)

    # accounts
    acc = sub.add_parser("accounts", help="Accounts.")
    acc_sub = acc.add_subparsers(dest="accounts_cmd", required=True)
    a_list = acc_sub.add_parser("list", help="List a customer's accounts.")
    a_list.add_argument("--customer-id")
    a_list.set_defaults(func=_accounts_list)
    a_ref = acc_sub.add_parser("refresh", help="Refresh a customer's accounts.")
    a_ref.add_argument("--customer-id")
    a_ref.set_defaults(func=_accounts_refresh)

    # balance
    bal = sub.add_parser("balance", help="Live available balance for an account.")
    bal.add_argument("--customer-id")
    bal.add_argument("--account-id")
    bal.set_defaults(func=_balance)

    # transactions
    txn = sub.add_parser("transactions", help="Transactions.")
    txn_sub = txn.add_subparsers(dest="transactions_cmd", required=True)
    t_list = txn_sub.add_parser("list", help="List customer transactions in a date range.")
    t_list.add_argument("--customer-id")
    t_list.add_argument("--from-date", type=int, required=True, dest="from_date",
                        help="Epoch seconds (inclusive).")
    t_list.add_argument("--to-date", type=int, required=True, dest="to_date",
                        help="Epoch seconds (inclusive).")
    t_list.add_argument("--limit", type=int, default=1000)
    t_list.set_defaults(func=_transactions_list)

    # reports
    rep = sub.add_parser("reports", help="Decisioning reports.")
    rep_sub = rep.add_subparsers(dest="reports_cmd", required=True)
    r_voa = rep_sub.add_parser("voa", help="Generate a Verification of Assets report.")
    r_voa.add_argument("--customer-id")
    r_voa.add_argument("--account-ids", help="Comma-separated account ids (optional).")
    r_voa.set_defaults(func=_reports_voa)
    r_voi = rep_sub.add_parser("voi", help="Generate a Verification of Income report.")
    r_voi.add_argument("--customer-id")
    r_voi.add_argument("--account-ids", help="Comma-separated account ids (optional).")
    r_voi.set_defaults(func=_reports_voi)
