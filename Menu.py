from objects.Item import Item

"The Menu class represents a menu, which is a type of item." 
"It extends the functionality of the Item class by allowing the addition and removal" 
"of individual items to form a collection of items within the menu."

class Menu(Item):
    def __init__(self, name, category, price, ingredients):
        super().__init__(name, category, price, ingredients)
        self.items = []


    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)