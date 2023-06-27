from objects.Item import Item
from objects.Menu import Menu
import csv

"An implementation of the MenuData class that handles operations related to menu data." 
"It provides methods to save, load, and retrieve menu information from a CSV file."
"The class interacts with the Item and Menu classes to create and manipulate menu objects."

class MenuData:
    def __init__(self, file_menu):
        self.file_menu = file_menu

    def save_info(self, menus):
        with open(self.file_menu, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'category', 'price', 'ingredients'])
            for menu in menus:
                for item in menu.items:
                    writer.writerow([menu.name, menu.category, item.name, item.price, ",".join(item.ingredients)])

    def load_info(self):
        menus = []
        current_menu = None
        with open(self.file_menu, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                menu_name = row[0]
                category = row[1]
                price = float(row[2])
                ingredients = row[3].split(".")

                if current_menu is None or current_menu.name != menu_name:
                    current_menu = Menu(menu_name, category, price, ingredients)
                    menus.append(current_menu)
                    
                item = Item(menu_name, category, price, ingredients)
                current_menu.add_item(item)
        return menus



        # if menu_exists:
        #     self.save_info(menus)
        #     print("Menu removed successfully.")
        # else:
        #     print("Menu not found.")