

def count_repetitions(elements):
    seen_elements = {} #empty dictionary

    for element in elements:
        if element in seen_elements:
            seen_elements[element] += 1
        else:
            seen_elements[element] = 1
    
    return seen_elements

print(count_repetitions([1,5,5,5,12,12,0,0,0]))
        