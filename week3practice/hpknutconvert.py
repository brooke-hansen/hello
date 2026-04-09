#Q12 HP money conversion, only print non-zero values
userk = int(input("How many knuts do you have? "))
whole_g = 0  # to be added to and then printed if >0
whole_s = 0  # to be added to and printed if >0
whole_k = 0  # to be added to and printed if >0
#convert knuts to galleons
total_g = userk / 493
whole_g = int(total_g)
#remaining knuts after galleons
remaining_knuts = userk - (whole_g * 493)
#convert remaining knuts to sickles
total_s = remaining_knuts / 29
whole_s = int(total_s)
#remaining knuts after sickles
whole_k = remaining_knuts - (whole_s * 29)
print("The smallest change you can carry is", end=" ")
first = True
if whole_g > 0:
    print(whole_g, "galleon(s)", end="")
    first = False
if whole_s > 0:
    if not first:
        print(" and ", end="")
    print(whole_s, "sickle(s)", end="")
    first = False
if whole_k > 0:
    if not first:
        print(" and ", end="")
    print(whole_k, "knut(s)")