"""Request validation for the payments API."""

_CURRENCIES = frozenset({"USD", "EUR", "GBP", "JPY", "CHF", "SEK"})


class ValidationError(ValueError):
    """A request the API refuses to process."""


def validate_amount(amount_minor: int) -> None:
    if not isinstance(amount_minor, int):
        raise ValidationError("amount must be an integer number of minor units")
    if amount_minor <= 0:
        raise ValidationError("amount must be positive")


def validate_currency(currency: str) -> None:
    if currency not in _CURRENCIES:
        raise ValidationError(
            f"unsupported currency: {currency}; supported: "
            + ", ".join(sorted(_CURRENCIES))
        )
