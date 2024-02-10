def Get_Name():
    '''
    Method that allows the user to enter a real/valid name
    '''
    while True:
        name = input('What is your name? ')
        if name.isalpha():
            return name
        else:
            print('Please enter valid name (only alpha characters) and one word!')