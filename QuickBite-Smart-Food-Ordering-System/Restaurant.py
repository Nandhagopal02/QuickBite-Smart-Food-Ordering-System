# Restaurant.py
from AbstractItem import AbstractItem
from FoodMenu import FoodMenu
class Restaurant(AbstractItem):
    def __init__(self, name, rating, location, offer):
        super().__init__(name, rating)
        self.Location = location
        self.Offer = offer
        self.__FoodMenus = []  # ✅ Initialize properly

    @property
    def FoodMenus(self):
        return self.__FoodMenus

    @FoodMenus.setter
    def FoodMenus(self, items):
        if not all(isinstance(item, FoodMenu) for item in items):
            print("Invalid FoodMenu.")
            return
        self.__FoodMenus = items  # ✅ Assign FoodMenus properly

    def DisplayItem(self):
        print(f"{self.Name} - Rating: {self.Rating} - Location: {self.Location} - Offer: {self.Offer}")
        print("Food Menus:")
        for menu in self.FoodMenus:
            menu.DisplayItem()
