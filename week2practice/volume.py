import math

#Q4 volume of a pyramid
#base_edge = float(input("What is length of the base edge? "))
#height_edge = float(input("What is the height? "))
#volume = ((((base_edge) ** 2) + (height_edge)) / 3)
#print(f"The volume of this pyramid is {volume}")

#Q5 volume of a cylinder
#value_r = float(input("What is the measurement of the radius? "))
#value_h = float(input("What is the length of the height? "))
#volume = math.pi * (value_r ** 2) * value_h
#print(f"The volume of your cylinder is {round(volume)}")

#Q7 volume of a cone
value_r = float(input("What is the measurement of the radius? "))
value_h = float(input("What is the length of the height? "))
volume = math.pi * (((value_r ** 2 ) * value_h) / 3)

print(f"The volume of your cone is {volume}")