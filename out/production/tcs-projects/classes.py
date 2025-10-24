class Company():

    def __init__(self,employee_count, manager_name, ceo_name):
        self.employee_count = employee_count
        self.manager_name = manager_name
        self.ceo_name = ceo_name

    def __str__(self):
        return f"Employees: {self.employee_count} Manager: {self.manager_name} CEO: {self.ceo_name}"

    def get_employee_count(self):
        return self.employee_count
    
    def set_employee_count(self, employees):
        self.employee_count = employees


"""facebook = Company(100, "bob", "Mark Zuckerberg")
print(facebook.employee_count)
print(facebook.get_employee_count())

print(facebook)"""

class Person():

    def __init__(self, height, weight, haircolor, ):
        self.height = height
        self.weight = weight
        self.haircolor = haircolor

    def get_height(self):
        return self.height
    
    def set_height(self, new_height):
        self.height = new_height

    def get_haircut(self, new_hairdo):
        self.haircolor = new_hairdo


alice = Person("5'9", 'x', 'brown')
alice.set_height("6'0")
print(alice.get_height())
