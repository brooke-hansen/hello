

def find_unique(numbers):
    seen_numbers = {}

    for number in numbers:
        if number in seen_numbers:
            seen_numbers[number] += 1
        else:
            seen_numbers[number] = 1
    
    for number, count in seen_numbers.items():
        if count == 1:
            return number

    
print(find_unique([5,6,6,7,7,8,5,9,8]))