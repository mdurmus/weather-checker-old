import re
import requests
import smtplib
import pyfiglet

from email.mime.text import MIMEText
from person import City
from geopy.geocoders import Nominatim
from datetime import datetime

def Get_Name():
    '''
    Method that allows the user to enter a real/valid name
    '''
    while True:
        name = input('What is your name? ')
        #I use it to verify that the information entered is only alphanumeric characters
        if name.isalpha():
            print(f'Welcome {name} \n')
            return name
        else:
            print('\nPlease enter valid name (only alpha characters) and one word!\n')

            
def Get_Email():
    '''
    Method that allows the user to enter a valid email
    '''
    while True:
        # I use regex to make sure that the user enters a real email address.
        email = input('Please enter your email: ')
        pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')
        match = re.fullmatch(pattern, email)
        if match:
            return email
        else:
            print('Please enter a valid email address, for example: xxx@xxx.com')

def Show_Map_Hint():
    '''
    A method that shows the user how to get latitude and longitude numbers on maps.
    '''
    print()
    need_help = input('Please type Y or N and press return key. If you press a letter other than Y, the system accept it as N! ')
    need_help = need_help.upper()
    if need_help =='Y':
       print()
       print('Open the Google maps service. Find the place you want to go on the map. When you click the right mouse button on the place you want to go, you will see two decimal numbers at the top of the menu that opens, these are the numbers I want from you. For example: 53.298185248091954, -6.178650603203118')
       print()
       print('For more information please visit: https://support.google.com/maps/answer/18539?hl=en&co=GENIE.Platform%3DDesktop')
       print()
    else:
     print()
    print('Good sound!')

def Get_City_Information(city_count):
    '''
    Method that gets the city information to be added to the system from the user and creates an object.
    '''
    # I create a city list item.
    city_list = []
    # I create a loop with the number of cities entered by the user.
    for i in range(city_count):
       # I used a tuple to store the city information.
       city_data= Get_Latitude_Longitude(i)
       name = f'{i+1}'
       arrival_date = input('Enter arrival date (YYYY-MM-DD): ')
       # I converted the date because the Openweather API works with unix datetime.
       time_stamp = Convert_Date_Time(arrival_date)
       weather_data = Get_Weather_Info(city_data[0],city_data[1],time_stamp)
       kelvin = weather_data['temperature']
       weather = weather_data['description']
       celcius = kelvin_to_celcius_convert(kelvin)
       # I create a city object
       city = City(name,city_data[0],city_data[1],arrival_date,weather,celcius,kelvin,city_data[2],city_data[3])
       city_list.append(city)
    
    return city_list

def kelvin_to_celcius_convert(kelvin):
    '''
    This method convert kelvin value to celcius value
    '''
    celcius = kelvin-273.15
    celcius_format = "{:.1f}".format(celcius)
    return celcius_format
       
def Get_Latitude_Longitude(city_no):
    '''
    Method to verify entered coordinates
    '''
    city_no +=1
    while True:
        latitude = input(f'Please paste {city_no}. city  latitude: ')
        longitude = input(f'Please paste {city_no}. city  longitude: ')
        geolocator = Nominatim(user_agent="demo")
        location = geolocator.reverse(f"{latitude},{longitude}")
        # I wrote the whole address on the screen to be able to verify it.
        print(location.address)
        post_code = location.raw['address']['postcode']
        country = location.raw['address']['country']
        city_result = input('Is this correct city? Y/N ').upper()
        if city_result == 'Y':
            print('City added.')
            return (latitude,longitude,post_code,country)
        elif city_result == 'N':
            print('Please enter another latitude/longitude data.')
        else:
            print('Invalid input!')           
            
def Get_Weather_Info(latitude,longitude,date):
    '''
    Method to retrieve weather information.
    '''
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&dt={date}&appid=1406b02bd8391df1c6d7b280122de5ca"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
         # I only got two pieces of information, but there is actually much more
        return {
            "description": weather_description,
            "temperature": temperature
        }
    else:
        return None
    
def Convert_Date_Time(date):
    '''
    This method convert date to unix date format
    '''
    date = datetime.strptime(date,"%Y-%m-%d")
    api_format = int(date.timestamp())
    return api_format

def Show_All_Route(cities):
    print()
    print('##################################')
    print()
    print('Here is the weather list for the locations you want to visit!')
    print()
    for city in cities:
        print(f"Location: {city.city_name}\nPostal Code: {city.postal_code}\nCountry: {city.country}\nLatitude: {city.latitude}\nLongitude: {city.longitude}\nArrival Date: {city.arrival_date}\nWeather: {city.weather}\nCelsius: {city.celsius}°C\nKelvin: {city.kelvin}K\n")
        if cities.count()>1:
            print('\n-------------\n')
    print('##################################')
    print()
    
def Send_Mail(cities,person):
       subject = f"Hello {person.person_name}, report from Weather Reporter"
       body = "The locations and weather conditions you want to go to: \n "
       for city in cities:
           text = f"Location: {city.city_name}\nPostal Code: {city.postal_code}\nCountry: {city.country}\nLatitude: {city.latitude}\nLongitude: {city.longitude}\nArrival Date: {city.arrival_date}\nWeather: {city.weather}\nCelsius: {city.celsius}°C\nKelvin: {city.kelvin}K\n-----------\n"
           body += text
       password = "ZXCsdfert456_"
       receiver = person.person_email
       sender = "kontakt@mehmetdurmus.de"
       
       msg = MIMEText(body)
       msg['Subject'] = subject
       msg['From'] = sender
       msg['To'] = receiver
       
       with smtplib.SMTP_SSL('mail.your-server.de',465) as smtp_server : 
           smtp_server.login(sender,password)
           smtp_server.sendmail(sender,receiver, msg.as_string())

       print('All reports sended your email, please check your mailbox...')
    
