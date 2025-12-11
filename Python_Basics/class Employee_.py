class Employee:

    def __init__(self , name , empid , salary):
        self.name = name
        self.empid = empid
        self.salary = salary
    
    def display_info(self):
        print("Name : " , self.name)
        print("EMPID : " , self.empid)
        print("Salary : " , self.salary)


class Manager(Employee):

    def __init__(self , name , empid , salary):
        super().__init__(name , empid , salary)
        self.employees = []
    
    def display_info(self):
        print("Name : " , self.name)
        print("EMPID : " , self.empid)
        print("Salary : " , self.salary)
    
    def add_employee(self , emp):
        self.employees.append(emp)
    
    def show_managed_employees(self):
        for e in self.employees:
            print("EMP NAME : " , e)

e = Employee("Dev" , 7 , 25000)
e.display_info()

m = Manager("Humum" , 11 , 55000)
m.display_info()

m.add_employee("Sarvesh")
m.add_employee("Ramesh")
m.add_employee("Suresh")

m.show_managed_employees()