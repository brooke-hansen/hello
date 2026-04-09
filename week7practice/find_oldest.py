#Q1 create function that takes dict of names and ages
#and returns name of oldest person

def find_oldest(people):
    oldest_name = ""
    oldest_age = 0
    for name, age in people.items():
        if age > oldest_age:
            oldest_age = age
            oldest_name = name
    return oldest_name

people = {"Emma":71, "Jack":45, "Olivia":82, "Lucas":31} 
print(find_oldest(people))