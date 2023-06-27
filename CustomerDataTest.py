from objects.Customer import Customer
import unittest
from data.CustomerData import CustomerData
import os

class CustomerDataTest(unittest.TestCase):
    
    def setUp(self):
        # Create an instance of CustomerData
        self.customer_data = CustomerData('/content/test_customers.csv')

    def tearDown(self):
        # Delete the test_customers.csv file after each test

        if os.path.exists('/content/test_customers.csv'):
            os.remove('/content/test_customers.csv')

    def test_save_and_load_info(self):
        # Create some sample customers
        customers = [
            Customer('4252551', 'Roei', 'roy4050@gmail.com', '0541516161'),
            Customer('2525262', 'Hadas', 'Hadas3060@gmail.com', '0524513616')]
        cust_data = CustomerData('customer.csv')
        cust_data.save_info(customers)
        self.customer_data.save_info(customers)
        loaded_customers = self.customer_data.load_info()


        self.assertEqual(len(loaded_customers), len(customers))
        for i in range(len(customers)):
            self.assertEqual(loaded_customers[i].id, customers[i].id)
            self.assertEqual(loaded_customers[i].name, customers[i].name)
            self.assertEqual(loaded_customers[i].email, customers[i].email)
            self.assertEqual(loaded_customers[i].phone, customers[i].phone)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)