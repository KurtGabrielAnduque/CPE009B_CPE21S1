class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def Area(self):
        return f'{self.length*self.width} cm'

    def Perimeter(self):
        return f'{2*(self.width+self.length)} cm'

while True:
    try:

        user_length = float(input("Enter the length of the Rectangle: "))
        user_width = float(input("Enter the width of the Rectangle: "))
        break

    except ValueError:
        print("Enter number only!!!")

user_Rectangle = Rectangle(user_length,user_width)

print(user_Rectangle.Area())
print(user_Rectangle.Perimeter())