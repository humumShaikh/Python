class Vehicle:

    def __init__(self , make , model , year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print("Make : " , self.make)
        print("Model : " , self.model)
        print("Year : " , self.year)

class Car(Vehicle):

    def __init__(self , make , model , year , num_doors):
        super().__init__(make , model , year)
        self.num_doors = num_doors
    
    def display_info(self):
        print("Make : " , self.make)
        print("Model : " , self.model)
        print("Year : " , self.year)
        print("Num Doors : " , self.num_doors)


v =  Vehicle("Rover" , "SUV" , 2012)
c = Car("Prius" , "Sedan" , 2020 , 4)
v.display_info()
c.display_info()