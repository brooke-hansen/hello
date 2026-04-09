'''
#also just a bad way to organize code
#make a parameter optional by giving it a default value
def greeting(name, age = "unknown"):
    if age == "unknown":
        print(f"hello {name}! How old are you?")    
    else:
        print(f"hello {name}! It's cool being {age} years old!")

greeting("Ashley", 35)

#def greeting(name):
    #print(f"hello {name}! How old are you? ")

greeting("ashley")

greeting("Dexter", 8)
'''
'''
def fctn1(num):
    return num + 1

x = 3
y = fctn1(x)

print(x)
print(y)
'''
'''immutable vs mutable
def fctn2(lyst:list):
    lyst2 = []
    for element in lyst:
        lyst2.append(element)
    lyst.append('a')

lyst1 = [1,2,3]
lyst2 = lyst1

lyst2.append(4)

print(lyst1)

fctn2(lyst1)
print(lyst1)
'''
'''
x = 3
y = x

y += 1
print(x)
'''