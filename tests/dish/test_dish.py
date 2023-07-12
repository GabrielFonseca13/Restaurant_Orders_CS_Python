from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish_1 = Dish("pizza", 35.00)
    dish_2 = Dish("pizza", 35.00)
    dish_3 = Dish("sushi", 45.00)

    assert dish_1.name == "pizza"
    assert dish_1.name != "sushi"

    assert dish_1.__hash__() == dish_2.__hash__()
    assert dish_1.__hash__() != dish_3.__hash__()

    assert dish_1 == dish_2
    assert dish_1 != dish_3

    assert dish_1.__repr__() == "Dish('pizza', R$35.00)"

    with pytest.raises(TypeError):
        Dish("pizza", "R$ 35.00")

    with pytest.raises(ValueError):
        Dish("pizza", -10)

    ingredient = Ingredient("farinha")
    dish_1.add_ingredient_dependency(ingredient, 15)
    assert dish_1.get_ingredients() == set([ingredient])
    assert dish_1.get_restrictions() == ingredient.restrictions
