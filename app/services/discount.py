from abc import ABC, abstractmethod
from app.models.menu_item import MenuItem
from app.models.pizza import Pizza


class DiscountPolicy(ABC):
    @abstractmethod
    def apply(self, items: list[MenuItem], total: float) -> float:
        """
        Applies a discount to the total price based on the given list of menu items and the total price.

        Args:
            items (list[MenuItem]): The list of menu items.
            total (float): The total price.

        Returns:
            float: The discounted total price.
        """
        pass

class HighestPricedPizzaHalfOff(DiscountPolicy):
    def apply(self, items: list[MenuItem], total: float) -> float:
        """
        Applies a discount of 50% to the highest priced pizza in the list of menu items, if there are at least 2 pizzas.

        Args:
            items (list[MenuItem]): The list of menu items.
            total (float): The total price.

        Returns:
            float: The discounted total price.
        """
        pizzas = [item.calculate_price() for item in items if isinstance(item, Pizza)]
        if len(pizzas) >= 2:
            sorted_pizzas = sorted(pizzas, reverse=True)
            discount = sorted_pizzas[0] * 0.5
            return total - discount
        return total
