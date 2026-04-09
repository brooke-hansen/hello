#CHALLENGE 1

#ask user for input for age (can include decimals)
human_age = float(input("Enter age: "))
#convert human_age to dog_age
dog_age = human_age * 7
#break into years, months, days
years = int(dog_age)
#subtract years to isolate decimals (months -> days)
remain_year = dog_age - years
#isolate decimals and convert into months
months_total = remain_year * 12
months = int(months_total)
#isolate decimals and convert into days
remain_month = months_total - months
days = int(remain_month * 30)
#round result of dog_age to first two decimals
print(f"That is {dog_age:.2f} dog years.")
#string dog age with years, months, and days
print(f"Your age as a dog is {years} years, {months} months, and {days} days old!")

#convert human age to cat age
cat_age = human_age * 9
#ignore decimal from cat years
cyears = int(cat_age)
#isolate decimal from cat years and convert to months
locyears = cat_age - cyears
cmonths_total = locyears * 12
#ignore decimal from cat months
cmonths = int(cmonths_total)
#isolate decimal from cat months and convert to days
locmonths = cmonths_total - cmonths
cdays = int(locmonths * 30)
#round result of cat_age to first two decimals
print(f"That is {cat_age:.2f} cat years.")
#string cat age together in years, months, and days
print(f"Your age as a cat is {cyears} years, {cmonths} months, and {cdays} days old!")

#convert human_age to horse_age
horse_age = 3 * ((((human_age ** 2) - 47) / 7) + 12)
hyears = int(horse_age)
lohyears = horse_age - hyears
hmonths_total = lohyears * 12
hmonths = int(hmonths_total)
lohmonths = hmonths_total - hmonths
hdays = int(lohmonths * 30)
print(f"That is {horse_age:.4f} horse years.")
print(f"Your age as a horse is {hyears} years, {hmonths} months, and {hdays} days old!")

