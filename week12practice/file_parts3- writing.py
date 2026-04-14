
number_file = open("numbers.txt")
'''
data = number_file.read()
#print(data)
lyst = []
lyst.append(data)
'''
'''
data = number_file.readlines()

#print(data)

for number in data:
    print(number)

total = 0
count = 0

for number in data:
    total += int(number.strip())
    count += 1

mean = total/count
print(mean)
'''
total = 0
count = 0

for number in number_file.readlines():
    total += int(number.strip())
    count += 1

mean = total/count
print(mean)

number_file.close()
