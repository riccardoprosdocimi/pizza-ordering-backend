from app.models.dessert import Dessert


def test_dessert_price():
    """
    Test the calculate_price method of the Dessert class.
    """
    dessert = Dessert("brownie")
    assert dessert.calculate_price() == 3.0


def test_dessert_description():
    """
    Test the get_description method of the Dessert class.
    """
    dessert = Dessert("Ice cream")
    assert dessert.get_description() == "Ice cream"
