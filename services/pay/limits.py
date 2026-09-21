"""Per-account daily limits, in minor units."""

_DAILY_MINOR = 500_000_00          # 500,000 a day


class LimitExceeded(ValueError):
    """The payment would take the account past its daily limit."""


def check_daily(spent_today_minor: int, amount_minor: int) -> None:
    """Refuse a payment that would take the account past its daily limit.

    The comparison is on the total *after* this payment, so a payment that lands
    exactly on the limit is allowed and one minor unit beyond it is not.
    """
    if amount_minor > _DAILY_MINOR:
        raise LimitExceeded(
            f"this payment would reach {spent_today_minor + amount_minor}, "
            f"past the daily limit of {_DAILY_MINOR}"
        )
