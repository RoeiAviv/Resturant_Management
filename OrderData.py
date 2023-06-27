import csv
from objects.Order import Order

"The OrderData class provides functionality to save, load, and manipulate order data using CSV files."
"It uses the csv module and interacts with the order class to handle order information." 
"The department maintains an internal list (self.orders) to store the loaded orders and provides" 
"methods to add new orders and check the presence of specific items within the orders."

class OrderData:
    def __init__(self, file_order):
        self.file_order = file_order
        self.orders = []  # Add the orders attribute to store the list of orders

    def save_info(self, orders):
        with open(self.file_order, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Order Number', 'Chef ID', 'Items'])
            for order in orders:
                writer.writerow([order.order_number, order.chef_id, ",".join(order.items)])

    def load_info(self):
        self.orders = []  # Clear the existing orders list
        with open(self.file_order, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 3:  # Check if row has enough elements
                    order_number = row[0]
                    chef_id = row[1]
                    items = row[2].split(",")
                    self.orders.append(Order(chef_id, order_number, items))  # Append the loaded order to the list
        return self.orders

    def add_order(self, order):
        self.orders.append(order)

    def contains_item(self, item_name):
        for order in self.orders:
            for item in order.items:
                if item.name.lower() == item_name.lower():
                    return True
        return False

