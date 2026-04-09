#Q2 
class Duck:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def getcolor(self):
        return self.color
    
    def setcolor(self, new_color):
        self.color = new_color
    
    def speak(self):
        print("Quack!")
    
    def __str__(self):
        msg = f"{self.name} is a {self.color} duck!"
        return msg

class Pond:
    def __init__(self, name, duck_count = 0):
        self.name = name
        self.duckList = []
        self.duck_count = duck_count
    
    def add_duck(self, duck):
        self.duckList.append(duck)
        self.duck_count += 1
    
    def duck_speak(self):
        for duck in self.duckList:
            Duck.speak(self)


    def __str__(self):
        msg = f"Welcome to {self.name}, home to {self.duck_count} ducks!"
        return msg


pond1 = Pond("Mill Pond")
pond2 = Pond("Any Pond")

duck1 = Duck("Mallard", "Blue")
duck2 = Duck("Mellerd", "Yellow")
duck3 = Duck("Millird", "green")

#duck_lyst = [duck1, duck2, duck3]
#pond2.add_duck(duck_lyst)

pond2.add_duck(duck1)
pond2.add_duck(duck2)
pond2.add_duck(duck3)

pond2.duck_speak()

print(duck3)