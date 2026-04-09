

def return_unique(numbers):
    seen_numbers= {}
    unique_numbers = []

    for number in numbers:
        if number in seen_numbers:
            seen_numbers[number] += 1
        else:
            seen_numbers[number] = 1
    
    for number, count in seen_numbers.items():
        if count == 1:
            unique_numbers.append(number)
    
    return unique_numbers
        
print(return_unique([9,5,6,8,7,7,8,9]))