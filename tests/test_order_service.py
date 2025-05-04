from app.entities.order import Order
from app.models.pizza import Pizza
from app.services.order_service import OrderService
import pytest


def test_order_service_total():
    """
    Test the total price calculation in the OrderService class.

    This test case creates an Order object and adds a Pizza object to it.
    It then creates an instance of the OrderService class and calls the
    process_order method with the created Order object. The expected total
    price is calculated using the calculate_price method of the Pizza object.
    The test asserts that the actual total price returned by the
    process_order method is approximately equal to the expected total price.

    """
    order = Order()
    order.add_item(Pizza("large", "thin", ["pepperoni"]))
    service = OrderService()
    assert pytest.approx(service.process_order(order), 0.01) == Pizza("large", "thin", ["pepperoni"]).calculate_price()
    