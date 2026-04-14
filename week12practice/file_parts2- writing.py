#var_name = open ('filename w/ extension', 'arguement for what we want to do')
# w = write, r = read, a = append, ...

my_file = open('sample.txt', 'w')

my_file.write('party time!\n')
my_file.write('hello world')

family_file = open('family.txt', 'w')
family_file.write("first last age\n")
family_file.write('Amanda, Connors, 47\n')
family_file.write('Bryon, Hansen, 47\n')
family_file.write('Brooke, Hansen, 26\n')
family_file.write('Britney, Hansen, 24\n')
family_file.write('Bryon, Hansen, 22\n')

family_file.close()

family_file = open('family.txt', 'r')

total = 0
count = 0 

for line in family_file.readlines()[1:]:
    line_data = line.split(",")
    #print(line_data)
    first_name = line_data[0]
    last_name = line_data[1]
    age = int(line_data[2])
    count += 1
    total += age

mean = total / count
print(mean)


