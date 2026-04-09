#Q6 create a function that creates product ids for diff fruit juices
#use first 3 letters of fruit and capacity 
def get_drink_id(flavor, capacity):
    words = flavor.split()
    product_id = ""

    for word in words:
        product_id += word[:3]
    
    product_id += str(capacity)

    return product_id

user_flavor = input("Enter flavor: ")
user_capacity = int(input("Enter the capacity: "))

print(get_drink_id(user_flavor, user_capacity))