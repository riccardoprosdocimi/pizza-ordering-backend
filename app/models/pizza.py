from app.models.menu_item import MenuItem
from app.config.pricing_config import PIZZA_BASE_PRICES, CRUST_PRICES, TOPPING_PRICES


class Pizza(MenuItem):
    def __init__(self, size: str, crust: str, toppings: list[str]):
        """
        Initialize a Pizza object.

        Args:
            size (str): The size of the pizza.
            crust (str): The type of crust for the pizza.
            toppings (list[str]): The list of toppings for the pizza.
        """
        self.size = size
        self.crust = crust
        self.toppings = toppings

    def calculate_price(self) -> float:
        """
        Calculate the price of the pizza.

        Returns:
            float: The total price of the pizza.
        """
        base_price = PIZZA_BASE_PRICES.get(self.size, 0.0)
        crust_price = CRUST_PRICES.get(self.crust, 0.0)
        toppings_price = sum(TOPPING_PRICES.get(t, 0.0) for t in self.toppings)
        return base_price + crust_price + toppings_price

    def get_description(self) -> str:
        """
        Get the description of the pizza.

        Returns:
            str: The description of the pizza.
        """
        return f"{self.size.capitalize()} pizza with {self.crust} crust and toppings: {', '.join(self.toppings)}"
