
#calculate amount of taxed owed for the 2023 year based on marital status and income
#request income earned
earned_income = float(input("Enter your earned income for 2023: "))
taxed_income = 0
#request marital status
print("Were you married or single in 2023? ")
marital_status = input("m for married or s for single: ")
#if single, 10%= 0-11k, 12%= 11,001-44,725, 22%= 44,725-95,375
if marital_status == 's':
    if earned_income in range(0,11000):
        tax_rate = 0.10
        taxed_income = 0
    elif earned_income in range(11001,44725):
        tax_rate = 0.12
        
    elif earned_income in range(44726,95375):
        tax_rate = 0.22
#if married, 10%= 0-22k, 12%= 22,001-89,450, 22%= 89,451-190,750
else:
    if earned_income in range(0,22000):
        tax_rate = 0.10
    elif earned_income in range(22001,89450):
        tax_rate = 0.12
    elif earned_income in range(89451,190750):
        tax_rate = 0.22
tax_owed = earned_income * tax_rate
#inform user of taxes owed, rounded to the nearest penny
print(f"You owe approximately ${tax_owed:.2f} in taxes for 2023!")