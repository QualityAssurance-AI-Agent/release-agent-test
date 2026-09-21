"""Receipt identifiers.

Customer-facing, so deliberately not the internal payment id: exposing a sequential
internal id lets anyone count how much business went through today.
"""

import hashlib

_PREFIX = "RCPT"


def receipt_id(payment_id: str, created_at: str) -> str:
    """A stable, opaque receipt id for a payment.

    Derived rather than stored so the same payment always yields the same receipt,
    and includes the timestamp so two payments that somehow share an id do not share
    a receipt.
    """
    if not payment_id:
        raise ValueError("payment_id is required")
    digest = hashlib.sha256(f"{payment_id}|{created_at}".encode()).hexdigest()
    return f"{_PREFIX}-{digest[:12].upper()}"
