from __future__ import annotations

from dataclasses import asdict

from .mapper import OrderMapper, OrderRecord


class OrderRepository:
    def save(self, record: OrderRecord) -> None:
        raise NotImplementedError

    def find_by_id(self, order_id: str) -> OrderRecord:
        raise NotImplementedError


class InMemoryOrderRepository(OrderRepository):
    def __init__(self) -> None:
        self._storage: dict[str, dict] = {}
        self._mapper = OrderMapper()

    def save(self, record: OrderRecord) -> None:
        self._storage[record.order_id] = asdict(record)

    def find_by_id(self, order_id: str) -> OrderRecord:
        stored = self._storage[order_id]
        return OrderRecord(**stored)
