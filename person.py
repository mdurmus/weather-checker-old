

class Person:
    '''
    Here I am creating the user object to be used in the system.
    '''
    def __init__(self,person_name,person_email):
        self.person_name = person_name
        self.person_email=person_email
        self.cities = []
        
    def Add_City_Person(self,city):
        self.cities.append(city)
    
class City:
    '''
    I will keep the destination city and weather information here.
    '''
    def __init__(self,city_name,latitude,longitude, arrival_date, weather, celsius,kelvin,postal_code,country):
        self.country = country
        self.city_name = city_name
        self.latitude = latitude
        self.longitude = longitude
        self.arrival_date = arrival_date
        self.weather = weather
        self.celsius = celsius
        self.kelvin = kelvin
        self.postal_code = postal_code

