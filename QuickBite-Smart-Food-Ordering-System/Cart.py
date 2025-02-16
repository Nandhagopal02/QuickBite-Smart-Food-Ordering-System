class Cart:
    def __init__(self, items, choices):
        self.Choices = choices
        self.FoodItems = self.__AddtoCart(items)

    def __AddtoCart(self, items):
        fooddic = {}
        for choice in self.Choices:
            if choice > len(items) or choice <= 0:
                print(f"Invalid choice: {choice}")
                continue
            if choice in fooddic:
                fooddic[choice] += 1
            else:
                fooddic[choice] = 1
        return fooddic

    def ProcessOrder(self, fooditems):
        total = 0
        for item in self.FoodItems:
            price = self.FoodItems[item] * fooditems[item-1].Price
            print(f"{fooditems[item-1].Name} x {self.FoodItems[item]}")
            total += price

        print(f"Total: {total}")