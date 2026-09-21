"""A receipt id must be stable, opaque, and not the internal id."""

import pytest

from receipts import receipt_id


def test_the_same_payment_always_yields_the_same_receipt():
    first = receipt_id("pay_1001", "2026-09-01T10:00:00Z")
    assert receipt_id("pay_1001", "2026-09-01T10:00:00Z") == first


def test_the_receipt_does_not_leak_the_internal_id():
    assert "pay_1001" not in receipt_id("pay_1001", "2026-09-01T10:00:00Z")


def test_the_timestamp_is_part_of_the_identity():
    assert receipt_id("pay_1001", "2026-09-01T10:00:00Z") != receipt_id(
        "pay_1001", "2026-09-02T10:00:00Z"
    )


def test_a_missing_payment_id_is_refused():
    with pytest.raises(ValueError):
        receipt_id("", "2026-09-01T10:00:00Z")
