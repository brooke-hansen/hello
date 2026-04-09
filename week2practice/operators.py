import math
import decimal


#sum = 16 + 18
#print(sum)
#product = 24 * 45
#print(product)
#subtraction = product - sum
#print(subtraction)
#division = sum / 2
#print(division)

# 7.5 Mod 2
#modulus = division % 2
#print(modulus)
#floordiv = 10 // 3
#print(floordiv)

# Type casting to a different data type.
#floordiv2 = int(10/3)
#print(floordiv2)

#using math functions
#pie = round(math.pi)
#print(pie)

#example = 5 ** 2: this means 5^2 in Python

#radius = 7
#pi r-squared
#area_of_circle = math.pi * (radius ** 2)
#print(area_of_circle)
#4/3 pi r-cubed

# Q6 volume of a sphere
#volume_of_sphere = (4/3) * math.pi * (radius ** 3)
#print(f"If the radius = {radius} the area must be {round(area_of_circle,1)} and the volume must be {round(volume_of_sphere)}")

#Q1 farm
#chicken_legs = int(input("How many chickens do you have on your farm? "))
#cow_legs = int(input("How many cows do you have on your farm? "))
#pig_legs = int(input("How many pigs do you have on your farm? "))
#sum_of_legs = (chicken_legs * 2) + (cow_legs * 4) + (pig_legs * 4)
#print(f"You have a total of {sum_of_legs} livestock legs on your farm")

#Q2 bball
#two_point = float(input("How many two pointers were scored? "))
#three_point = float(input("How many three pointers were scored? "))
#sum_of_scores = (two_point * 2) + (three_point * 3)
#print(f"The final score must've been {sum_of_scores}")

#Q3 area of trapezoid
#value_a = float(input("What is the length of the short base? "))
#value_b = float(input("What is the length of the long base? "))
#value_h = float(input("What is the length of the height? "))
#area_of_trap = ((value_a + value_b) / 2) * (value_h)
#print(f"The area of the trapezoid is {area_of_trap}")

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
#value_r = float(input("What is the measurement of the radius? "))
#value_h = float(input("What is the length of the height? "))
#volume = math.pi * (((value_r ** 2 ) * value_h) / 3)
#print(f"The volume of your cone is {volume}")

#Q8 area of a semi circle
#value_r = float(input("What is the radius of the semi-circle? "))
#area = math.pi * (1/2) * (value_r ** 2)
#print(f"The area of the semi-circle is {area} cm^2")



#CHALLENGE 1
#ask user for input for age (can include decimals)
human_age = float(input("Enter age: "))
#convert human_age to dog_age
dog_age = human_age * 7
#break into years, months, days
years = int(dog_age)
#subtract years to isolate decimals (months -> days)
remain_year = dog_age - years
#isolate decimals and convert into months
months_total = remain_year * 12
months = int(months_total)
#isolate decimals and convert into days
remain_month = months_total - months
days = int(remain_month * 30)
#round result of dog_age to first two decimals
print(f"That is {dog_age:.2f} dog years.")
#string dog age with years, months, and days
print(f"Your age as a dog is {years} years, {months} months, and {days} days old!")

#convert human age to cat age
cat_age = human_age * 9
#ignore decimal from cat years
cyears = int(cat_age)
#isolate decimal from cat years and convert to months
locyears = cat_age - cyears
cmonths_total = locyears * 12
#ignore decimal from cat months
cmonths = int(cmonths_total)
#isolate decimal from cat months and convert to days
locmonths = cmonths_total - cmonths
cdays = int(locmonths * 30)
#round result of cat_age to first two decimals
print(f"That is {cat_age:.2f} cat years.")
#string cat age together in years, months, and days
print(f"Your age as a cat is {cyears} years, {cmonths} months, and {cdays} days old!")

#convert human_age to horse_age
horse_age = 3 * ((((human_age ** 2) - 47) / 7) + 12)
hyears = int(horse_age)
lohyears = horse_age - hyears
hmonths_total = lohyears * 12
hmonths = int(hmonths_total)
lohmonths = hmonths_total - hmonths
hdays = int(lohmonths * 30)
print(f"That is {horse_age:.4f} horse years.")
print(f"Your age as a horse is {hyears} years, {hmonths} months, and {hdays} days old!")

