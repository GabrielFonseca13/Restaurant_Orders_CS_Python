from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        menu = []

        for i in self.menu_data.dishes:
            recipe_available = self.inventory.check_recipe_availability(
                i.recipe
            )
            if not recipe_available:
                return menu
            # for i in self.menu_data.dishes:
            if restriction is None or restriction not in i.get_restrictions():
                menu_data = {
                    "dish_name": i.name,
                    "price": i.price,
                    "ingredients": i.get_ingredients(),
                    "restrictions": i.get_restrictions(),
                }
                menu.append(menu_data)
        return menu
