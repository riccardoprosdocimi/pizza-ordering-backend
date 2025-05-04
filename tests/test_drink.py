from app.models.drink import Drink


def test_drink_price():
    """
    Test the calculate_price method of the Drink class.
    """
    drink = Drink("coke", "medium")
    assert drink.calculate_price() == 2.0


def test_drink_description():
    """
    Test the get_description method of the Drink class.
    """
    drink = Drink("coke", "large")
    assert drink.get_description() == "Large Coke"
