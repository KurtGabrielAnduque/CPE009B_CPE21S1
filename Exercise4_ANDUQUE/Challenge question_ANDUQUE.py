class Person():
    def __init__(self, name, pre, mid, fin):
        self.__name = name
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin
        


class Student1(Person):
    
    def Grade(self):
        return (self._Person__pre + self._Person__mid + self._Person__fin)/3
        
    def Display_Grade(self):
        print(f'Student name: {self._Person__name}')
        print(f'Student prelim Grade: {self._Person__pre}')
        print(f'Student midterm Grade: {self._Person__pre}')
        print(f'Student finals Grade: {self._Person__pre}') 
        print(f'Student Average grade: {round(self.Grade(),2)}')
        if self.Grade() >= 50:
            return "Situation: PASS"
        else:
            return "Situation: Fail"
    
class Student2(Person):
    def Grade(self):
        return (self._Person__pre + self._Person__mid + self._Person__fin)/3    
    def Display_Grade(self):
        print(f'Student name: {self._Person__name}')
        print(f'Student prelim Grade: {self._Person__pre}')
        print(f'Student midterm Grade: {self._Person__pre}')
        print(f'Student finals Grade: {self._Person__pre}') 
        print(f'Student Average grade: {round(self.Grade(),2)}')
        if self.Grade() >= 50:
            return "Situation: PASS"
        else:
            return "Situation: Fail"
        

class Student3(Person):
    
    def Grade(self):
        return (self._Person__pre + self._Person__mid + self._Person__fin)/3
    def Display_Grade(self):
        
        print(f'Student name: {self._Person__name}')
        print(f'Student prelim Grade: {self._Person__pre}')
        print(f'Student midterm Grade: {self._Person__pre}')
        print(f'Student finals Grade: {self._Person__pre}') 
        print(f'Student Average grade: {round(self.Grade(),2)}')
        if self.Grade() >= 50:
            return "Situation: PASS"
        else:
            return "Situation: Fail"
    



Student_1 = Student1("Kurt", 20, 20, 30)
print(Student_1.Display_Grade())
print("\n")

Student_2 = Student2("Christian",50,50,50)
print(Student_2.Display_Grade())
print("\n")

Student_3 = Student3("Hendricks",100,100,100)
print(Student_3.Display_Grade())


