from FoodItem import FoodItem
from FoodMenu import FoodMenu
from Restaurant import Restaurant

class FoodManager:
    def __init__(self):
        self.Restaurants = self.__PrepareRestaurants()

    def __prepareFoodItems(self):
        item1 = FoodItem("Veg Biriyani", 4, 150, "****")
        item2 = FoodItem("Chicken Biriyani", 4.2, 250, "*****")
        item3 = FoodItem("Parotta", 4.4, 60, "***")
        item4 = FoodItem("Dosa", 4.1, 50, "****")
        item5 = FoodItem("Noodles", 4.1, 30, "*****")
        return [item1, item2, item3, item4, item5]

    def __PrepareFoodMenus(self):
        foodItems = self.__prepareFoodItems()
        menu1 = FoodMenu("Veg")
        menu1.FoodItems = [foodItems[0], foodItems[3]]  # Veg Biryani & Dosa
        menu2 = FoodMenu("Non Veg")
        menu2.FoodItems = [foodItems[1], foodItems[2]]  # Chicken Biryani & Parotta
        menu3 = FoodMenu("Chinese")
        menu3.FoodItems = [foodItems[4]]  # Noodles
        return [menu1, menu2, menu3]

    def __PrepareRestaurants(self):
        foodMenus = self.__PrepareFoodMenus()
        
        res1 = Restaurant("A2B", 4.5, "Chennai", "10% Off")
        res1.FoodMenus = [foodMenus[0]]  # ✅ Only Veg
        
        res2 = Restaurant("Munyadi Vilas", 4.3, "Bangalore", "20% Off")
        res2.FoodMenus = [foodMenus[0], foodMenus[1]]  # ✅ Veg & Non-Veg
        
        res3 = Restaurant("Madurai Kannappar", 3.8, "Madurai", "25% Off")
        res3.FoodMenus = [foodMenus[0], foodMenus[1]]  # ✅ Veg & Non-Veg
        
        return [res1, res2, res3]


    def FindRestaurant(self, name):
        for res in self.Restaurants:
            if res.Name.lower() == name.lower():  # Case-insensitive search
                return res
        return None

    def FindFoodItems(self, item_name):
        """
        Searches for food items across all restaurants.
        Returns a list of (restaurant_name, FoodItem).
        """
        item_name = item_name.lower()  # Convert to lowercase for case-insensitive search
        found_items = []

        for restaurant in self.Restaurants:
            for menu in restaurant.FoodMenus:
                for food_item in menu.FoodItems:
                    if food_item.Name.lower() == item_name:
                        found_items.append((restaurant.Name, food_item))

        return found_items if found_items else None
