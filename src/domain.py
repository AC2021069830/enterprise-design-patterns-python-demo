from dataclasses import dataclass


@dataclass
class LineItem:
    name: str
    price: float
    quantity: int


@dataclass
class Order:
    order_id: str
    items: list[LineItem]
    total: float = 0.0

    def calculate_total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
