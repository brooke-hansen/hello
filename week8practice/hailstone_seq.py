#Q6 given hailstone sequence
#set default argument to 40 

def hailstone_seq( n = 40):
    hailstone_lyst= []
    while n != 1:
        hailstone_lyst.append(round(n,0))
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3) + 1
    hailstone_lyst.append(1)
    return hailstone_lyst

print(hailstone_seq())
print(hailstone_seq(25))
