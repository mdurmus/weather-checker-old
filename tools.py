import re
import requests
from geopy.geocoders import Nominatim

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

def Show_Map_Hint():
# A method that shows the user how to get 
# latitude and longitude numbers on maps.
    
   need_help = input('Please type Y or N and press return key. If you enter another letter application not accept!')
   need_help = need_help.upper()
   if need_help =='Y':
       print()
       print('Open the Google maps service. Find the place you want to go on the map. When you click the right mouse button on the place you want to go, you will see two decimal numbers at the top of the menu that opens, these are the numbers I want from you. For example: 53.298185248091954, -6.178650603203118')
       print()
       print('For more information please visit: https://support.google.com/maps/answer/18539?hl=en&co=GENIE.Platform%3DDesktop')
   else:
    print()
    print('Good sound!')

def Get_City_Information(city_count):
    '''
    Method that gets the city information to be added to the system from the user and creates an object.
    '''
    print(f'Toplam {city_count} kadar dönmelisin!')
   
    
    


def Get_CityName(latitude, longitude):
    geolocator = Nominatim(user_agent="demo")
    location = geolocator.reverse(f"{latitude},{longitude}")
    print(location.address)


