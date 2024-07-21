import pymongo
import random
#Database Connection
CONNECTION_STRING = "mongodb://localhost:27017/"
PLAYER_GEN =pymongo.MongoClient(CONNECTION_STRING)["PlayerGen"]


class Player:

    #Constructor
    def __init__(self):
        self.first_name = self.first_name()  
        self.last_name = self.last_name()
        self.age = random.randrange(14,18)
        self.nationality = self.nationality()
        self.height = random.randrange (66,78)
        self.weight = random.randrange (140,220)
        self.jersey_num = random.randrange (0,99)

    #Randomly Retrieves First Name
    def first_name(self):
        first_name_CL = PLAYER_GEN["FirstName"]
        fn = first_name_CL.aggregate(
    [{ "$match": { "$expr": { "$gte": [ { "$rand": {} }, 0.5 ] } } }, { "$sample": { "size": 1 } }]
    )
        for name in fn:
            return name["first_name"]


    #Randomly Retrieves Last Name    
    def last_name(self):
        last_name_CL = PLAYER_GEN["LastName"]
        ln = last_name_CL.aggregate(
    [{ "$match": { "$expr": { "$gte": [ { "$rand": {} }, 0.5 ] } } }, { "$sample": { "size": 1 } }]
    )
        for name in ln:
            return name["name"]
        
    #Randomly Retrieves Country of Origin    
    def nationality(self):
        nation_CL = PLAYER_GEN["Locations"]
        nations = nation_CL.aggregate(
    [{ "$match": { "$expr": { "$gte": [ { "$rand": {} }, 0.5 ] } } }, { "$sample": { "size": 1 } }]
    )
        for countries in nations:
            return countries["Name"]

    #Converts height from inches to feet and inches, returns string of height in traditionally readable format
    def height_str(self):
        mod = self.height % 12

        match mod:
            case 0: return str(self.height // 12) + " foot"
            case 1: return str(self.height // 12) + " foot " + str(self.height % 12) + " inch"
            case _:  return str(self.height // 12) + " foot " + str(self.height % 12) + " inches"  

    
    #Output Formatting
    def __str__(self):
        return f"{self.first_name} {self.last_name}, age {self.age}, from {self.nationality}. Stands at {self.height_str()} tall and weighs {self.weight} pounds. They wear number {self.jersey_num}."