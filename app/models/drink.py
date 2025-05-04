from .menu_item import MenuItem
from app.config.pricing_config import DRINK_PRICES


class Drink(MenuItem):
    def __init__(self, name: str, size: str):
        """
        Initialize a Drink object.

        Args:
            name (str): The name of the drink.
            size (str): The size of the drink.
        """
        self.name = name
        self.size = size

    def calculate_price(self) -> float:
        """
        Calculate the price of the drink based on its name and size.

        Returns:
            float: The calculated price of the drink.
        """
        return DRINK_PRICES.get((self.name, self.size), 0.0)

    def get_description(self) -> str:
        """
        Get the description of the drink.

        Returns:
            str: The description of the drink.
        """
        return f"{self.size.capitalize()} {self.name.capitalize()}"
