class Student:                                    #class named Student

    def __init__(self , name , age , id):            #class constructor
        self.name = name                             #self is the 'this' pointer here in python         
        self.age = age
        self.id = id

    def display_info(self):
        print("Name : " , self.name)
        print("Age : " , self.age)
        print("ID : " , self.id)

    def is_eligible_to_vote(self):
        if(self.age >= 18):
            return True
        else:
            return False



s1 =  Student("Humum" , 17 , 11)

s1.display_info()

print("Voting Eligibility : " , s1.is_eligible_to_vote())
