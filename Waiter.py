from objects.Order import Order
from objects.Employee import Employee
from data.OrderData import OrderData

"The Waiter class represents a waiter in a restaurant." 
"It has methods to place an order, remove an order, and edit an order." 
"It interacts with an OrderData object to load and save order information." 
"The methods allow the waiter to perform actions related to managing orders."

class Waiter(Employee):
    def __init__(self, ID, Name, Email, Phone):
        super().__init__(ID, Name, Email, Phone, "", 0)

    def place_order(self, order_data, customer_id, items):
        orders = order_data.load_info()
        order_number = len(orders) + 1
        order = Order(order_number, customer_id, items)
        orders.append(order)
        order_data.save_info(orders)
        print(f"Order {order_number} placed successfully.")

    def remove_order(self, order_data, order_number):
        orders = order_data.load_info()
        updated_orders = [order for order in orders if order.order_number != order_number]
        if len(orders) == len(updated_orders):
            print(f"Order {order_number} not found.")
        else:
            order_data.save_info(updated_orders)
            print(f"Order {order_number} removed successfully.")

    def edit_order(self, order_data, order_number, new_items):
        orders = order_data.load_info()
        for order in orders:
            if order.order_number == order_number:
                order.items = new_items
                order_data.save_info(orders)
                print(f"Order {order_number} edited successfully.")
                break
        else:
            print(f"Order {order_number} not found.")

# waiter = Waiter("314151516", "Hadas", "Hadas@gmail.com", "0525381645")
# order_data = OrderData('Orders.csv')
# waiter.place_order(order_data, "208321469", ["Ravioli", "Pasta", "Salad"])

# order_number = 2
# waiter.remove_order(order_data, order_number)

# order_number = 1
# new_items = ["Fries", "Coke"]
# waiter.edit_order(order_data, order_number, new_items)

