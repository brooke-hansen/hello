#Q3 create a function is_boiling to determine if temp is boiling or not (in C & F)
def is_boiling(temp):
    unit = temp[-1]
    value = float(temp[:-1])

    if unit == "F" or unit == "f":
        return value > 212
    elif unit == "C" or unit =="c":
        return value > 100
    else:
        return "Invalid temperature measurement"
    
print(is_boiling("980F"))