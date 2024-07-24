import pymongo
import random
import sqlite3

#Database Connection
CONNECTION_STRING = "mongodb://localhost:27017/"
PLAYER_GEN =pymongo.MongoClient(CONNECTION_STRING)["PlayerGen"]

#Frequently Used Arrays
POSITIONAL_ARRAY = ['1B', '2B', 'SS', '3B', 'CF', 'LF', 'RF', 'C' 'P']

class Prospect:

    #Constructor
    def __init__(self):
        self.first_name = self.first_name()  
        self.last_name = self.last_name()
        self.age = random.randrange(14,18)
        self.nationality = self.nationality()
        self.height = random.randrange (66,78)
        self.weight = random.randrange (140,220)
        self.jersey_num = random.randrange (0,99)
        self.position = POSITIONAL_ARRAY[random.randrange(0,8)]

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
        
    #To String Functions broken up by section or subfunction
    def height_str(self):
        mod = self.height % 12

        match mod:
            case 0: return str(self.height // 12) + "' "
            case _: return str(self.height // 12) + "'" + str(self.height % 12) + "\" "
                 
    def intro__str__(self):
        return f"{self.first_name} {self.last_name} | Age: {self.age} | {self.nationality} | Height: {self.height_str()}| Weight: {self.weight} | Position: {self.position}\n\nSECONDARY POSITIONS"

    def injury__str__(self):
        return 'INJURY HISTORY'

    def athletic__str__(self):
        return 'ATHLETIC PROFILE'
    
    def defense__str__(self):
        return 'DEFENSE'
    
    def hitting__str__(self):
        return 'HITTING'
    
    def pitching__str__(self):
        return 'PITCHING'
    
    def pedigree__str__(self):
        return 'PEDIGREE'

    #Output Formatting Consolidation
    def __str__(self):
        return self.intro__str__() + "\n\n" + self.injury__str__() + "\n\n" + self.athletic__str__() + "\n\n" + self.defense__str__() + "\n\n" + self.hitting__str__() + "\n\n" + self.pitching__str__() + "\n\n" + self.pedigree__str__() + "\n"
    
   