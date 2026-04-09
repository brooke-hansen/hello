
import math

class Planet:
    def __init__(self, name, radius, mass, distance):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._distance = distance
    
    def get_name(self):
        return self._name
    def get_radius(self):
        return self._radius
    def get_mass(self):
        return self._mass
    def get_distance(self):
        return self._distance
    def get_volume(self):
        volume = 4/3 * math.pi * self._radius ** 3
        return volume
    def get_density(self):
        return self.mass / self.get_volume()
    
    def setName(self, new_name):
        self._name = new_name
    
    def __str__(self):
        msg = f"Hello from planet {self.get_name()}"
        return msg
    

"""
print(planet1.get_name())

#add code here to change the name from the console

userinput = input("Do you want to change the planets anme? y/n ")
if userinput == "y":
    usernewname = input("Pick a new name ")
    planet1.setName(usernewname)

print(planet1.get_name())

#print(planet2.get_name())
#print(planet1.get_volume())
"""

#planet1.setName("x26")

#print(planet1.get_name())

class Star:
    def __init__(self, name):
        self._name = name
    
    def getName(self):
        return self._name
    
    def setName(self, new_name):
        self._name = new_name
    
    def __str__(self):
        msg = f"This is the star: {self._name}"
        return msg
    

class PlanetarySystem:
    def __init__(self, name, star):
        self._name = name
        self._star = star
        self._planetList = []

    def addPlanet(self, planet):
        self._planetList.append(planet)
    
    def showPlanets(self):
        for planet in self._planetList:
            print(planet)
    
    def changeStarName(self, NewName):
        self._star.setName(NewName)
    
    def changePlanetName(self, changePlanet, newPlanetName):
        count = 0
        if (changePlanet in self._planetList):
            count = 0
            for i in range(len(self._planetList)):
                if (self._planetList[i] == changePlanet):
                    break
                else:
                    count += 1
        self._planetList[count].setName(newPlanetName)


"""
sun = Star("Sun")
print(sun)
"""

planet1 = Planet("x25", 45, 198, 1000)
planet2 = Planet("Gornar", 12, 23, 456)

"""
print(planet1)
print(planet2)
"""

star1 = Star("Gold150")

solarSystem= PlanetarySystem("Solar System", Star("Sun"))

#print(f"This star is {star1.getName()}")

print(solarSystem._star.getName())

solarSystem.changeStarName("Sol")

print(solarSystem._star.getName())



solarSystem.addPlanet(Planet("x25", 45, 198, 1000))
solarSystem.addPlanet(Planet("Gornar", 12, 23, 456))

solarSystem.showPlanets()

solarSystem.changePlanetName('x25', 'x26')
print("----------------")

solarSystem.showPlanets()
print("----------------")

#sun.setName("Sol")
