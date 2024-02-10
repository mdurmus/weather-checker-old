import re

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
            
def Get_Email():
    '''
    Method that allows the user to enter a valid email
    '''
    while True:
        email = input('Please enter your email: ')
        pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')
        match = re.fullmatch(pattern, email)
  
        if match:
            return email
        else:
            print('Please enter a valid email address, for example: xxx@xxx.com')
