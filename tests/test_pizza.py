import pytest
from app.models.pizza import Pizza


def test_pizza_price_with_crust():
    """
    Test the calculation of the price for a pizza with crust.
    """
    pizza = Pizza("medium", "stuffed", ["pepperoni", "onions"])
    expected = 10.0 + 2.5 + 1.0 + 0.5
    assert pytest.approx(pizza.calculate_price(), 0.01) == expected


def test_pizza_description():
    """
    Test the generation of the description for a pizza.
    """
    pizza = Pizza("small", "thin", ["mushrooms"])
    assert pizza.get_description() == "Small pizza with thin crust and toppings: mushrooms"
