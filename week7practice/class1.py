#2/24/26 
'''
#to initialize a dictionary in python we use { }
my_dictionary = {} #this is an empty dictionary

#we can creae a dictionary with inital values with following code
#the keys and values are seperated by a : and key-value pairs are
#seperated by , 
phonebook = {'matt': 1438, 'ashley': 1234} #{'key': value} use keys to find values

#print(phonebook['matt']) #prints 1438
#print(phonebook['waters']) #breaks because name isn't there
#print(phonebook[0]) #crashes because no 0 key
#print(phonebook) #print before adding 'waters', not in dictionary

#to add to a dictionary -> dict_name[key] = value
phonebook['waters'] = 5678

#print(phonebook['waters'])
#print(phonebook) #prints after phonebook, 'waters' present

#print(phonebook.keys()) #prints "dict_keys(['matt', 'ashley', 'waters'])"
#print(list(phonebook.keys())) #prints "['matt', 'ashley', 'waters']"

for key in phonebook.keys():
    value = phonebook[key]
    msg = f'name: {key}   number: {value}'
    print(msg) #prints ( name: xxxx   number: 0000) line by line of phonebook
'''

#create an empty dictionary
#add functionality to allow each person at table to enter name and age from console
#store info in dictionary 
#once type done, info prints on single line
table_dict = {}
while True:
    key = input("Enter your name: ") #asks for name
    if key == 'done': #if input is done
        break #end code
    value = int(input("Enter your age: ")) #ask age
    table_dict[key] = value #attach input to dictionary
print("At this table is" ) #print 
for key in table_dict.keys(): #for key in table_dict(): also works
    value = table_dict[key]
    msg = f'name: {key}   age: {value} '
    print(msg) #prints ( name: xxxx   number: 0000) line by line of phonebook
    
    

