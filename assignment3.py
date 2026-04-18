class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
class Employee (person):
    def __init__(self, name , age,emp_id,emp_salary):
        person.__init__(self,name,age)
        self.emp_id=emp_id
        self.emp_salary=emp_salary

class Manager(Employee):
     def __init__(self,name, age,emp_id,emp_salary,department):
         Employee.__init__(self,name, age,emp_id,emp_salary)
         self.department=department
    
     def display(self):
         print("Name= ",self.name)
         print("Age",self.age)
         print("ID ",self.emp_id)
         print("Salary= ",self.emp_salary)
         print("Position ",self.department)
         print("-" *20)

Emp1=Manager("suyash",28,"emp5868",56000000,"CTO")
Emp2=Manager("parth",28,"emp5869",56000000,"ASTROLOGER")
Emp3=Manager("rani",28,"emp5888",56000000,"DESIGN HEAD")
Emp4=Manager("raja",28,"emp5868","000000000000000000.1₹","CEO")
Emp1.display()
Emp2.display()
Emp3.display()
Emp4.display()
