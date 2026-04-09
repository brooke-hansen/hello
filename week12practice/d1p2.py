class Point:
    def __init__(self, xCoord, yCoord):
        self._x = xCoord
        self._y = yCoord
    
    def __str__(self):
        return f"Point: ({self._x}, {self._y})"
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    
    def __add__(self, other):
        newX = self._x + other.getX()
        newY = self._y + other.getY()
        return Point(newX, newY)
#MAKE SURE YOU ARE RETURNING AN OBJECT OF THE RIGHT TYPE    

p1 = Point(3,4)
p2 = Point(7,12)

p3 = p1 + p2
#p3 = p1.__add__(p2)
p4 = Point(1,1)

p5 = p3 + p4

print(p3) #(3+7, 4+12) = (10, 16)
print(p5)