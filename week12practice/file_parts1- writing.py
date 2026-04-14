import random
number_file = open("numbers.txt", 'w')

for index in range(100):
    number = random.randint(300,750)
    number_file.write(str(number)+ "\n")

'''
ave_num = 0
num_lyst = []
data = number_file.read()

for number in data:
    number = int(number)
    ave_num += number
    num_lyst.append(number)

for index in len(num_lyst):
    ave_num = ave_num / (len(num_lyst_ + 1)) 

print(ave_num)
'''

data = number_file.readlines()

print(data)

total = 0
count = 0

for number in data:
    total += number.strip()
    count += 1

mean = total/count
number_file.close()
#write 100 random numbers in separate linees
#str(3) = 3
