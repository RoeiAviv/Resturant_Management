"The Table class represents a table in a restaurant." 
"It has methods to assign a waiter, take an order, and clear the table." 
"It tracks the availability of the table, the assigned waiter's name," 
"and the current order associated with the table."
class Table:
    def __init__(self, table_number, is_available):
        self.table_number = table_number
        self.is_available = is_available
        self.waiter_name = None
        self.order = None


    def assign_waiter(self, waiter_name):
        self.waiter_name = waiter_name

    def take_order(self, order):
        self.order = order
        print(f"Order taken for table {self.table_number}.")

    def clear_table(self):
        self.is_available = True
        self.waiter_name = None
        self.order = None
