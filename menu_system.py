import sys
import re
"import  class from module located in the `data` package or module"
from data.EmployeeData import EmployeeData
from data.CustomerData import CustomerData
from data.OrderData import OrderData
from data.ItemData import ItemData
from data.MenuData import MenuData
from data.TableData import TableData
"import  class from module located in the `objects` package or module."
from objects.Employee import Employee
from objects.Customer import Customer
from objects.Menu import Menu
from objects.Item import Item
from objects.Order import Order
from objects.Waiter import Waiter
from objects.Chef import Chef
from objects.Manager import Manager

"Contains several static methods for managing different" 
"aspects of the restaurant, such as employees, customers, items, menus, and tables."
class Menu_system:

    "The main_menu method displays the main menu options to the user."
    @staticmethod
    def main_menu():
        print ("\nWellcome to H&R Resturant \nPlease choose an option and please behave appropriately!! \n")
        print("1. Manage Employees")
        print("2. Manage Customers")
        print("3. Manage Items")
        print("4. Manage Menus")
        print("5. Manage Tables")
        print("0. Exit")

    "The manage_employees method allows the user to view, add, and remove employees" 
    "from the system."
    @staticmethod
    def manage_employees(employee_data):
        employee_data = EmployeeData.get_instance("Employee.csv")
        while True:
            print("\n----- Employee Management -----")
            print("1. View Employees")
            print("2. Add Employee")
            print("3. Remove Employee")
            print("0. Go Back")
            choice = input("Enter your choice: ")

            if choice == "1":
                employees = employee_data.load_info()
                print("Employees:")
                for employee in employees:
                    print(f"ID: {employee.id}, Name: {employee.name}, Email: {employee.email}, Phone: {employee.phone}, Role: {employee.role}")
            elif choice == "2":
               
                employee_id = input("Enter employee ID (numeric): ")
                employees = employee_data.load_info()

                while not employee_id.isnumeric() or len(employee_id) != 9 or any(emp.id == employee_id for emp in employees):
                   if not employee_id.isnumeric() or len(employee_id) != 9:
                      print("Invalid input. Employee ID must be a numeric value and contain 9 digits.")
                   else:
                     print("ID exists. Please enter another ID.")

                   employee_id = input("Enter employee ID (numeric): ")

                # employee_id = input("Enter employee ID (numeric): ")
                # while not employee_id.isnumeric() or len(employee_id) != 9:
                #     print("Invalid input. Employee ID must be a numeric value and contain 9 digits.")
                #     employee_id = input("Enter employee ID (numeric): ")
               
               
                name = input("Enter employee name: ")
                while not (name.replace(" ", "").isalpha() and len(name) >= 2):
                    print("Invalid input. Name must contain only alphabetic characters and have at least 2 characters.")
                    name = input("Enter employee name: ")
                name=name.capitalize()

                email = input("Enter employee email: ")
                while not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                    print("Invalid email format, FIX ASAP!!!!")
                    email = input("Enter employee email: ")
                email=email.capitalize()

                phone = input("Enter employee phone (numeric): ")
                while not phone.replace("-", "").isnumeric() or len(phone.replace("-", "")) != 10:
                    print("Invalid input. Phone number must be a numeric value and contain 10 digits.")
                    phone = input("Enter employee phone (numeric): ")
                phone = phone[:3] + "-" + phone[3:]

                role = input("Enter employee role (Chef, waiter, or manager): ").lower()
                while role.lower() not in ["chef", "waiter", "manager"]:
                    print("Invalid input. Role must be either Chef, waiter, or manager.")
                    role = input("Enter employee role (Chef, waiter, or manager): ").lower()
                role = role.capitalize()

                salary = input("Enter employee salary (numeric): ")
                while not salary.isnumeric():
                    print("Invalid input. Salary must be a numeric value.")
                    salary = input("Enter employee salary (numeric): ")

                employee = Employee(employee_id, name, email, phone, role, salary)
                employee_data.add_employee(employee)
                print("Employee added successfully!")
            elif choice == "3":
                employee_id = input("Enter Employee ID to remove: ")
                if employee_data.remove_info(employee_id):
                    print("Employee removed successfully.")
                # else:
                #     print ("Sorry, There is no employee with that id ")
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

    "The manage_customers method allows the user to view, add, and remove customers" 
    "from the system."
    @staticmethod
    def manage_customers(customer_data):
        while True:
            print("\n----- Customer Management -----")
            print("1. View Customers")
            print("2. Add Customer")
            print("3. Remove Customer")
            print("0. Go Back")
            choice = input("Enter your choice: ")

            if choice == "1":
                customers = customer_data.load_info()
                print("Customers:")
                for customer in customers:
                    print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")
            elif choice == "2":
                customers = []


                customer_id = input("Enter Customer ID (numeric): ")
                customers = customer_data.load_info()
                while not customer_id.isnumeric() or len (customer_id) !=9 or any(cust.id == customer_id for cust in customers):
                    if not customer_id.isnumeric() or len(customer_id) != 9:
                        print("Invalid input. Customer ID must be an integer and contain 9 digits")
                    else:
                     print("ID exists. Please enter another ID.")
                    customer_id = input("Enter Customer ID (numeric): ")
                
                customer_name = input("Enter Customer Name: ")
                while not (customer_name.replace(" ", "").isalpha() and len(customer_name) >= 2):
                    print("Invalid input. Name must contain only alphabetic characters and have at least 2 characters.")
                    customer_name = input("Enter Customer Name: ")
                customer_name=customer_name.capitalize()

                customer_email = input("Enter Customer email: ")
                while not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', customer_email):
                    print("Invalid email format, FIX ASAP!!!!")
                    customer_email = input("Enter Customer email: ")
                customer_email=customer_email.capitalize()

                customer_phone = input("Enter Customer Phone(numeric): ")
                while not customer_phone.replace("-", "").isnumeric() or len(customer_phone.replace("-", ""))!= 10:
                    print("Invalid input. Phone number must be a numeric value and contain 10 digits.")
                    customer_phone = input("Enter Customer Phone (numeric): ")
                customer_phone = customer_phone[:3] + "-" + customer_phone[3:]

                customer = Customer(customer_id, customer_name, customer_email, customer_phone)
                customers.append(customer)
                customer_data.save_info(customers)
                print("Customer added successfully.")


            elif choice == "3":

                        customer_id = input("Enter Customer ID to remove: ")
                        if customer_data.remove_info(customer_id):
                            print ("Customer removed successfullly")

                   
            elif choice == "0":
                break
    
    "The manage_items method allows the user to view, add, and remove items from the system." 
    "It also includes functionality for checking item availability, writing item reviews," 
    "and viewing reviews for each item."
    @staticmethod
    def manage_items(all_item_data):
        while True:
            print("\n----- Item Management -----")
            print("1. View Items")
            print("2. Check Item Availability")
            print("3. Write Item Review")
            print("4. Review from the customer to each item")
            print("5. Add Item")
            print("6. Remove Item")
            print("0. Go Back")
            choice = input("Enter your choice: ")

            if choice == "1":
                items = all_item_data.load_info()
                if items:
                    print("Items:")
                    for item in items:
                        print(f"Name: {item.name}, Price: {item.price}, Category: {item.category}, Ingredients: {item.ingredients}")
                else:
                    print("No items found.")
            elif choice == "2":
                item_name = input("Enter the name of the item to check availability: ")
                item = all_item_data.get_item_by_name(item_name)
                if item:
                    print(f"The item: {item_name} is available.")
                else:
                    print(f"The item '{item_name}' is not found.")
            elif choice == "3":
                item_name = input("Enter the name of the item to write a review: ")
                item_to_review = all_item_data.get_item_by_name(item_name)
                if item_to_review:
                    review = input("Write your review: ")

                    all_items = all_item_data.load_info()
                    for item in all_items:
                        if item.name == item_to_review.name:
                            item.reviews.append(review)

                    all_item_data.save_info(all_items)
                    print("Review added successfully.")
                else:
                    print("Item not found.")
            elif choice == "4":
                item_name = input("Enter the name of the item: ")
                item = all_item_data.get_item_by_name(item_name)
                if item:
                    reviews = item.get_reviews()
                    if reviews:
                        print(f"Reviews for {item.name}:")
                        for review in reviews:
                            print(f"- {review}")
                    else:
                        print(f"No reviews found for {item.name}.")
                else:
                    print("Item not found.")
            elif choice == "5":
                while True:
                    item_name = input("Enter the name of the item to add: ")
                    if item_name.replace(" ", "").isalpha():
                        break
                    else:
                        print("Invalid input. The item name should only contain alphabetic characters and spaces.")

                while True:
                    category = input("Enter the category of the item (First Course, Main Course, Dessert, Beverage): ")
                    category = category.lower()
                    if category.strip() in ['first course', 'main course', 'dessert', 'beverage']:
                        break
                    else:
                        print("Invalid input. The category should only contain alphabetic characters and spaces. Please choose from the provided options.")

                price = None
                while True:
                    try:
                        price = float(input("Enter the price of the item: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid floating-point number for the price.")

                ingredients = []
                while True:
                    ingredient_input = input("Enter the ingredients of the item (separated by commas): ")
                    ingredients = [ingredient.strip() for ingredient in ingredient_input.split(",")]
                    if all(ingredient.replace(" ", "").isalpha() for ingredient in ingredients):
                        break
                    else:
                        print("Invalid input. Ingredients should only contain alphabetic characters and spaces.")

                item = Item(item_name, category, price, ingredients)

                all_items = all_item_data.load_info()
                all_items.append(item)
                all_item_data.save_info(all_items)
                print(f"Item '{item_name}' added successfully.")
            elif choice == "6":
                item_name = input("Enter the name of the item to remove: ")
                all_items = all_item_data.load_info()
                item_found = False
                for item in all_items:
                    if item.name == item_name:
                        all_items.remove(item)
                        item_found = True
                        break

                if item_found:
                    all_item_data.save_info(all_items)
                    print(f"Item '{item_name}' removed successfully.")
                else:
                    print(f"Item '{item_name}' not found.")
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")


    "The manage_menus method allows the user to manage menus." 
    "It includes functionality for assigning a waiter to a table," 
    "taking customer orders, and handling payment."
    @staticmethod
    def manage_menus(menu_data, table_data, order_data):
        def assign_waiter_and_take_order(table_number):
            tables = table_data.load_info()
            found_table = False
            for table in tables:
                if table.table_number == table_number:
                    found_table = True
                    if table.is_available:
                        waiter_name = input("Enter Your Name: ")
                        while not (waiter_name.replace(" ", "").isalpha() and len(waiter_name) >= 2):
                            print("Invalid input. Name must contain only alphabetic characters and have at least 2 characters.")
                            waiter_name = input("Enter Your Name: ")

                        print(f"Hello, {waiter_name}, I will be your waiter tonight. Are you ready to order?")
                        customer_response = input("Enter 'yes' or 'no': ")
                        while customer_response.lower() != "yes":
                            if customer_response == "0":
                                return  # Go back to the main menu
                            print("Okay, take your time.")
                            print(f"Hello, {waiter_name}, I will be your waiter tonight. Are you ready to order?")
                            customer_response = input("Enter 'yes' or 'no': ")

                        # Load the menu and display it to the user
                        menus = menu_data.load_info()
                        if menus:
                            print("Menu:")
                            for menu in menus:
                                print(f"{menu.category}, {menu.name}, {menu.price}, {menu.ingredients}\n")

                            # Gather customer order
                            customer_order = []
                            while True:
                                item_name = input("Enter the name of the item to order (0 to finish): ")
                                if item_name == "0":
                                    break
                                # Check if the item exists in the menu
                                found_item = None
                                for menu in menus:
                                    for item in menu.items:
                                        if item_name.lower() == item.name.lower():
                                            found_item = item
                                            break
                                    if found_item:
                                        break
                                if found_item:
                                    customer_order.append(found_item)
                                    continue
                                else:
                                    print("Sorry, we don't have this item in our menu. Please try again.")

                            # Create the order and assign it to the table
                            waiter = Waiter(waiter_name, "", "", "")
                            order = Order(waiter, customer_order)
                            table.assign_waiter(waiter_name)
                            table.take_order(order)
                            order_data.add_order(order)
                            table.is_available = False  # Mark the table as unavailable
                            table_data.save_info(tables)
                            print("\nOrder placed successfully.")
                            print("Your order:")
                            total_price = 0
                            for item in customer_order:
                                print(f"Name: {item.name}\tPrice: {item.price}\tIngredients: {', '.join(item.ingredients)}")
                                total_price += item.price
                            print("Total Price:", total_price, "NIS")
                            handle_payment(order)
                        else:
                            print("No menus found.")
                    else:
                        print("Table is already occupied.")
                    break
            if not found_table:
                print("Table not found.")

        def handle_payment(order):
            payment_method = input("Would you like to pay in Cash or Credit? Enter 'Cash' or 'Credit': ")
            while payment_method.lower() not in ['cash', 'credit']:
                print("Invalid payment method. Please try again.")
                payment_method = input("Would you like to pay in Cash or Credit? Enter 'Cash' or 'Credit': ")

            if payment_method.lower() == 'cash':
                while True :
                    try:
                        cash_given = float(input("Enter the amount of cash you will be paying: "))
                        break
                    except ValueError:
                        print ("Please use a numbber only .")

                while cash_given < order.total_price :
                    print("Please provide enough to cover the total price.")
                    cash_given = float(input("Enter the amount of cash you will be paying: "))
                # while not re.match(r"^(0[1-9]|1[0-2])/(20)\d{2}$", cash_given) ##neeed to think if do that on the same while and use "or" , or just do that loop in other while, for now its enough for us dont touch it hadas leave me that.
                    print ("Please Enter only numbers.")
  
                change = cash_given - order.total_price
                print("Payment successful.")
                print("Your Surplus:", change, "NIS")
                print ("If you have a moment, we would appreciate it if you could review each dish you ate, press 3 and then again 3")
                print ("Thank you very much. We would be delighted to see you again at our restaurant. Have a good day! ")
            else:
                credit_card_number = input("Enter your 16-digit credit card number: ")
                while len(credit_card_number) != 16 or not credit_card_number.isdigit():
                    print("Invalid credit card number. Please enter a valid 16-digit number.")
                    credit_card_number = input("Enter your 16-digit credit card number: ")
                expiry_date = input("Enter the expiry date of your credit card (MM/YYYY): ")
                while not re.match(r"^(0[1-9]|1[0-2])/20(2[4-9]|[3-9]\d)$", expiry_date):
                    print("Invalid expiry date. Please enter a valid date in the format MM/YYYY, after 01/2024.")
                    expiry_date = input("Enter the expiry date of your credit card (MM/YYYY): ")
                print("Payment successful.")
        
        def remove_ingredient_from_item(item):
                print(f"Current ingredients for '{item.name}': {', '.join(item.ingredients)}")
                remove_choice = input(f"Do you want to remove any ingredient from '{item.name}'? (yes/no): ")

                if remove_choice.lower() == "yes":
                    while True:
                        ingredient_to_remove = input("Enter the ingredient to remove (0 to finish): ")
                        if ingredient_to_remove == "0":
                            break

                        if ingredient_to_remove in item.ingredients:
                            item.ingredients.remove(ingredient_to_remove)
                            print(f"'{ingredient_to_remove}' has been removed from '{item.name}'.")
                        else:
                            print("Ingredient not found in the item.")
                else:
                    print("No ingredients removed.")
            
        while True:
            print("\n----- Menu Management -----")
            print("1. Assign Waiter to Table and Take Order")
            print("0. Go Back")
            choice = input("Enter your choice: ")

            if choice == "1":
                table_number = input("Enter the table number to assign a waiter: ")
                assign_waiter_and_take_order(table_number)
                return
            elif choice == "0":
                return  # Go back to the main menu
            else:
                print("Invalid choice. Please try again.")

    "Manages the tables in the restaurant by providing options to view tables, book a table," 
    "cancel a table reservation, and assign a waiter to a table." 
    "It interacts with the `table_data` object to load and save table information."
    @staticmethod
    def manage_table(table_data):
        tables = table_data.load_info()
        while True:
            print("\n----- Table Management -----")
            print("1. View Tables")
            print("2. Book a Table")
            print("3. Cancel a Table")
            print("4. Assign Waiter to Table")
            print("0. Go Back")
            choice = input("Enter your choice: ")

            if choice == "1":
                print("Tables:")
                for table in tables:
                    availability = "Available" if table.is_available else "Not Available"
                    print(f"Table Number: {table.table_number}, Availability: {availability}")

            elif choice == "2":
                table_number = input("Enter the table number to book: ")
                for table in tables:
                    if table.table_number == table_number:
                        if table.is_available:
                            table.is_available = False
                            table_data.save_info(tables)
                            print(f"Table {table_number} booked successfully.")
                        else:
                            print(f"Table {table_number} is already booked.")
                        break
                else:
                    print(f"Table {table_number} not found.")

            elif choice == "3":
                table_number = input("Enter the table number to cancel: ")
                for table in tables:
                    if table.table_number == table_number:
                        if not table.is_available:
                            table.is_available = True
                            table_data.save_info(tables)
                            print(f"Table {table_number} reservation canceled successfully.")
                        else:
                            print(f"Table {table_number} is not currently booked.")
                        break
                else:
                    print(f"Table {table_number} not found.")

            elif choice == "4":
                table_number = input("Enter the table number to assign a waiter: ")
                for table in tables:
                    if table.table_number == table_number:
                        if table.is_available:
                            waiter_name = input("Enter the waiter name to assign: ")
                            table.assign_waiter(waiter_name)
                            table_data.save_info(tables)
                            print(f"Waiter {waiter_name} assigned to Table {table_number}.")
                        else:
                            print(f"Table {table_number} is not currently available for assignment.")
                        break
                else:
                    print(f"Table {table_number} not found.")

            elif choice == "0":
                break

            else:
                print("Invalid choice. Please try again.")

    "The main function that serves as the entry point of the program." 
    "It creates instances of various data classes such as `EmployeeData`, `CustomerData`," 
    "`ItemData`, `MenuData`, `TableData`, and `OrderData`." 
    "It then presents a menu to the user and based on the user's choice," 
    "it calls different functions to manage employees, customers, items, menus," 
    "and tables, or exit the program."
    @staticmethod
    def main():
        employee_data = EmployeeData("Employee.csv")
        customer_data = CustomerData("Customer.csv")
        item_data = ItemData("Item.csv")
        menu_data = MenuData("Menu.csv")
        table_data = TableData("table.csv")
        order_data = OrderData("Order.csv")


        while True:
            Menu_system.main_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                Menu_system.manage_employees(employee_data)
            elif choice == "2":
                Menu_system.manage_customers(customer_data)
            elif choice == "3":
                Menu_system.manage_items(item_data)
            elif choice == "4":
                Menu_system.manage_menus(menu_data,table_data, order_data)
            elif choice == "5":
                Menu_system.manage_table(table_data)
            elif choice == "0":
                sys.exit("Goodbye, We will be happy to see you later (: ")
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu_system = Menu_system()
    menu_system.main()