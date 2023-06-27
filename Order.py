"The Order class represents an order containing items handled by a chef." 
"It provides methods to calculate the total price, add items, remove items," 
"and edit items within the order."

class Order:
        
        def __init__(self, chef_id, items):
            self.chef_id = chef_id
            self.items = items
            self.total_price = self.calculate_total_price()
        
        def calculate_total_price(self):
            total_price = 0
            for item in self.items:
                total_price += item.price
            return total_price


        def add_item(self, item):
            self.items.append(item)
        
        def remove_item(self, item):
            if item in self.items:
                self.items.remove(item)
        
        def edit_item(self, old_item, new_item):
            if old_item in self.items:
                index = self.items.index(old_item)
                self.items[index] = new_item