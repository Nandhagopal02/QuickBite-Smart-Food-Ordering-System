# FoodMenu.py
from AbstractItem import AbstractItem
from FoodItem import FoodItem

# FoodMenu.py
from AbstractItem import AbstractItem
from FoodItem import FoodItem  # assuming you already have this class defined elsewhere

class FoodMenu(AbstractItem):
    def __init__(self, name):
        super().__init__(name)
        self.__FoodItems = []

    @property
    def FoodItems(self):
        return self.__FoodItems

    @FoodItems.setter
    def FoodItems(self, items):
        for item in items:
            if not isinstance(item, FoodItem):
                print("Invalid FoodItem.")
                return
        self.__FoodItems = items

    # Implementing the abstract method 'DisplayItem'
    def DisplayItem(self):
        print(f"Menu: {self.Name}")
        for food_item in self.__FoodItems:
            food_item.DisplayItem()
