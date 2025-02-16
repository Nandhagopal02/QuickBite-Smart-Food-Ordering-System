from  AbstractItem import AbstractItem
class FoodItem(AbstractItem):
    def __init__(self, name, rating, price, description):
        super().__init__(name, rating)
        self.Price = price
        self.description = description

    def DisplayItem(self, index=None):
        print(f"{index}. {self.Name} => Rating: {self.Rating}, Price: {self.Price}, Description: {self.description}")