
import csv
from objects.Customer import Customer

class CustomerData:
    "Handling customer data stored in a CSV file"
    def __init__(self, file_cust):
        self.file_cust = file_cust

    def save_info(self, customers):
        "Saving customer details to a specified file in CSV format"
        "with each customer's attributes written correctly in the file."
        # existing_customers = self.load_info()  # Load existing customers
        # existing_customers.extend(customers)  # Append new customers

        with open(self.file_cust, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email", "Phone"])
            for customer in customers:
                writer.writerow([customer.id, customer.name, customer.email, customer.phone])
    

    def remove_info(self, customer_id):
        "Removes the client with the specified ID from the client details stored in the file" 
        "Update the file by writing the updated customer information to it"
        customers = self.load_info()
        updated_customers =  [customer for customer in customers if customer.id != customer_id]
        if len(updated_customers) == len(customers):
            print("Customer not found.")
        else:
            with open(self.file_cust, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Email", "Phone"])
                for customer in updated_customers:
                    writer.writerow([customer.id, customer.name, customer.email, customer.phone])
            print("Customer removed successfully.")



    def load_info(self):
        "Loading customer information from the file, creates customer objects" 
        "The resulting list of client objects is then returned"
        customers = []
        with open(self.file_cust, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                customers.append(Customer(row[0], row[1], row[2], row[3]))
        return customers
    

    def add_customer(self, customer):
        customers = self.load_info()
        
        # Check if the employee ID already exists
        if any(cust.id == customer.id for cust in customers):
            print("ID exists, please enter another ID.")
            return
        
        customers.append(customer)
        
        with open(self.file_cust, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email", "Phone"])
            for cust in customers:
                writer.writerow([cust.id, cust.name, cust.email, cust.phone])
        












# import csv
# from objects.Customer import Customer

# class CustomerData:
#     "Handling customer data stored in a CSV file"
#     def __init__(self, file_cust):
#         self.file_cust = file_cust

#     def save_info(self, customers):
#         "Saving customer details to a specified file in CSV format"
#         "with each customer's attributes written correctly in the file."
#         existing_customers = self.load_info()  # Load existing customers
#         existing_customers.extend(customers)  # Append new customers

#         with open(self.file_cust, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["ID", "Name", "Email", "Phone"])
#             for customer in existing_customers:
#                 writer.writerow([customer.id, customer.name, customer.email, customer.phone])
    
#     def remove_info(self, customer_id):
#         "Removes the client with the specified ID from the client details stored in the file" 
#         "Update the file by writing the updated customer information to it"
#         customers = self.load_info()
#         updated_customers = []

#         customer_exists = False

#         for customer in customers:
#             if customer.id == customer_id:
#                 customer_exists = True
#             else:
#                 updated_customers.append(customer)

#         if customer_exists:
#             with open(self.file_cust, 'w', newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerow(["ID", "Name", "Email", "Phone"])
#                 for customer in updated_customers:
#                     writer.writerow([customer.id, customer.name, customer.email, customer.phone])
#             print("Customer removed successfully.")
#         else:
#             print("Customer not found.")


#     def load_info(self):
#         "Loading customer information from the file, creates customer objects" 
#         "The resulting list of client objects is then returned"
#         customers = []
#         with open(self.file_cust, 'r', newline='') as file:
#             reader = csv.reader(file)
#             next(reader)  # Skip the header row
#             for row in reader:
#                 customers.append(Customer(row[0], row[1], row[2], row[3]))
#         return customers
    

#     def add_customer(self, customer):
#         customers = self.load_info()
#         customers.append(customer)
#         with open(self.file_emp, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["ID", "Name", "Email", "Phone"])
#             for cust in customers:
#                 writer.writerow([cust.id, cust.name, cust.email, cust.phone, cust.role, cust.salary])

