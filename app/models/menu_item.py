from abc import ABC, abstractmethod


class MenuItem(ABC):
    @abstractmethod
    def calculate_price(self) -> float:
        """
        Abstract method to calculate the price of the menu item.
        Returns:
            float: The calculated price of the menu item.
        """
        pass

    @abstractmethod
    def get_description(self) -> str:
        """
        Abstract method to get the description of the menu item.
        Returns:
            str: The description of the menu item.
        """
        pass
    