

class Person:
    '''
    Here I am creating the user object to be used in the system.
    '''
    def __init__(self,person_name,person_surname,person_email):
        self.person_name = person_name
        self.person_surname=person_surname
        self.person_email=person_email
        self.cities = []
        
    def Add_City_Person(self,city):
        self.cities.append(city)
    
class City:
    '''
    I will keep the destination city and weather information here.
    '''
    def __init__(self,city_name, arrival_date, weather, celsius):
        self.city_name = city_name
        self.arrival_date = arrival_date
        self.weather = weather
        self.celsius = celsius

