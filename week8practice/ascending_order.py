#Q7 function takes 3 arguments
#returns list of integers in ascending order
#NO built-in max, min, sort, or sorted!!!

def ascending_order(num1, num2 = 5, num3 = 25):
    num_lyst = []
    largest_num = ""
    mid_num = ""
    small_num = ""
    if num1 > num2 and num2 > num3: #1>2>3
        num_lyst.append(num3)
        num_lyst.append(num2)
        num_lyst.append(num1)
        return num_lyst
    if num2 > num1 and num1 > num3: #2>1>3
        num_lyst.append(num3)
        num_lyst.append(num1)
        num_lyst.append(num2)
        return num_lyst
    if num2 > num3 and num3 > num1: #2>3>1
        num_lyst.append(num1)
        num_lyst.append(num3)
        num_lyst.append(num2)
        return num_lyst
    if num3 > num2 and num2 > num1: #3>2>1
        num_lyst.append(num1)
        num_lyst.append(num2)
        num_lyst.append(num3)
        return num_lyst
    if num3 > num1 and num1 > num2: #3>1>2
        num_lyst.append(num2)
        num_lyst.append(num1)
        num_lyst.append(num3)
        return num_lyst
    if num1 > num3 and num3 > num2: #1>3>2
        num_lyst.append(num2)
        num_lyst.append(num3)
        num_lyst.append(num1)
        return num_lyst
    
print(ascending_order(2,3,1))
print(ascending_order(10,1))
print(ascending_order(50))