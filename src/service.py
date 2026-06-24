from .mapper import OrderMapper
from .repository import OrderRepository
from .domain import Order


class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository
        self._mapper = OrderMapper()

    def place_order(self, order: Order) -> Order:
        order.total = order.calculate_total()
        if order.total <= 0:
            raise ValueError("invalid order total")

        record = self._mapper.to_record(order)
        self._repository.save(record)
        return order
