from AbstractItem import AbstractItem
from FoodManager import FoodManager
from Cart import Cart

class MainMenu(AbstractItem):
    __Options = {
        1: "ShowRestaurants",
        2: "SearchRestaurants",
        3: "SearchFoodItems",
        4: "Logout"
    }

    def __init__(self):
        self.__FoodManager = FoodManager()

    def DisplayItem(self):
        return super().DisplayItem()

    def ShowRestaurants(self):
        print("\n✅ List of Available Restaurants:")
        for index, res in enumerate(self.__FoodManager.Restaurants, 1):
            print(f"{index}. {res.Name} (Rating: {res.Rating})")

        try:
            choice = int(input("\nPlease Select a Restaurant (number): "))
            if 1 <= choice <= len(self.__FoodManager.Restaurants):
                res = self.__FoodManager.Restaurants[choice - 1]
                print(f"\n✅ Selected Restaurant: {res.Name}")
                self.ShowFoodMenus(res.FoodMenus)  # FIXED: Corrected attribute name
            else:
                print("\n❌ Invalid choice! Please select a valid restaurant number.")
        except ValueError:
            print("\n❌ Invalid input! Please enter a valid number.")

    def ShowFoodItems(self, foodItems=None):

        

        if foodItems:
            print("\n✅ List of Food Items:")
            for i, fooditem in enumerate(foodItems, 1):
                print(f"{i}. {fooditem.Name} (Price: {fooditem.Price}, Rating: {fooditem.Rating})")

            try:
                choices = list(map(int, input("\nEnter food choices separated by commas: ").split(",")))

                # Validate user choices
                selected_items = []
                for choice in choices:
                    if 1 <= choice <= len(foodItems):
                        selected_items.append(foodItems[choice - 1]) 
                
                if selected_items:
                    cart = Cart(selected_items, choices)  # ✅ FIX: Pass correct arguments
                    cart.ProcessOrder(selected_items)  # ✅ FIX: Now passing fooditems
                else:
                    print("\n❌ No valid items selected.")
            except ValueError:
                print("\n❌ Invalid input! Please enter valid item numbers.")
        else:
            print("\n❌ No food items available.")



    def SearchRestaurants(self):
        resName = input("\n🔍 Enter a Restaurant Name: ").strip()
        res = self.__FoodManager.FindRestaurant(resName)

        if res:
            print(f"\n✅ Found: {res.Name} (Rating: {res.Rating})")
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print(f"\n❌ No Restaurant found with the name '{resName}'.")

    def SearchFoodItems(self):
        itemName = input("🔍 Enter a Food Item Name: ").strip()
        items = self.__FoodManager.FindFoodItems(itemName)

        if items:
            print("\n✅ Found Food Items:")
            for i, (restaurant_name, food_item) in enumerate(items, 1):
                print(f"{i}. {food_item.Name} (Price: {food_item.Price}, Rating: {food_item.Rating}) - Available at {restaurant_name}")

            try:
                choices = list(map(int, input("\nEnter your food choices separated by commas: ").split(",")))
                selected_items = [items[i - 1][1] for i in choices if 1 <= i <= len(items)]

                if selected_items:
                    cart = Cart(selected_items, choices)
                    cart.ProcessOrder(selected_items)
                else:
                    print("\n❌ No valid items selected.")
            except ValueError:
                print("\n❌ Invalid input! Please enter valid item numbers.")
        else:
            print("\n❌ No food items found matching your search.")


    def ShowFoodMenus(self, menus):
        print("\n✅ Available Menus:")
        for i, menu in enumerate(menus, 1):
            print(f"{i}. {menu.Name}")

        try:
            choice = int(input("\nPlease Choose a Menu (number): "))
            if 1 <= choice <= len(menus):
                fooditems = menus[choice - 1].FoodItems
                self.ShowFoodItems(fooditems)
            else:
                print("\n❌ Invalid choice! Please select a valid menu.")
        except ValueError:
            print("\n❌ Invalid input! Please enter a valid number.")

    def Logout(self):
        print("🔒 Logging out... You have logged out successfully!")
        from LoginSystem import LoginSystem  # Import LoginSystem
        login_system = LoginSystem()  # Create a new instance
        
        # Replace Init() with the correct method
        login_system.validateOption(1)  # Redirect to login screen






    def Start(self):
        while True:
            print("\n📌 **Main Menu**:")
            for option, name in MainMenu.__Options.items():
                print(f"{option}. {name.replace('Show', '📜 Show').replace('Search', '🔍 Search').replace('Logout', '🔒 Logout')}")

            try:
                choice = int(input("\n🛎️ Please Enter Your Choice: "))
                if choice in MainMenu.__Options:
                    method_name = MainMenu.__Options[choice]
                    getattr(self, method_name)()  # ✅ Call the selected function
                else:
                    print("\n❌ Invalid choice! Please select a valid option.")
            except (ValueError, KeyError):
                print("\n❌ Invalid input! Please enter a valid number.")