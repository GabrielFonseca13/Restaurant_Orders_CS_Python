from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Requisito 1
def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    assert ingredient1.name == "queijo mussarela"
    assert ingredient1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    ingredient2 = Ingredient("farinha")
    assert repr(ingredient2) == "Ingredient('farinha')"

    ingredient3 = Ingredient("bacon")
    ingredient4 = Ingredient("bacon")
    ingredient5 = Ingredient("manteiga")
    assert ingredient3 == ingredient4
    assert not ingredient3 == ingredient5

    ingredient6 = Ingredient("caldo de carne")
    ingredient7 = Ingredient("caldo de carne")
    ingredient8 = Ingredient("camarão")
    assert hash(ingredient6) == hash(ingredient7)
    assert hash(ingredient6) != hash(ingredient8)

    ingredient9 = Ingredient("farinha")
    ingredient10 = Ingredient("bacon")
    assert hash(ingredient9) != hash(ingredient10)

    ingredient11 = Ingredient("salmão")
    expected_restrictions = {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
    assert ingredient11.restrictions == expected_restrictions

    ingredient12 = Ingredient("queijo provolone")
    assert repr(ingredient12) == "Ingredient('queijo provolone')"
