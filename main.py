import pyfiglet
from person import Person
from tools import Get_Name, Get_Email, Show_Map_Hint, Get_City_Information, Show_All_Route,Send_Mail
welcome_text = 'Weather Checker!'

banner = pyfiglet.figlet_format(welcome_text)
print(banner)

# Method that retrieves the user's name. 
name = Get_Name()

# The method that retrieves the user's mail address. 
mail = Get_Email()

print(f'\nOk {name}, now i will prepare your personal data file...\n')

# I create person object and fill data
person = Person(name,mail)

print('Yes your personal data is ready. I\'ll help you plan your trip/vacation. But we need to agree on some things. Firstly, you need to give me the latitude and longitude of your destination. Can you do that or should I give you a hint?')

# Method that shows the user how to use maps.
Show_Map_Hint()

print('Ok now can continue...\n')


# I want the user to enter only numeric character.
while True:
    try:
        city_count = int(input('How many cities do you want to add? '))
        break
    except ValueError:
        print('Please enter only numeric value!')

# Method that asks for the number of cities specified by the user one by one
cities = Get_City_Information(city_count)

# Method that shows all the cities entered by the user with all relevant information.
Show_All_Route(cities)


mail_result = input('Do you want me to send this information to your e-mail address? Y/N ').upper()

if mail_result == 'Y':
    # If user want, this method send all information to user as e-mail
    Send_Mail(cities,person)
else:
    print('See you again!')


