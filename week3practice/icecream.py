#Q8
customer_request = input("Pick a flavor: ")
available = False
if customer_request == 'strawberry' or customer_request == 'Strawberry':
    available = True
if customer_request == 'chocolate' or customer_request == 'Chocolate':
    available = True
if customer_request == 'vanilla' or customer_request == 'Vanilla':
    available = True
if available == False:
    print(f'{customer_request} ice cream is not available!')
else:
    print(f'Here is your {customer_request} ice cream!')