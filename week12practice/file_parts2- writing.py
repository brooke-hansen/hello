#var_name = open ('filename w/ extension', 'arguement for what we want to do')
# w = write, r = read, a = append, ...

my_file = open('sample.txt', 'w')

my_file.write('party time!\n')
my_file.write('hello world')

family_file = open('family.txt', 'w')
family_file.write("first last age\n")
family_file.write('Amanda, 47\n')
family_file.write('Bryon, 47\n')
family_file.write('Britney, 24\n')
family_file.write('Bryon, 22\n')

family_file.close()





