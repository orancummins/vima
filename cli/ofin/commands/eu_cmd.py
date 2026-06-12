"""EU (Aiia) Open Finance commands."""
from __future__ import annotations

from ..errors import UsageError
from .common import emit, parse_account_ids, resolve_arg

REGION = "eu"


def _auth_token(args, ctx) -> int:
    return emit(ctx.client.eu.auth_token(), ctx, REGION)


def _providers_list(args, ctx) -> int:
    return emit(ctx.client.eu.list_providers(country=args.country or "", limit=args.limit),
                ctx, REGION)


def _consent_create(args, ctx) -> int:
    # use-case-configuration-id falls back to the configured OPEN_FINANCE_EU_USE_CASE_ID.
    ucid = args.use_case_id or ctx.config.eu.use_case_id
    if not ucid:
        raise UsageError(
            "--use-case-id is required (no OPEN_FINANCE_EU_USE_CASE_ID configured)."
        )
    # Reuse a previously saved end_user_id if present so flow create matches.
    existing_eu_id = ctx.state.get(REGION, "end_user_id")
    res = ctx.client.eu.create_consent(
        use_case_configuration_id=ucid,
        end_user_email=args.email,
        end_user_id=args.end_user_id or existing_eu_id,
    )
    return emit(res, ctx, REGION)


def _consent_get(args, ctx) -> int:
    cid = resolve_arg(args, "consent_id", ctx, REGION, "consent_id")
    return emit(ctx.client.eu.get_consent(cid), ctx, REGION)


def _consent_revoke(args, ctx) -> int:
    if not args.yes:
        raise UsageError("Refusing to revoke without --yes (destructive).")
    cid = resolve_arg(args, "consent_id", ctx, REGION, "consent_id")
    return emit(ctx.client.eu.revoke_consent(cid), ctx, REGION)


def _flow_create(args, ctx) -> int:
    cid = resolve_arg(args, "consent_id", ctx, REGION, "consent_id")
    eu_id = resolve_arg(args, "end_user_id", ctx, REGION, "end_user_id",
                        label="end-user-id")
    res = ctx.client.eu.create_flow(cid, eu_id, language=args.language,
                                    provider_id=args.provider_id or "")
    return emit(res, ctx, REGION, open_link=args.open)


def _accounts_list(args, ctx) -> int:
    cid = resolve_arg(args, "consent_id", ctx, REGION, "consent_id")
    return emit(ctx.client.eu.list_accounts(cid, include=args.include), ctx, REGION)


def _account_get(args, ctx) -> int:
    cid = resolve_arg(args, "consent_id", ctx, REGION, "consent_id")
    aid = resolve_arg(args, "account_id", ctx, REGION, "account_id")
    return emit(ctx.client.eu.get_account(aid, cid), ctx, REGION)


def _transactions_list(args, ctx) -> int:
    cid = resolve_arg(args, "consent_id", ctx, REGION, "consent_id")
    aid = resolve_arg(args, "account_id", ctx, REGION, "account_id")
    return emit(
        ctx.client.eu.list_transactions(aid, cid, from_date=args.from_date or "",
                                        to_date=args.to_date or "", limit=args.limit),
        ctx, REGION)


def _balance(args, ctx) -> int:
    cid = resolve_arg(args, "consent_id", ctx, REGION, "consent_id")
    aid = resolve_arg(args, "account_id", ctx, REGION, "account_id")
    return emit(ctx.client.eu.check_balance(aid, cid, max_age=args.max_age), ctx, REGION)


def _verify_ownership(args, ctx) -> int:
    cid = resolve_arg(args, "consent_id", ctx, REGION, "consent_id")
    return emit(
        ctx.client.eu.verify_ownership(cid, args.customer_name,
                                       account_ids=parse_account_ids(args.account_ids)),
        ctx, REGION)


