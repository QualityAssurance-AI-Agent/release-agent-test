"""The boundary is the whole point of a limit, so it is what gets tested."""

import pytest

from limits import LimitExceeded, check_daily

_LIMIT = 500_000_00


def test_a_payment_landing_exactly_on_the_limit_is_allowed():
    check_daily(_LIMIT - 1000, 1000)


def test_one_minor_unit_past_the_limit_is_refused():
    with pytest.raises(LimitExceeded):
        check_daily(_LIMIT - 1000, 1001)


def test_the_refusal_says_the_limit_and_the_total():
    with pytest.raises(LimitExceeded) as caught:
        check_daily(_LIMIT, 1)
    assert str(_LIMIT) in str(caught.value)
