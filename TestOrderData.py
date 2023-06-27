import unittest
import os
from objects.Order import Order
from data.OrderData import OrderData

class TestOrderData(unittest.TestCase):

    def setUp(self):
        self.filename = 'orders.csv'  # Absolute file path
        orders = [
            Order('1', '208321469', ['Pizza', 'Burger']),
            Order('2', '209582853', ['Salad', 'Soup']),
            Order('3', '314753427', ['Pasta', 'Bread'])
        ]
        order_data = OrderData('orders.csv')
        order_data.save_info(orders)
        self.order_data.save_info(orders)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_info_load_info(self):
        self.order_data.save_info(self.orders)

        loaded_orders = self.order_data.load_info()
        self.assertEqual(len(loaded_orders), len(self.orders))
        for i in range(len(self.orders)):
            self.assertEqual(loaded_orders[i].order_number, self.orders[i].order_number)
            self.assertEqual(loaded_orders[i].chef_id, self.orders[i].chef_id)
            self.assertEqual(loaded_orders[i].items, self.orders[i].items)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)