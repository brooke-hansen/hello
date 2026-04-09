#Q7 function takes 3 numbers as arguments and returns list in ascending order
def ascending_order(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            return f"Your numbers in ascending order are {num3}, {num2}, {num1}!"
        else:
            return f"Your numbers in ascending order are {num2}, {num3}, {num1}!"
    elif num2 > num3 and num2 > num1:
        if num3 > num1:
            return f"Your numbers in ascending order are {num1}, {num3}, {num2}!"
        else:
             return f"Your numbers in ascending order are {num3}, {num1}, {num2}!"
    elif num3 > num1 and num3 > num2:
        if num2 > num1:
            return f"Your numbers in ascending order are {num1}, {num2}, {num3}!"
        else:
            return f"Your numbers in ascending order are {num2}, {num1}, {num3}!"
        
print(ascending_order(7,74,10))
