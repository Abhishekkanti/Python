
#Single Inheritance

class Employee:
    def __init__(self,name,Id):
        self.name = name
        self.Id = Id
     
    def intro(self):
        print(f"Hello I am {self.name}")
        print(f"My I'd is {self.Id}")
        
class Dept(Employee):
    def __init__(self,name,Id,salary,role):
        self.salary = salary
        self.role = role
        Employee.__init__(self,name,Id)
        
    def Details(self):
        print(f"Hello I am {self.name}.!!!")
        print(f"My I'd is {self.Id} and I work as a {self.role} on {self.salary} salary.")
        

stephen = Dept("stephen",54,45000,'intern')
stephen.Details()
    