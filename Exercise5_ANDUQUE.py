#Exercise5

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

class Student(Person):
    def traits(self):
        return "studying, dancing,singing,playing"
    
class Teacher(Person):
    def traits(self):
        return "socializing, teaching, participating"
    

Student1 = Student("Kurt",20)
Teacher1 =Teacher("Ma'am",41)

print(f'As a Student, I do {Student1.traits()}')
print(f'As a Teacher, I do {Teacher1.traits()}')



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
class Plane_ticket_child(Person):
    def ticket_cost(self):
        return f'{self.name} your ticket is worth 1000 pesos'
    
class Plane_ticket_adult(Person):
    def ticket_cost(self):
        return f'{self.name} your ticket is worth 2000 pesos'

class Plane_ticket_senior(Person):
    def ticket_cost(self):
        return f'{self.name} your ticket is worth 1500 pesos'
    
class Plane_ticket_youth(Person):
    def ticket_cost(self):
        return f'{self.name} your ticket is worth 1200 pesos'


print("\n")
print("\n")
print("\n")
while True:
    
    try:
        
        print("================= BOOK A PLANE TICKET =================")
        print("\n")
        age_input = int(input("Enter age: "))
        name_input = input("Enter name: ")
    
    
        if age_input >= 0 and age_input <= 14:
            ChildTicket = Plane_ticket_child(name_input, age_input)
            print(ChildTicket.ticket_cost())
            break
        
        
        elif age_input >=15 and age_input <=24:
            YouthTicket = Plane_ticket_youth(name_input, age_input)
            print(YouthTicket.ticket_cost())
            break
        
        
        elif age_input >= 25 and age_input <= 64:
            AdultTicket = Plane_ticket_adult(name_input, age_input)
            print(AdultTicket.ticket_cost())
            break
        
        
        elif age_input >= 65:
            SeniorTicket = Plane_ticket_senior(name_input, age_input)
            print(SeniorTicket.ticket_cost())
            break
        
    except ValueError:
        print("Pls enter a number in age!!!")
