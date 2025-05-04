from .menu_item import MenuItem
from app.config.pricing_config import DESSERT_PRICES


class Dessert(MenuItem):
    def __init__(self, name: str):
        """
        Initialize a Dessert object.

        Args:
            name (str): The name of the dessert.
        """
        self.name = name

    def calculate_price(self) -> float:
        """
        Calculate the price of the dessert.

        Returns:
            float: The price of the dessert.
        """
        return DESSERT_PRICES.get(self.name, 0.0)

    def get_description(self) -> str:
        """
        Get the description of the dessert.

        Returns:
            str: The description of the dessert.
        """
        return self.name.capitalize()
