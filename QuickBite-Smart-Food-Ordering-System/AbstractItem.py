from abc import ABC, abstractmethod

# AbstractItem.py
class AbstractItem(ABC):
    def __init__(self, name, rating=None):
        self.Name = name
        self.Rating = rating

    @abstractmethod
    def DisplayItem(self):
        pass