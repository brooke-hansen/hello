#Q2 create a function is_fever that determines if temp is considered a fever
def is_fever(temp):
    unit = temp[-1]
    value = float(temp[:-1])

    if unit == "F" or unit == "f":
        return value > 98.6
    elif unit == "C" or unit == "c":
        return value > 37
    else:
        return "Invalid temperature measurement"

user_temp = input("Enter your temperature: ")
print(is_fever(user_temp))