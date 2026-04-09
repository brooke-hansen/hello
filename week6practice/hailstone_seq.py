#Q5 given n, write function that returns hailstone sequence
def hailstone_seq(n):
    numlyst = []
    num = n
    while num != 1:
        if num % 2 == 0:
            numlyst.append(num)
            num = num / 2
        elif num % 2 == 1:
            numlyst.append(num)
            num = (num * 3) + 1
    num = 1
    numlyst.append(num)
    return numlyst

print(hailstone_seq(25))