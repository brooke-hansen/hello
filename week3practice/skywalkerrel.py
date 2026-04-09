#Q9 user input name --> output relation
relative = input("Input name: ")
if relative == 'Darth Vader' or relative == 'darth vader':
    print('Darth Vader is your father')
elif relative == 'Leia' or relative == 'leia':
    print('Leia is your sister')
elif relative == 'Han Solo' or relative == 'han solo' or relative == 'han' or relative == 'Han':
    print('Han is your brother in law')
elif relative == 'R2D2' or relative == 'r2d2':
    print('R2D2 is your drone')
else:
    print('Unknown')