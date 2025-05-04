from abc import ABC, abstractmethod
from app.entities.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order):
        """
        Saves the given order.

        Args:
            order (Order): The order to be saved.
        """
        pass

    @abstractmethod
    def load_all(self) -> list[Order]:
        """
        Loads all orders.

        Returns:
            list[Order]: A list of all orders.
        """
        pass
