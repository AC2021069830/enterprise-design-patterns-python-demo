from .domain import LineItem, Order
from .repository import InMemoryOrderRepository
from .service import OrderService


def test_place_order_saves_total() -> None:
    repository = InMemoryOrderRepository()
    service = OrderService(repository)

    order = Order(
        order_id="ORD-3001",
        items=[
            LineItem(name="Keyboard", price=50.0, quantity=1),
            LineItem(name="Mouse", price=25.0, quantity=2),
        ],
    )

    saved_order = service.place_order(order)
    stored_order = repository.find_by_id("ORD-3001")

    assert saved_order.total == 100.0
    assert stored_order.total == 100.0


def test_place_order_rejects_invalid_total() -> None:
    repository = InMemoryOrderRepository()
    service = OrderService(repository)

    try:
        service.place_order(Order(order_id="ORD-3002", items=[]))
    except ValueError as error:
        assert "invalid order total" in str(error)
    else:
        raise AssertionError("expected ValueError")
