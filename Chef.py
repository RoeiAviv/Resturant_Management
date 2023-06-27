from objects.Employee import Employee

"The Chef class extends the functionality of the Worker class." 
"It provides methods for removing, adding and editing menu items." 
"It interacts with the MenuData and Item classes to perform these operations on menu data." 
"The class uses the load_info and save_info methods of MenuData to load and save menu" 
"information from or to a file."

class Chef(Employee):

    def __init__(self, id, name, email, phone):
        super().__init__(id, name, email, phone)

    def remove_item_from_menu(self, menu_data, item_name):
        menus = menu_data.load_info()
        updated_menus = [menu for menu in menus if menu.name != item_name]
        if len(menus) == len(updated_menus):
            print(f"Item {item_name} not found in the menu.")
        else:
            menu_data.save_info(updated_menus)
            print(f"Item {item_name} has been removed from the menu.")

    def add_item_to_menu(self, menu_data, item):
        menus = menu_data.load_info()
        menus.append(item)
        menu_data.save_info(menus)
        print(f"Item {item.name} has been added to the menu.")

    def edit_item_in_menu(self, menu_data, old_item_name, new_item):
        menus = menu_data.load_info()
        for menu in menus:
            if menu.name == old_item_name:
                menu.name = new_item.name
                menu.category = new_item.category
                menu.price = new_item.price
                menu.ingredients = new_item.ingredients
                menu_data.save_info(menus)
                print(f"Item {old_item_name} has been edited in the menu.")
            else:
               print(f"Item {old_item_name} not found in the menu.")