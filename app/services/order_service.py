from app.entities.order import Order
from app.services.discount import DiscountPolicy


class OrderService:
    def __init__(self, discount_policy: DiscountPolicy = None):
        self.discount_policy = discount_policy

    def process_order(self, order: Order) -> float:
        """
        Process an order and calculate the total amount.

        Args:
            order (Order): The order to be processed.

        Returns:
            float: The total amount of the order after applying any discounts.
        """
        return order.calculate_total(self.discount_policy)
