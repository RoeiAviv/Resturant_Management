from objects.Employee import Employee
from data.EmployeeData import EmployeeData

"The Manager class represents a manager, who is a type of employee." 
"It provides methods to hire and fire employees, as well as edit their roles and salaries." 
"The functionality relies on an instance of the EmployeeData class to load and save" 
"employee information."

class Manager(Employee):
    def __init__(self, id, name, email, phone):
        super().__init__(id, name, "", 0, email, phone)

    def hire_employee(self, employee_data, employee):
        employees = employee_data.load_info()
        employees.append(employee)
        employee_data.save_info(employees)
        print(f"Employee {employee.name} has been hired.")

    def fire_employee(self, employee_data, employee_id):
        employees = employee_data.load_info()
        for employee in employees:
            if employee.id == employee_id:
                employees.remove(employee)
                break
        else:
            print(f"Employee with ID {employee_id} not found.")
            return

        employee_data.save_info(employees)
        print(f"Employee with ID {employee_id} has been fired.")

    def edit_employee_role(self, employee_data, employee_id, new_role):
        employees = employee_data.load_info()
        for employee in employees:
            if employee.id == employee_id:
                employee.role = new_role
                employee_data.save_info(employees)
                print(f"Employee with ID {employee_id} role has been updated.")
                break
        else:
            print(f"Employee with ID {employee_id} not found.")

    def edit_employee_salary(self, employee_data, employee_id, new_salary):
        employees = employee_data.load_info()
        for employee in employees:
            if employee.id == employee_id:
                employee.salary = new_salary
                employee_data.save_info(employees)
                print(f"Employee with ID {employee_id} salary has been updated.")
                break
        else:
            print(f"Employee with ID {employee_id} not found.")


# manager = Manager("314753427", "Roei Aviv", "roy40@gmail.com", "054-8199932")
# employee_data = EmployeeData("Employee.csv")

# employee1 = Employee("313451561", "Anna Zak", "", 0, "Anna@gmail.com", "052-5381648")

# manager.hire_employee(employee_data, employee1)

# employee_id = "214146151"
# manager.fire_employee(employee_data, employee_id)

# employee_id = "214125515"
# new_role = "Washing dishes"
# manager.edit_employee_role(employee_data, employee_id, new_role)

# employee_id = "214125515"
# new_salary = 3100
# manager.edit_employee_salary(employee_data, employee_id, new_salary)
