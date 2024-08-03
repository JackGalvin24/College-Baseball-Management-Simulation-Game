import random
import sqlite3
import numpy as np

#Database Connection
#Frequently Used Arrays
POSITIONAL_ARRAY = ['1B', '2B', 'SS', '3B', 'CF', 'LF', 'RF', 'C', 'P']
RECCOMENDATION_ARRAY = ['C', '2W', 'PO', 'CB', 'MI', 'CF']
#Substitution for normal curve
GRADE_ARRAY = [20] + [30] * 25 + [40] * 135 + [45] * 200 + [50] * 280 + [55] * 200 + [60] * 135 + [70] * 25 + [80]


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


class Prospect:

    #Constructor
    def __init__(self):
        self.origin = self.from__location()
        self.firstname = self.name_gen('FirstName')
        self.lastname = self.name_gen('LastName')
        self.age = random.randrange(1,365)
        self.height = random.randrange (66,78)
        self.weight = random.randrange (140,220)
        self.position_history = self.pos_played()
        self.bats = self.bat_hand()
        self.throws = self.throw_hand()
        self.hit_tool_dic = self.hit_tool_atr()
        self.raw_power_dic = self.raw_power_atr()
        self.game_power_dic = self.game_power_atr()
        self.speed_dic = self.speed_atr()
        self.defense_dic = self.defense_atr ()
        self.plate_discipline_dic = self.plate_discipline_atr()
        """match 'P' in self.position_history:
            #Pitching Quantitative Stats if applicable
            case False: self.IP = 0
            case _: self.pitch_grades = self.pitching_atr()
"""


    #Randomly Retrieves First/Last Name from Database
    def name_gen(self, col):
        conn = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\PlayerGen.db")
        cur = conn.cursor()
        rows = cur.execute(f'SELECT {col} FROM Names ORDER BY RANDOM() LIMIT 1').fetchall()
        conn.close()
        return rows[0][0]
        
    #Randomly Retrieves Country of Origin    
    def from__location(self):
        conn = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\PlayerGen.db")
        cur = conn.cursor()
        rows = cur.execute('SELECT Name FROM Locations ORDER BY RANDOM() LIMIT 1').fetchall()
        conn.close()
        return rows[0][0]

    #Randomly Assigns Bat Hand Base on Weighted Values
    def bat_hand(self):
        bat_chance = ['R'] * 55 + ['L'] * 33 + ['S'] * 13

        for x in self.position_history:
            if x.__eq__('P'):
                bat_chance = ['R'] * 57 + ['L'] * 43

        return bat_chance[random.randrange(0,100)]
    
    #Assigns throwing hand based on factors like positions played and batting hand
    def throw_hand(self):
        chance = []
        
        for x in self.position_history:
            if x.__eq__('P'):
                return self.bats

        match self.bats:
            case 'R': 
                chance = ['R'] * 500 + ['L'] + ['R'] * 499
            case 'L':
                chance = ['R'] * 3 + ['L'] * 25
            case _:
                chance = ['R'] * 57 + ['L'] * 42
                


        return chance[random.randrange(0,len(chance))]

    #Assigns random amount of randomly selected positions
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

    #Supplementary function to pos_played
    def __pos__list__mixer(self):
        pos_played = []

        for x in range(9):
            pos_played.append(POSITIONAL_ARRAY[x])

        return pos_played
    

    def hit_tool_atr(self):
        ags = {
            'DirectToBall': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'PlateVision': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'BaseballMovements': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'H/PA': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'K/AB': str(random.sample(GRADE_ARRAY, k=1))[1:3]
            }
        
        return ags


    def raw_power_atr(self):
        ags = {
            'Explosiveness': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Strength': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Rotationality': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'FrameMaximization': str(random.sample(GRADE_ARRAY, k=1))[1:3]
            }
        return ags
    

    def game_power_atr(self):
        ags = {
            'Explosiveness': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Strength': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Rotationality': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'FrameMaximization': str(random.sample(GRADE_ARRAY, k=1))[1:3]
            }
        return ags

    def speed_atr(self):
        ags = {
            'H1': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            '60Yd': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'FrameMaximization': self.raw_power_dic.get('FrameMaximization')
            }
        return ags
    

    def defense_atr(self):
        ags = {
            'PositionFeel': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'BaseballMovements': self.hit_tool_dic.get('BaseballMovements'),
            'VeloOF': 'N/A',
            'VeloIF': 'N/A',
            'Framing': 'N/A',
            'PopTime': 'N/A',
            'Agility': str(random.sample(GRADE_ARRAY, k=1))[1:3]
            }
        

        if '2B' in self.position_history or '2B' in self.position_history or '2B' in self.position_history or '2B' in self.position_history:
            ags.update({'VeloIF': str(random.sample(GRADE_ARRAY, k=1))[1:3]})

        if 'LF' in self.position_history or 'CF' in self.position_history or 'RF' in self.position_history:
            ags.update({'VeloOF': str(random.sample(GRADE_ARRAY, k=1))[1:3]})

        if 'C' in self.position_history:
            ags.update({'Framing': str(random.sample(GRADE_ARRAY, k=1))[1:3]})
            ags.update({'PopTime': str(random.sample(GRADE_ARRAY, k=1))[1:3]})


        return ags
    
    def plate_discipline_atr(self):
        ags = {
            'Experience': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            '60Yd': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'FrameMaximization': self.raw_power_dic.get('FrameMaximization')
            }
        
        return ags
    
    def makeup_factors(self):
        return ""
    
    def grades_to_stats(self):
        return ""

        
    def __str__(self):
        return "" + self.firstname + " " + self.lastname + " " + self.origin
    
    
    


#Presentation Function here will be individual player card?
   