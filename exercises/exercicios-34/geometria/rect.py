import math

class Rect:
    def __init__(self, size_h, size_b):
        self.size_h = size_h
        self.size_b = size_b

    def rect_area(self):
        return self.size_h * self.size_b

class Circle:
    def __init__(self, raio):
        self.raio = raio
    
    def circle_area(self):
        return math.pi * self.raio ** 2
    
    def cicle_diameter(self):
        return self.raio * 2

circle = Circle(3)

print(circle.circle_area())