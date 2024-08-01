import pymongo
import random
import sqlite3

#Database Connection
CONNECTION_STRING = "mongodb://localhost:27017/"
PLAYER_GEN =pymongo.MongoClient(CONNECTION_STRING)["PlayerGen"]

#Frequently Used Arrays
POSITIONAL_ARRAY = ['1B', '2B', 'SS', '3B', 'CF', 'LF', 'RF', 'C', 'P']
GRADE_ARRAY = ['30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80']


"""
Necessary Methods:
Batting Stat Gen
Athletic Gen
Pitching Gen
Make-Up / Pedigree Gen
    includes new adaptablity stat
Accolades Gen
Injury Gen
Age Converter / Birthday Generator
getters for all of this
"""
AGES = [16] + [17] * 6 + [18]

class Prospect:

    #Constructor
    def __init__(self):
        self.firstname = self.first_name()  
        self.lastname = self.last_name()
        self.age = AGES[random.randrange(0,7)]
        self.origin = self.nationality()
        self.height = random.randrange (66,78)
        self.weight = random.randrange (140,220)
        self.position_history = self.pos_played()
        self.bats = self.bat_hand()
        self.throws = self.throw_hand(self.bats)
        #Athletic Qualitative Stats
        self.AA = self.athletic_grades()
        #Batting Quantitative Stats
        self.hitting_performance = self.batting__stats()
        
        match 'P' in self.position_history:
            #Pitching Quantitative Stats if applicable
            case False: self.IP = 0
            case _: self.pitch_grades = self.pitching_grades()


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


    def bat_hand(self):
        bat_chance = ['R'] * 55 + ['L'] * 33 + ['S'] * 13

        for x in self.position_history:
            if x.__eq__('P'):
                bat_chance = ['R'] * 57 + ['L'] * 43

        return bat_chance[random.randrange(0,100)]
    
    def throw_hand(self,bats):
        chance = []
        
        for x in self.position_history:
            if x.__eq__('P'):
                return self.bats

        match bats:
            case 'R': 
                chance = ['R'] * 500 + ['L'] + ['R'] * 499
            case 'L':
                chance = ['R'] * 3 + ['L'] * 25
            case _:
                chance = ['R'] * 57 + ['L'] * 42
                


        return chance[random.randrange(0,len(chance))]


    def pos_played(self):
        max = 9
        played = []
        rand_weight = [1] * 2 + [2] * 3 + [3] * 3 + [4,5]
        num_played = random.choice(rand_weight)
        pos_list =self.__pos__list__mixer()

        for x in range(num_played):
            i = random.randrange(0,max)
            played.append(pos_list.pop(i))
            max -= 1

        return played

    def __pos__list__mixer(self):
        pos_played = []

        for x in range(9):
            pos_played.append(POSITIONAL_ARRAY[x])

        return pos_played
    

    def athletic_grades(self):
        ags = {
            'H1': str(round(random.uniform(10.5,12.2), 2)) + ' s',
            '60': str(round(random.uniform(6.9,8.1), 2))+ ' s',
            'IF': str(90) + ' mph',
            'OF': str(95) + ' mph',
            'PROJ': 50,
            'AGI': 50,
            'BBMOV': 50,
            'ROT': 50,
            'MAX': 50,
            'STR': 50,
            'RAWP': 50,
            'GAMP': 50,
            'EXP' : 50,

        }
        
        match 'P' in self.position_history:
            case False:
                ags.update({'FB': 'N/A'})
            case _:
                ags.update({'FB': random.randrange(30,80)})

        return ags

    def batting__stats(self):
        return ""


    def batting_grades(self):
        return ""
    

    def defensive_grades(self):
        return ""
    

    def pitching_grades(self):
        return ""

    def makeup_factors(self):
        return ""
    
    def grades_to_stats(self):
        return ""
        


    
    


#Presentation Function here will be individual player card?
   