from objects.Person import Person

"The Employee class extends the functionality of the Person class." 
"It serves as a blueprint for creating employee objects and inherits" 
"the attributes and behaviors defined in the Person class while adding" 
"the additional attributes role and salary specific to employees."

class Employee(Person):
  
  def __init__(self, id, name, email, phone, role, salary):
    super().__init__(id, name, email, phone)
    self.role = role
    self.salary = salary