from dataclasses import dataclass

from .domain import Order


@dataclass
class OrderRecord:
    order_id: str
    total: float


class OrderMapper:
    def to_record(self, order: Order) -> OrderRecord:
        return OrderRecord(order_id=order.order_id, total=order.total)

    def to_order(self, record: OrderRecord) -> Order:
        return Order(order_id=record.order_id, items=[], total=record.total)
