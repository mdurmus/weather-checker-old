import re
import requests
from person import City
from geopy.geocoders import Nominatim
from datetime import datetime

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
   print()
   need_help = input('Please type Y or N and press return key. If you enter another letter application not accept! ')
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
    city_list = []
    for i in range(city_count):
       city_data= Get_Latitude_Longitude(i)
       name = f'City {i}'
       arrival_date = input('Enter arrival date (YYYY-MM-DD): ')
       time_stamp = Convert_Date_Time(arrival_date)
       weather_data = Get_Weather_Info(city_data[0],city_data[1],time_stamp)
       kelvin = weather_data['temperature']
       weather = weather_data['description']
       celcius = kelvin_to_celcius_convert(kelvin)
       
       city = City(name,city_data[0],city_data[1],arrival_date,weather,celcius,kelvin,city_data[2])
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
        
        print(location.address)
        
        post_code = location.raw['address']['postcode']
        
        city_result = input('Is this correct city? Y/N ').upper()
        
        if city_result == 'Y':
            print('City added.')
            return (latitude,longitude,post_code)
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
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return {
            "description": weather_description,
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed
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


