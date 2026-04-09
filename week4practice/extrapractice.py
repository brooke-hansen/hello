#write a program that outputs the amount of deficient numbers, perfect numbers, and abundant numbers
#between 1 and some upper bound specified by the user
upper_bound = int(input("Enter an upper bound for a check: "))
for number in range(1, upper_bound +1):
    proper_divisors = 0
    prop_div_list = []
    deficient_num = 0
    perfect_num = 0
    abundant_num = 0
#proper divisor is less than self
    if upper_bound % number == 0:
        if number < upper_bound:
            prop_div_list.append(number)
            proper_divisors += 1

#perfect number is sum of proper divisors
    #if proper_divisors > 0:

#abundunt num is less than sum of proper divisors


#deficient numb is greater than sum of proper divisors

