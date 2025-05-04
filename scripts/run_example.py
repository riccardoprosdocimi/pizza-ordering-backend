from app.models.pizza import Pizza
from app.models.drink import Drink
from app.models.dessert import Dessert
from app.entities.order import Order
from app.services.discount import HighestPricedPizzaHalfOff
from app.services.order_service import OrderService


def run_example():
    """
    Runs an example of a pizza ordering process.

    This function creates an order with various items such as pizzas, drinks, and desserts.
    It applies a discount policy to the order and calculates the total with the discount.
    Finally, it prints the order summary and the total with the discount.
    """

    order = Order()
    order.add_item(Pizza("small", "thin", []))
    order.add_item(Pizza("medium", "thick", ["pepperoni"]))
    order.add_item(Pizza("large", "stuffed", ["pepperoni", "mushrooms", "onions"]))
    order.add_item(Dessert("brownie"))
    order.add_item(Dessert("ice cream"))
    order.add_item(Drink("coke", "medium"))
    order.add_item(Drink("coke", "large"))

    service = OrderService(discount_policy=HighestPricedPizzaHalfOff())
    total = service.process_order(order)

    print("Order summary:")
    print(order.summary())
    print(f"Total with discount: ${total:.2f}")

if __name__ == "__main__":
    """
    Entry point for the script.
    Calls the run_example function to demonstrate the pizza ordering process.
    """
    run_example()
