import csv
from objects.Employee import Employee

"Implementation of the EmployeeData class that handles operations related to employee data." 
"It provides methods to save, remove, load, and add worker information to a CSV file." 
"The class also follows the Singleton design pattern to ensure that there is only one" 
"instance of EmployeeData throughout the program execution"

class EmployeeData:
    _instance = None

    @staticmethod
    def get_instance(file_emp):
        if EmployeeData._instance is None:
            EmployeeData._instance = EmployeeData(file_emp)
        return EmployeeData._instance
    

    def __init__(self, file_emp):
        if EmployeeData._instance is not None:
            raise Exception("Singleton class should not be instantiated directly.")
        self.file_emp = file_emp

    def save_info(self, employees):
        with open(self.file_emp, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email", "Phone", "Role", "Salary"])
            for employee in employees:
                writer.writerow([employee.id, employee.name, employee.email, employee.phone, employee.role, employee.salary])


    def remove_info(self, employee_id):
        employees = self.load_info()
        updated_employees = [employee for employee in employees if employee.id != employee_id]
        if len(updated_employees) == len(employees):
            print("Employee not found.")
        else:
            with open(self.file_emp, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Email", "Phone", "Role", "Salary"])
                for employee in updated_employees:
                    writer.writerow([employee.id, employee.name, employee.email, employee.phone, employee.role, employee.salary])
            print("Employee removed successfully.")

    def load_info(self):
        employees = []
        with open(self.file_emp, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                employees.append(Employee(row[0], row[1], row[2], row[3], row[4], row[5]))
        return employees
    

    def add_employee(self, employee):
        employees = self.load_info()
        
        # Check if the employee ID already exists
        if any(emp.id == employee.id for emp in employees):
            print("ID exists, please enter another ID.")
            return
        
        employees.append(employee)
        
        with open(self.file_emp, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email", "Phone", "Role", "Salary"])
            for emp in employees:
                writer.writerow([emp.id, emp.name, emp.email, emp.phone, emp.role, emp.salary])
        
