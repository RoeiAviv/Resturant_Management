import unittest
from objects.Employee import Employee
import os
from data.EmployeeData import EmployeeData

class EmployeeTest(unittest.TestCase):
    
    def test_employee_initialization(self):
        employee = Employee('205025246', 'Omri', 'Manager', 5000, 'Omri@gmail.com', '054-3589021')
        self.assertEqual(employee.id, '205025246')
        self.assertEqual(employee.name, 'Omri')
        self.assertEqual(employee.role, 'Manager')
        self.assertEqual(employee.salary, 5000)
        self.assertEqual(employee.email, 'Omri@gmail.com')
        self.assertEqual(employee.phone, '054-3589021')

class EmployeeDataTest(unittest.TestCase):
    def setUp(self):
        self.employee_data = EmployeeData('test_employee.csv')

    def tearDown(self):
        if os.path.exists('test_employee.csv'):
            os.remove('test_employee.csv')

    def test_save_and_load_info(self):
        employees = [
            Employee('322525246', 'Roei', 'Manager', '35000', 'roy4050@gmail.com', '052-5523698'),
            Employee('214125515', 'Hadas', 'Waiter', '2200', 'Hadas424@gmail.com', '052-3523627'),
            Employee('415253151', 'Eden', 'Chef', '19500', 'Eden221@gmail.com', '052-1511316'),
            Employee('153876435', 'Shlomi', 'Guard', '9500', 'Shlomi54@gmail.com', '054-1515151'),
            Employee('178512551', 'Nir', 'Barmen', '11000', 'Nir34@gmail.com', '052-2451875'),
            Employee('325231661', 'Lian', 'Host', '10000', 'Lian25@gmail.com', '052-5522685')]
 
        emp_data = EmployeeData('employee.csv')
        emp_data.save_info(employees)
        emp_data.remove_employee('Shlomi')
        self.employee_data.save_info(employees)

        loaded_employees = self.employee_data.load_info()
        self.assertEqual(len(loaded_employees), len(employees))
        for i in range(len(employees)):
            self.assertEqual(loaded_employees[i].id, employees[i].id)
            self.assertEqual(loaded_employees[i].name, employees[i].name)
            self.assertEqual(loaded_employees[i].role, employees[i].role)
            self.assertEqual(loaded_employees[i].salary, employees[i].salary)
            self.assertEqual(loaded_employees[i].email, employees[i].email)
            self.assertEqual(loaded_employees[i].phone, employees[i].phone)

    def test_remove_employee(self):
       employees = [
            Employee('322525246', 'Roei', 'Manager', '35000', 'roy4050@gmail.com', '052-5523698'),
            Employee('214125515', 'Hadas', 'Waiter', '2200', 'Hadas424@gmail.com', '052-3523627'),
            Employee('415253151', 'Eden', 'Chef', '19500', 'Eden221@gmail.com', '052-1511316'),
            Employee('153876435', 'Shlomi', 'Guard', '9500', 'Shlomi54@gmail.com', '054-1515151'),
            Employee('178512551', 'Nir', 'Barmen', '11000', 'Nir34@gmail.com', '052-2451875'),
            Employee('325231661', 'Lian', 'Host', '10000', 'Lian25@gmail.com', '052-5522685')]

       self.employee_data.save_info(employees)

       self.employee_data.remove_employee('Shlomi')
       loaded_employees = self.employee_data.load_info()
       employee_names = [emp.name for emp in loaded_employees]
       self.assertNotIn('Shlomi', employee_names)

    def test_all_employees(self):
        employees = [
            Employee('322525246', 'Roei', 'Manager', '35000', 'roy4050@gmail.com', '052-5523698'),
            Employee('214125515', 'Hadas', 'Waiter', '2200', 'Hadas424@gmail.com', '052-3523627'),
            Employee('415253151', 'Eden', 'Chef', '19500', 'Eden221@gmail.com', '052-1511316'),
            Employee('153876435', 'Shlomi', 'Guard', '9500', 'Shlomi54@gmail.com', '054-1515151'),
            Employee('178512551', 'Nir', 'Barmen', '11000', 'Nir34@gmail.com', '052-2451875'),
            Employee('325231661', 'Lian', 'Host', '10000', 'Lian25@gmail.com', '052-5522685')]

        self.employee_data.save_info(employees)
        all_employees = self.employee_data.all_employees()
        self.assertEqual(len(all_employees), len(employees))
        for i in range(len(employees)):
            self.assertEqual(all_employees[i].id, employees[i].id)
            self.assertEqual(all_employees[i].name, employees[i].name)
            self.assertEqual(all_employees[i].role, employees[i].role)
            self.assertEqual(all_employees[i].salary, employees[i].salary)
            self.assertEqual(all_employees[i].email, employees[i].email)
            self.assertEqual(all_employees[i].phone, employees[i].phone)
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)