class RegularPolygon():
    def __init__(self,side):
        self.side = side
        
    
class Square(RegularPolygon):

    def area(self):
        return self.side * self.side
    
    
class EquilateralTriangle(RegularPolygon):

    def area(self):
        return self.side * self.side * 0.433
    
    

Square_object = Square(3)
Triange_object = EquilateralTriangle(3)

print(Square_object.area())
print(Triange_object.area())