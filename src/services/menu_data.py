import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set(self.insert_menu_datas(source_path))

    def insert_menu_datas(self, source_path):
        with open(source_path, encoding="utf8", newline="") as file:
            data = csv.DictReader(file)
            dishes = set()
            for content in data:
                dish_name = content["dish"]
                dish_price = float(content["price"])
                dish_ingredient = content["ingredient"]
                dish_recipe_amount = int(content["recipe_amount"])

                dishes.add(Dish(dish_name, dish_price))

                index_dish = next(iter(dishes))
                index_dish.add_ingredient_dependency(
                    Ingredient(dish_ingredient), dish_recipe_amount
                )

            return dishes
