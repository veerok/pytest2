# Реализовать классы: фигура, круг, прямоугольник, квадрат. Классы должны предоставлять методы: 
# получение центра
# получение периметра
# получение площади

import math
class Figure:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getCenter(self):
        return (self.x, self.y)
    
    
class Circle(Figure):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r
        
    def getPerimeter(self):    
        p = 2 * math.pi * self.r
        return p
    
    def getSquare(self):
        s = math.pi * self.r**2 
        return s
    
class Rectangle(Figure):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def getCenter(self):
        return (self.x, self.y)
        
    def getPerimeter(self):    
        p = 2 * (self.a + self.b)
        return p
    
    def getSquare(self):
        s = self.a * self.b
        return s
    
class Quadrate(Rectangle):
    def __init__(self, x, y, a, b, c):
        super().__init__(x, y, a, b)
        self.c = c
        
    def getPerimeter(self):    
        p = 4 * self.c
        return p
    
    def getSquare(self):
        s = self.c * self.c
        return s

r = Circle(1, 3, 3).getCenter()
print(r)    
r = Rectangle(1, 4, 3, 4).getCenter()
print(r)
r = Quadrate(1, 4, 3, 4, 5).getCenter()
print(r)   

r = Circle(1, 3, 3).getPerimeter()
print(r) 
r = Rectangle(1, 3, 3, 9).getPerimeter()
print(r) 
r = Quadrate(1, 3, 3, 7, 8).getPerimeter()
print(r) 

r = Circle(1, 3, 3).getSquare()
print(r) 
r = Rectangle(1, 3, 3, 4).getSquare()
print(r) 
r = Quadrate(1, 3, 3, 7, 8).getSquare()
print(r) 