#Q6 function that returns list of factors of a given integer
def find_factors(num):
    factor_list = []
    factor = ''
    for number in range(1, num +1):
        if num % number == 0:
            factor_list.append(number)
            number += 1
    return factor_list
        
print(find_factors(12))
