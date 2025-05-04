from app.entities.order import Order
from app.models.pizza import Pizza
from app.persistence.in_memory import InMemoryOrderRepository


def test_order_persistence():
    """
    Test the persistence of an order in the repository.
    """
    repo = InMemoryOrderRepository()
    order = Order()
    pizza = Pizza("small", "stuffed", ["pepperoni"])
    order.add_item(pizza)
    repo.save(order)
    saved_orders = repo.load_all()
    assert len(saved_orders) == 1
    assert saved_orders[0].calculate_total() == order.calculate_total()
