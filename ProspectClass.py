import random
import sqlite3
import numpy as np
import itertools
from pitch import Pitch

#STATIC VARIABLES
POSITIONAL_ARRAY = ['P', 'SS', 'C', 'CF', '3B', 'RF', '1B', '2B', 'DH', 'LF' ]
POSITIONAL_ARRAY_NUMS = [1, 6, 2, 8 ,5, 9, 3, 4, 0, 7]

#Custom curve w slightly right skew
GRADE_ARRAY = [20] * 235 + [30] * 1350 + [40] * 2272 + [45] * 2272 + [50] * 2272 + [55] * 675 + [60] * 675 + [70] * 235 + [80] * 30


#WEIGHT LIST KEY
#0: POSITIONS AVAILABLE TO PLAY
#1: WEIGHT TO PLAY EACH POSITION
#2: WEIGHT ON HOW MANY POSITIONS THEY WILL PLAY
#3: LEFT / RIGHT THROW WEIGHT
#4: LEFT / RIGHT / SWITCH HIT WEIGHT

INJURY_LIST = ['Shoulder Pain', 'Forearm Strain', 'Elbow Tendinitis', 'Blister', 'UCL Strain', 'UCL Tear', 'Rotator Cuff Strain', 'Labrum Tear',
        'Flexor Tendon Strain', 'Hip Flexor Strain', 'Wrist Pain', 'Oblique Strain', 'Back Strain', 'Ankle Sprain', 'Broken Bone', 'Hamstring Pull',
        'Concussion', 'Meniscus Tear', 'Groin Strain', 'Plantar Fascitis', "Skiier's Thumb", 'Bone Bruise', 'Fractured Finger/Hand', 'Quad Strain']

POS_WEIGHT_LISTS = {

'P': (['1B', 'LF', 'RF', '3B', 'CF', 'SS', 'C'],
      [0.22, 0.22, 0.22, 0.22, 0.08, 0.038, 0.002],
      [.775, .225],
      [.23, .756, .014],
      [.225,.755,.02]
      ),

'SS': (['3B', '2B', 'CF', 'LF', 'RF',  'C'],
       [0.54, 0.24, 0.1, 0.04, 0.04, 0.04],
       [.4,.05, .184, .183, .183],
       [.001,.999],
       [.14,.84,.02],
      
        ),


'C': (['1B', '3B', 'RF', 'SS', 'CF', 'LF'],
      [.75,.10,.10,.0225,.0225,.005],
      [.5,.2,.1,.1,.1],
      [.001,.999],
      [.11,.8775,.0125],
     
      ),

'DH': ( [],
        [],
        [],
        [.08,.92],
        [.225, .755 ,.02]),

'CF': (['RF', 'SS', '2B', 'LF', '3B'],
       [.6,.25,.05,.09,.01],
       [.5,.02,.16,.16,.16],
       [.23, .77],
       [.225, .755, .02]
       ),


'3B': (['1B', 'SS', 'RF', 'LF', 'CF', 'C'],
       [.75, .15, .04, .04, .01, .01],
       [.25,.35,.134,.133,.133],
       [0,1],
       [.11, .0075]
       ),


'RF': (['LF', 'CF', '1B', '3B', 'C'],
       [.9, .05, .03,.01,.01],
       [.5,.1,.134,.133,.133],
       [.08, .92],
       [.225, .755 ,.02]
       ),


'1B': (['RF', 'SS', 'CF', 'LF', 'C', '3B'],
       [.045,.15,.03,.005,.25,.52],
       [.67,.13, .067, .067, .066],
       [.32, .68],
       [.36, .62, .02]
       ),


'2B': (['SS', 'CF', '3B', 'C', 'LF', 'RF'],
       [.8,.08,.09,.01,.01,.01],
       [.2,.15,.217,.217,.216],
       [.001, .999],
       [.14, .83, .03]
       ),


'LF': (['CF', 'SS', '2B', 'RF', '1B'],
       [.7,.05,.05,.18,.02],
       [.2,.3,.167,.167,.166],
       [.32,.68],
       [.32, .62, .02]
       )   

}


