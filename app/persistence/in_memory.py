from app.persistence.repository import OrderRepository
from app.entities.order import Order


class InMemoryOrderRepository(OrderRepository):
    """
    In-memory implementation of the OrderRepository interface.
    Stores orders in a list in memory.
    """

    def __init__(self):
        self.orders = []

    def save(self, order: Order):
        """
        Saves the given order to the in-memory list of orders.

        Args:
            order (Order): The order to be saved.
        """
        self.orders.append(order)

    def load_all(self) -> list[Order]:
        """
        Returns a list of all orders stored in memory.

        Returns:
            list[Order]: A list of all orders.
        """
        return self.orders
