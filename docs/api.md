# Payments API

## GET /api/payments

Query parameters: `q` (required), `limit` (optional, 1..100, default 25).

Response body:

    { "query": "...", "payments": [ { "id", "amount_minor", "currency", "status" } ] }
