from objects.Item import Item
import os
import unittest
from data.ItemData import ItemData

class ItemDataTest(unittest.TestCase):

    def setUp(self):
        self.item_data = ItemData("test_items.csv")

    def tearDown(self):  
        if os.path.exists("test_items.csv"):
            os.remove("test_items.csv")

    def test_save_and_load_info(self):
        items = [
            Item('Arenchine', 'Starter', 32, 'Cheese, Rice'),
            Item('Pasta', 'Main course', 45, 'Pasta, Mushrooms, Cream'),
            Item('Water', 'Beverage', 6.5, 'Water'),
            Item('A piece of cake', 'Dessert', 25, 'Suger, Egg, Butter, flour')]
        item_data=ItemData('item.csv')
        item_data.save_info(items)
        watch_info = item_data.load_info()

        self.item_data.save_info(items)


        loaded_items = self.item_data.load_info()


        self.assertEqual(len(loaded_items), len(items))
        for i in range(len(items)):
            self.assertEqual(loaded_items[i].name, items[i].name)
            self.assertEqual(loaded_items[i].category, items[i].category)
            self.assertEqual(loaded_items[i].price, items[i].price)
            self.assertEqual(loaded_items[i].ingredients, items[i].ingredients)



unittest.main(argv=[''], exit=False)