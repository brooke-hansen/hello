#Q8 function that returns list of integers in descending order
def descending_order(num1, num2, num3):
    if num1 > num2 and num2 > num3:
        return f"Your numbers in descending order are {num1}, {num2}, {num3}"
    elif num1 > num3 and num3 > num2:
        return f"Your numbers in descending order are {num1}, {num3}, {num2}"
    elif num3 > num1 and num1 > num2:
        return f"Your numbers in descending order are {num3}, {num1}, {num2}"
    elif num3 > num2 and num2 > num1:
        return f"Your numbers in descending order are {num3}, {num2}, {num1}"
    elif num2 > num1 and num1 > num3:
        return f"Your numbers in descending order are {num2}, {num1}, {num3}"
    elif num2 > num3 and num3 > num1:
        return f"Your numbers in descending order are {num2}, {num3}, {num1}"

print(descending_order(18, 75, 99))
n1 = 55
n2 = 34
n3 = 1

print(descending_order(n1,n2,n3))