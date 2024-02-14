class Person:
    '''
    This class defining the person object
    '''
    def __init__(self,person_name,person_email):
        self.person_name = person_name
        self.person_email=person_email
        self.locations = []
        
    def Add_Location_Person(self,location):
        self.locations.append(location)
    
