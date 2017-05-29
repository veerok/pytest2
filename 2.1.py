# Реализовать классы: фигура, круг, прямоугольник, квадрат. Классы должны предоставлять методы: 
# получение центра
# получение периметра
# получение площади

import math
class Figure:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getCenter(x,y):
        return (x,y)
    
    
class Circle(Figure):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r
        
    def getPerimeter(r):    
        p = 2 * math.pi * r
        return p
    
    def getSquare(r):
        s = math.pi * r**2 
        return s
    
class Rectangle(Figure):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b
    def getCenter(x,y):
        return (x,y)
        
    def getPerimeter(a,b):    
        p = 2 * (a + b)
        return p
    
    def getSquare(a,b):
        s = a * b
        return s
    
class Quadrate(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
        
    def getPerimeter(c):    
        p = 4 * c
        return p
    
    def getSquare(c):
        s = c * c
        return s

r = Circle.getCenter(1,2)
print(r)    
r = Rectangle.getCenter(1,3)
print(r)   
r = Quadrate.getCenter(1,5)
print(r)   

r = Circle.getSquare(5)
print(r)
r = Rectangle.getSquare(1,4)
print(r)
r = Quadrate.getSquare(3)
print(r)    

r = Circle.getPerimeter(2)
print(r)
r = Rectangle.getPerimeter(2,5)
print(r)
r = Quadrate.getPerimeter(1)
print(r)   
