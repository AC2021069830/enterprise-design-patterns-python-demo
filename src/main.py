from .domain import LineItem, Order
from .repository import InMemoryOrderRepository
from .service import OrderService


def main() -> None:
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
    stored_order = repository.find_by_id(saved_order.order_id)

    print(f"order {saved_order.order_id} saved with total ${saved_order.total:.2f}")
    print(f"stored record confirmed with total ${stored_order.total:.2f}")


if __name__ == "__main__":
    main()
