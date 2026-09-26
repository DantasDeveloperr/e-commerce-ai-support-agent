from data_loader import find_order


def test_find_existing_order():
    order = find_order(1001)

    assert order is not None
    assert order.order_id == 1001


def test_find_non_existing_order():
    order = find_order(9999)

    assert order is None