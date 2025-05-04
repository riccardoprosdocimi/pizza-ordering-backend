from app.services.discount import HighestPricedPizzaHalfOff
from app.models.dessert import Dessert
from app.models.drink import Drink
from app.models.pizza import Pizza
import pytest


def test_discount_applies_to_highest_priced_pizza():
    """
    Test case to verify that the discount applies to the highest priced pizza.

    It creates a list of items including pizzas, desserts, and drinks.
    Calculates the total price of all items.
    Applies the discount to the items and calculates the discounted price.
    Verifies that the discounted price is equal to the total price minus the expected discount.

    Returns:
        None
    """
    discount = HighestPricedPizzaHalfOff()
    items = [
        Pizza("small", "thin", ["onions"]),
        Pizza("medium", "thick", ["pepperoni"]),
        Pizza("large", "stuffed", ["mushrooms, pepperoni"]),
        Dessert("ice cream"),
        Drink("coke", "medium")
    ]
    total = sum(p.calculate_price() for p in items)
    discounted = discount.apply(items, total)
    expected_discount = items[2].calculate_price() * 0.5
    assert pytest.approx(discounted, 0.01) == total - expected_discount