INJ_WEIGHT_LISTS = {
'Tommy John': (['1B', 'LF', 'RF', '3B', 'CF', 'SS', 'C'],
      [0.22, 0.22, 0.22, 0.22, 0.08, 0.038, 0.002],
      [.775, .225],
      [.23, .756, .014],
      [.225,.755,.02]

      ),

'Achilles Tear':([]),

'Forearm Strain': ([]),

'ACL Tear': ([]),

'Broken Wrist': ([]),


}
"""
Necessary Methods:

"""


class Prospect:
    id_iter = itertools.count(start=2500, step = 1)
    
    #Constructor
    def __init__(self, reg):
        self.prospect_id = next(Prospect.id_iter)
        self.region_id = reg
        self.origin_id = self.from__location()
        self.first_name = self.name_gen(0)
        self.last_name = self.name_gen(1)
        self.age = random.randrange(1,365)
        self.height = random.randrange (66,78)
        self.weight = random.randrange (140,220)
        
        self.position_history = self.pos_played()

        if self.position_history.__contains__('P'):
            self.pitch_mix = self.pitches_thrown()

        self.hit_tool_dic = self.hit_tool_atr()
        self.raw_power_dic = self.raw_power_atr()
        self.game_power_dic = self.game_power_atr()
        self.speed_dic = self.speed_atr()
        self.defense_dic = self.defense_atr ()
        self.plate_discipline_dic = self.plate_discipline_atr()
        
        self.bats = self.bat_hand()
        self.throws = self.throw_hand()
        """match 'P' in self.position_history:
            #Pitching Quantitative Stats if applicable
            case False: self.IP = 0
            case _: self.pitch_grades = self.pitching_atr()
"""


    #Randomly Retrieves First/Last Name from Database
    # *** NEEDS UPDATING ***
    def name_gen(self, col):
        conn = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\Reference.db")
        cur = conn.cursor()
        
        if self.region_id == 6:
            if col == 0:  rows = cur.execute('SELECT name FROM first_names WHERE international == 1 ORDER BY RANDOM() LIMIT 1').fetchall()
            elif col == 1: rows = cur.execute('SELECT name FROM last_names WHERE international == 1 ORDER BY RANDOM() LIMIT 1').fetchall()  
        else:
            if col == 0:  rows = cur.execute('SELECT name FROM first_names ORDER BY RANDOM() LIMIT 1').fetchall()
            elif col == 1: rows = cur.execute('SELECT name FROM last_names ORDER BY RANDOM() LIMIT 1').fetchall()     

        conn.close()
        return rows[0][0]
        
    #Randomly Retrieves Country of Origin    
    # *** NEEDS UPDATING ***
    def from__location(self):
        conn = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\Reference.db")
        cur = conn.cursor()
        rows = cur.execute(f'SELECT location_id FROM locations WHERE region_id = {self.region_id} ORDER BY RANDOM() LIMIT 1').fetchone()
        conn.close()
        return rows[0]

    #Randomly Assigns Bat Hand Base on Weighted Values
    def bat_hand(self):
        # 0 = R, 1 = L, 2 = S
        bat_chance = [0] * 55 + [1] * 33 + [2] * 13

        for x in self.position_history:
            if x.__eq__('P'):
                bat_chance = ['0'] * 57 + ['1'] * 43

        return bat_chance[random.randrange(0,100)]
    
    #Assigns throwing hand based on factors like positions played and batting hand
    def throw_hand(self):
        chance = []
        
        for x in self.position_history:
            if x.__eq__('P'):
                return self.bats

        match self.bats:
            case 0: 
                chance = [0] * 500 + [1] + [0] * 499
            case 1:
                chance = [0] * 3 + [1] * 25
            case _:
                chance = [0] * 57 + [1] * 42
                


        return chance[random.randrange(0,len(chance))]

    #Assigns random amount of randomly selected positions
    def pos_played(self):
        pos_p = []

        #Weight for position 1
        pos_1_weight = [0.44, 0.22, 0.13, 0.1, 0.04, 0.02, 0.03, 0.01, 0.007, 0.003]

        pos_1 = np.random.choice(POSITIONAL_ARRAY, 1, False, pos_1_weight)

        pos_p.append(pos_1.tolist()[0])

        if pos_p[0] == 'DH':
            #stays at 1 position
            return pos_p

        pos_lists = POS_WEIGHT_LISTS.get(pos_p[0])

        position_opts = pos_lists[0]
        weights = pos_lists[1]


        if pos_p[0] == 'P': can_play = np.random.choice([0,1], 1, False, pos_lists[2])
        else: can_play = np.random.choice([0,1,2,3,4], 1, False, pos_lists[2])

        num = can_play[0]

        if num > 0:
                sel = np.random.choice(position_opts, num, False, weights)
                for x in range(0,num):
                            pos_p.append(sel.tolist()[x])


        if pos_p[0] == ('CF'):
            if not (pos_p.__contains__('LF')):
                pos_p.append('LF')
            
            if not (pos_p.__contains__('RF')):
                pos_p.append('RF')



        elif pos_p[0] == ('LF'):
            if  not (pos_p.__contains__ ('RF')):
                pos_p.append('RF')

        elif pos_p[0] == ('RF'):
            if  not (pos_p.__contains__ ('LF')):
                pos_p.append('LF')


        return pos_p
    

    def pitches_thrown(self):
        mix = [Pitch()]

        n = np.random.choice([0,1,2], 1, False, [.71, .27, .02])
        
        for x in range(0, n):
            mix.append(Pitch(0))

        n = np.random.choice([0,1,2], 1, False, [.2, .7, .1])

        for x in range(0, n):
            mix.append(Pitch(1))

        n = np.random.choice([0,1,2], 1, False, [.05, .6, .35])

        for x in range(0, n):
            mix.append(Pitch(2))


        return mix
    


    # PERFORMANCE STATS NOTES
    # Based on:
    # Individual Attributes
    # Class Quality w/in region
    # School Pedigree w some split for public vs private
    # Injury record  

    def attribute_gen(self):
        #Randomly Generated attributes

        ags = {
            'PlateVision': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Explosiveness': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Strength': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Rotationality': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Experience': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Adaptability': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Agility': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'MakeupOn': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'MakeupOff': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'Personality': str(random.randrange(0,100)),
            'FrameMax': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'AthleticMax': str(random.sample(GRADE_ARRAY, k=1))[1:3],  
        }
        
        return ags


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
            'VeloOF': 20,
            'VeloIF': 20,
            'Framing': 20,
            'PopTime': 20,
            'Agility': str(random.sample(GRADE_ARRAY, k=1))[1:3]
            }
        

        if '2B' in self.position_history or '3B' in self.position_history or 'SS' in self.position_history or '1B' in self.position_history:
            ags.update({'VeloIF': str(random.sample(GRADE_ARRAY, k=1))[1:3]})

        if 'LF' in self.position_history or 'CF' in self.position_history or 'RF' in self.position_history:
            ags.update({'VeloOF': str(random.sample(GRADE_ARRAY, k=1))[1:3]})

        if 'C' in self.position_history:
            ags.update({'Framing': str(random.sample(GRADE_ARRAY, k=1))[1:3]})
            ags.update({'PopTime': str(random.sample(GRADE_ARRAY, k=1))[1:3]})


        return ags
    
    def plate_discipline_atr(self):
        ags = {
            'adaptability': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'PlateDiscipline': str(random.sample(GRADE_ARRAY, k=1))[1:3],
            'HitTool': self.raw_power_dic.get('FrameMaximization')
            }
        
        return ags
    
    def makeup_factors(self):
        return ""
    
    def grades_to_stats(self):
        return ""

        
    def __str__(self):
        pos = ""
        for x in self.position_history:
            pos = pos + " " + x
        return "" + self.first_name + " " + self.last_name + " " + str(self.region_id) + " " + str(self.prospect_id) + " " + pos
    
    
    


#Presentation Function here will be individual player card?
   