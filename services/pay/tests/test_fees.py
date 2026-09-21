"""Fees are money, so the rounding is the part worth testing."""

import pytest

from fees import UnknownMethod, fee_minor, net_minor


def test_a_card_fee_is_percentage_plus_fixed():
    # 2.9% of 10.00 is 29c, plus the 30c fixed component.
    assert fee_minor(1000, "card") == 59


def test_a_card_fee_rounds_half_up_rather_than_truncating():
    # 2.9% of 1.50 is 4.35c: truncating would quietly favour the merchant.
    assert fee_minor(150, "card") == 34


def test_a_bank_fee_is_flat():
    assert fee_minor(500, "bank") == 80
    assert fee_minor(500_00, "bank") == 80


def test_the_net_is_the_amount_less_the_fee():
    assert net_minor(1000, "card") == 1000 - 59


def test_a_non_positive_amount_is_refused():
    with pytest.raises(ValueError):
        fee_minor(0, "card")


def test_an_unknown_method_is_refused_by_name():
    with pytest.raises(UnknownMethod) as caught:
        fee_minor(1000, "crypto")
    assert "crypto" in str(caught.value)
