"""Processing fees, in minor units.

Kept apart from the amount itself: a fee is a property of how a payment was taken,
and folding it into the amount is how reconciliation reports stop adding up.
"""

_CARD_BASIS_POINTS = 290          # 2.9%
_CARD_FIXED_MINOR = 30            # plus 30c
_BANK_FIXED_MINOR = 80


class UnknownMethod(ValueError):
    """A payment method with no fee schedule."""


def fee_minor(amount_minor: int, method: str) -> int:
    """The fee charged on ``amount_minor``, rounded to the nearest minor unit.

    Rounds half up rather than truncating, because truncation always favours one
    side and the difference shows up as a slow drift in reconciliation.
    """
    if amount_minor <= 0:
        raise ValueError("amount must be positive")
    if method == "card":
        return (amount_minor * _CARD_BASIS_POINTS + 5000) // 10000 + _CARD_FIXED_MINOR
    if method == "bank":
        return _BANK_FIXED_MINOR
    raise UnknownMethod(f"no fee schedule for {method!r}")


def net_minor(amount_minor: int, method: str) -> int:
    """What reaches the merchant after the fee."""
    return amount_minor - fee_minor(amount_minor, method)
