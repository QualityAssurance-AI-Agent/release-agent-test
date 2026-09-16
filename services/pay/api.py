"""Payments read API."""

from dataclasses import dataclass, asdict


@dataclass
class PaymentView:
    """One payment, as returned to the front end."""

    id: str
    amount_minor: int
    currency: str
    status: str


class PaymentNotFound(LookupError):
    """No payment with that id."""


def search_payments(store, query: str, limit: int = 25) -> dict:
    """Search payments, newest first.

    Returns the response body: a list of payment views plus the applied query, so
    a caller can tell an empty result from a dropped filter.
    """
    if limit < 1 or limit > 100:
        raise ValueError("limit must be between 1 and 100")

    matches = store.search(query=query, limit=limit)
    return {
        "query": query,
        "payments": [asdict(_view(record)) for record in matches],
    }


def get_payment(store, payment_id: str) -> dict:
    record = store.get(payment_id)
    if record is None:
        raise PaymentNotFound(payment_id)
    return asdict(_view(record))


def _view(record) -> PaymentView:
    return PaymentView(
        id=record["id"],
        amount_minor=record["amount_minor"],
        currency=record["currency"],
        status=record["status"],
    )
