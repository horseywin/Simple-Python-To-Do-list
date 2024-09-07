tasks = ['do hass homework', 'eat instant noodles']
while True:
    print("")
    print('To do list:')

    for i in tasks:
        print(f'{(tasks.index(i)) + 1}. {i}')
    print("")
    edit = input(str('Would you like to add or remove '))

    if edit == 'add' or edit == 'remove':
        if edit == 'add':
            tasks.append(input("What would you like to add? "))
        else:
            tasks.pop(int(input("Enter the number of the item you want to remove ")) - 1)
    else:
        print("Please enter either add or remove")
        print('')
        