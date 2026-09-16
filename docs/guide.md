# Operating the payments service

## Searching payments

`GET /api/payments?q=<query>` returns up to 25 payments, newest first. Pass
`limit` to change the page size; values outside 1..100 are rejected.

## Environments

Changes are released beta, then gamma, then production. Production requires an
approval from the on-call SRE.

## Rate limits

Search is limited to 20 requests per minute per token. Exceeding it returns 429.
