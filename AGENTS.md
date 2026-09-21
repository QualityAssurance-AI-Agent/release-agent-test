# Working on the payments service

A small read API over payments: search, fetch one, and the fee and receipt helpers
that the console and the reconciliation job both depend on.

Amounts are stored and passed around in **minor units** (cents), as integers. Nothing
in this service should hold money in a float. Formatting to a human-readable string
happens once, in `_view`, and the tests pin the rounding — if you change it you will
see them fail, which is the point.

## Layout

```
services/pay/      the service: api.py, handler.py, validation.py, fees.py, receipts.py
services/pay/tests/  pytest, run with `pytest tests` from services/pay
web/               the search UI
docs/              what support and on-call read
```

`handler.py` is the Lambda entry point. It stamps `BUILD_INFO.json` into the package
at build time, so a running function can say which commit it came from.

## Release rules

Every deployment must be preceded by a passing code review and a passing security
scan. Nothing reaches an environment without both.

Any change to source code, services or libraries has to pass unit tests before it is
deployed. Documentation-only changes do not.

Payment code and the backend APIs carry the money path, so any change to them must
pass a load test before production. We have been burned by a query that was fine at
ten requests a second and fell over at a hundred.

Production is never the first environment: a non-production environment must be
released first. And a production deployment needs an approval from the on-call SRE —
not because we expect to reject them, but because somebody should know it happened.

## Environments

`beta` is a Lambda alias, `gamma` and `prod` run on ECS. The release path is
beta, then gamma, then production.
