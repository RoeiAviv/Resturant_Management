from objects.Person import Person

"The Customer class extends the functionality of the Person class." 
"It serves as a blueprint for creating customer objects and inherits" 
"the attributes and behaviors defined in the Person class."

class Customer(Person):

  def __init__(self, id, name, email, phone):
    super().__init__(id, name, email, phone)