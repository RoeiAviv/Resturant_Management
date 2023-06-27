import unittest
import os
from objects.Menu import Menu
from data.MenuData import MenuData

class TestMenuData(unittest.TestCase):

    def setUp(self):
        self.file_path = 'menu.csv'  
        menus = [
            Menu('Menu_1', 'Pasta', 'Starter+Main course', 45, True),
            Menu('Menu_2', 'A piece of cake', 'dessert', 25, True)]
        menu_data = MenuData('menu.csv')
        menu_data.save_info(menus)
        self.menu_data.save_info(menus)
        loaded_menu_menu=self.menu_data.laod_info()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_info_load_info(self):
        self.menu_data.save_info(self.menus)
        loaded_menus = self.menu_data.load_info()

        self.assertEqual(len(loaded_menus), len(self.menus))
        for i in range(len(self.menus)):
            self.assertEqual(loaded_menus[i].Num_of_Menu, self.menus[i].Num_of_Menu)
            self.assertEqual(loaded_menus[i].name, self.menus[i].name)
            self.assertEqual(loaded_menus[i].category, self.menus[i].category)
            self.assertEqual(loaded_menus[i].price, self.menus[i].price)
            self.assertEqual(loaded_menus[i].ingredients, self.menus[i].ingredients)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)