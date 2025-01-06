# Create a Shape parent class and Circle and Square child classes, 
# each with its own method to calculate the area.
import math

class Shape:
    def __init__(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
    
    def area_circle(self):
        area=math.pi*(self.radius*2)
        print("Area of Circle is ",area)

class Square(Shape):
    def __init__(self,side):
        super().__init__()
        self.side=side
        
    def area_Square(self):
        area=self.side*self.side
        print("Area of Square is ",area)
    
C=Circle(5)
S=Square(5)

C.area_circle()
S.area_Square()
