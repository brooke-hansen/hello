#Q3 function that loops through and returns list with every even number in a range
def output_even(smallernum,largernum):
    num_lyst = []
    even_num = ''
    for number in range(smallernum, largernum + 1):
        if number % 2 == 0:
            even_num = number
            num_lyst.append(even_num)
            even_num = ''
    return num_lyst

print(output_even(15,24))