def add_parser(subparsers) -> None:
    eu = subparsers.add_parser("eu", help="Open Finance Europe (Aiia) commands.")
    sub = eu.add_subparsers(dest="eu_cmd", required=True)

    auth = sub.add_parser("auth", help="Authentication (JWT client assertion).")
    auth_sub = auth.add_subparsers(dest="auth_cmd", required=True)
    auth_sub.add_parser("token", help="Sign a JWT and create an access token.").set_defaults(func=_auth_token)

    prov = sub.add_parser("providers", help="Providers (ASPSPs).")
    prov_sub = prov.add_subparsers(dest="providers_cmd", required=True)
    p_list = prov_sub.add_parser("list", help="List supported banks.")
    p_list.add_argument("--country", default="", help="ISO 3166-1 alpha-2 filter (e.g. DK).")
    p_list.add_argument("--limit", type=int, default=25)
    p_list.set_defaults(func=_providers_list)

    cons = sub.add_parser("consent", help="Consent lifecycle.")
    cons_sub = cons.add_subparsers(dest="consent_cmd", required=True)
    co_create = cons_sub.add_parser("create", help="Create a consent.")
    co_create.add_argument("--email", required=True, help="End user email.")
    co_create.add_argument("--use-case-id", dest="use_case_id",
                           help="Use case configuration id (defaults to env).")
    co_create.add_argument("--end-user-id", dest="end_user_id",
                           help="Reuse a specific end-user id (otherwise generated/saved).")
    co_create.set_defaults(func=_consent_create)
    co_get = cons_sub.add_parser("get", help="Get consent status.")
    co_get.add_argument("--consent-id", dest="consent_id")
    co_get.set_defaults(func=_consent_get)
    co_rev = cons_sub.add_parser("revoke", help="Revoke a consent (destructive).")
    co_rev.add_argument("--consent-id", dest="consent_id")
    co_rev.add_argument("--yes", action="store_true", help="Confirm the destructive action.")
    co_rev.set_defaults(func=_consent_revoke)

    flow = sub.add_parser("flow", help="Managed flow (hosted bank login).")
    flow_sub = flow.add_subparsers(dest="flow_cmd", required=True)
    f_create = flow_sub.add_parser("create", help="Create a managed flow URL.")
    f_create.add_argument("--consent-id", dest="consent_id")
    f_create.add_argument("--end-user-id", dest="end_user_id")
    f_create.add_argument("--provider-id", dest="provider_id", help="Optional bank hint.")
    f_create.add_argument("--language", default="en")
    f_create.add_argument("--open", action="store_true", help="Open the URL in a browser.")
    f_create.set_defaults(func=_flow_create)

    acc = sub.add_parser("accounts", help="Accounts.")
    acc_sub = acc.add_subparsers(dest="accounts_cmd", required=True)
    a_list = acc_sub.add_parser("list", help="List accounts under a consent.")
    a_list.add_argument("--consent-id", dest="consent_id")
    a_list.add_argument("--include", default="balances,holders,identifiers,additionalInformation")
    a_list.set_defaults(func=_accounts_list)

    acct = sub.add_parser("account", help="Single account.")
    acct_sub = acct.add_subparsers(dest="account_cmd", required=True)
    ag = acct_sub.add_parser("get", help="Get one account by id.")
    ag.add_argument("--account-id", dest="account_id")
    ag.add_argument("--consent-id", dest="consent_id")
    ag.set_defaults(func=_account_get)

    txn = sub.add_parser("transactions", help="Transactions.")
    txn_sub = txn.add_subparsers(dest="transactions_cmd", required=True)
    t_list = txn_sub.add_parser("list", help="List transactions for an account.")
    t_list.add_argument("--account-id", dest="account_id")
    t_list.add_argument("--consent-id", dest="consent_id")
    t_list.add_argument("--from-date", dest="from_date", help="ISO date (optional).")
    t_list.add_argument("--to-date", dest="to_date", help="ISO date (optional).")
    t_list.add_argument("--limit", type=int, default=50)
    t_list.set_defaults(func=_transactions_list)

    bal = sub.add_parser("balance", help="Force a fresh balance check.")
    bal.add_argument("--account-id", dest="account_id")
    bal.add_argument("--consent-id", dest="consent_id")
    bal.add_argument("--max-age", dest="max_age", default="PT15M",
                     help="ISO 8601 freshness window; PT0S forces a live call.")
    bal.set_defaults(func=_balance)

    vo = sub.add_parser("verify-ownership", help="Verify account ownership (Insights).")
    vo.add_argument("--consent-id", dest="consent_id")
    vo.add_argument("--customer-name", dest="customer_name", required=True)
    vo.add_argument("--account-ids", dest="account_ids",
                    help="Comma-separated account ids (optional; all if omitted).")
    vo.set_defaults(func=_verify_ownership)
