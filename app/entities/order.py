from app.models.menu_item import MenuItem


class Order:
    def __init__(self):
        """
        Initializes a new Order object.
        """
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem):
        """
        Adds a menu item to the order.

        Args:
            item (MenuItem): The menu item to add.
        """
        self.items.append(item)

    def calculate_total(self, discount_policy=None) -> float:
        """
        Calculates the total price of the order.

        Args:
            discount_policy (DiscountPolicy, optional): The discount policy to apply. Defaults to None.

        Returns:
            float: The total price of the order.
        """
        total = sum(item.calculate_price() for item in self.items)
        if discount_policy:
            total = discount_policy.apply(self.items, total)
        return total

    def summary(self) -> str:
        """
        Generates a summary of the order.

        Returns:
            str: The summary of the order.
        """
        lines = [f"- {item.get_description()}" for item in self.items]
        return "\n".join(lines)

    def __str__(self) -> str:
        """
        Returns a string representation of the order.

        Returns:
            str: The string representation of the order.
        """
        return self.summary()
