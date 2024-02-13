from person import Person, City
from tools import Get_Name, Get_Email, Show_Map_Hint, Get_City_Information, Show_All_Route,Send_Mail

print('Welcome to the weather report generator!')
print()
name = Get_Name()
print(f'Welcome {name}')
print()
mail = Get_Email()
print(f'Ok {name}, now i will prepare your personal data file...')
print()
person = Person(name,mail)

print('Yes your personal data is ready. I\'ll help you plan your trip/vacation. But we need to agree on some things. Firstly, you need to give me the latitude and longitude of your destination. Can you do that or should I give you a hint?')

Show_Map_Hint()

print('Ok now can continue...')

city_count = int(input('How many cities do you want to add? '))

cities = Get_City_Information(city_count)
Show_All_Route(cities)

mail_result = input('Do you want me to send this information to your e-mail address? Y/N ').upper()

if mail_result == 'Y':
    Send_Mail(cities,person)
else:
    print('See you again!')


