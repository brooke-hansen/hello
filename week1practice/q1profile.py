first_name = input("What's your first name? ")
age = int(input("What's your age? ").strip())
if age <= 19:
    print ("Isn't it past your bed time, " + first_name +'?')
if age > 19:
    print ("Need help finding an early bird's special, " + first_name + '?')
