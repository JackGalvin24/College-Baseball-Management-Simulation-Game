from prospect_gen import ProspectGen
from class_gen import ClassGen
from report_gen import ReportGen
import random
import sqlite3
import numpy as np

REGIONS = ([0,1,2,3,4,5,6])

class ScoutGen:

    def __init__(self):
        self.firstname = self.name_gen(0)
        self.lastname = self.name_gen(1)
        self.id = 0
        self.location_pref = REGIONS[random.randrange(0,6)]
        self. region_id = self.location_pref
        self.archetype_id = self.arc_gen()
        
        

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


    def arc_gen(self):
        return np.random.choice([0,1,2,3,4,5,6,7], 1, False, [.12,.15,.05,.07,.3,.13,.13,.05])


    def _assignment__(self, reg):
        #if matches location pref improve report acc rating
        self.region = reg

    def _hire_(self,org):
        self.team_id = org


    def scout_trip(self):
        
        # Connect to DB
        conn = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\RecruitingClasses.db")
        cur = conn.cursor()
        
        prospect_ids = cur.execute(f"SELECT player_id FROM prospect WHERE region_id = {self.location}").fetchall()
        
        for prospect in prospect_ids:
            ReportGen(self.id, prospect[0])

  #      for prospect in prospect_ids:
   #         baseball_movements_atr = "" # similar statement to hit tool 
    #        raw_power_atr = ""
     #       game_power_atr = ""
      #      hit_tool_atr = cur.execute(f"SELECT direct_to_ball, plate_vision, baseball_movements FROM prospect WHERE player_id = {prospect[0]}").fetchall()
       #     pos_feel_atr = ""
#
 #           if logic:
  #              framing_atr = ""
#
 #           baseball_movements = self.hit_tool(a,b,c)
  #          raw_power = self.hit_tool(a,b,c)
   #         game_power = self.hit_tool(a,b,c)
    #        hit_tool = self.hit_tool(a,b,c)
     #       pos_feel = self.hit_tool(a,b,c)
      #      self.scouting_report("""all, of, these""")

        

            
        conn.close()
            

        # Get all the stats from players in region, eventually some level of determination of how many you go get, maybe stored in player data?
        
       

        # for all of the stats, create range, select number from range, add to statistic matrix (aka numpy array) for each player
        # Things to think about - 
        # Helper functions?
        # implementation of range width - how flexible is possible
        

        # Calculate big bucket grades from all of the relevant attributes
        # write all big bucket grades to relevant players

        #general questions - how many players are gotten? How do you know which ones have been visited and how many times?
        return ""

    def scout_bias(self, atr):
        ""

    def grade_round(self, num):
        
        base = 10

        if 40 <= num <= 60:
            base = 5

        return base * round(num / base)
    

    def hit_tool(self, dtb, pv, bbm):
        direct_to_ball = self.scout_bias(dtb)
        plate_vision = self.scout_bias(pv)
        basbeball_movements = self.scout_bias(bbm)

        hittool = (dtb + pv + bbm) / 3

        return self.grade_round(hittool)
    

    def game_power(self, exp, str, rot):
        return 50
    
    def raw_power(self, rawp, hittool):
        return 50
    
    def speed(self, h1, sixty, frm):
        return 50
    
    def defense(self, bballmove):
        return 50

    def plate_discipline(self):
        return 50
    
    def hit_tool(self):
        return 50
    
    def starter_or_reliever(self):
        ""

    
    

    def scouting_report(self, hitT, rawP, gameP, spD, deF, plateD):
        con = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\RecruitingClasses.db")
        cur = con.cursor()
        
        query = """INSERT INTO scouting_report
              (scout_id, prospect_id, hit_tool, game_power, raw_power, speed, defense, plate_discipline, frame_max)
              VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
              """

        con.commit()
        con.close()
        

    def to_db(self):
        con = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\RecruitingClasses.db")
        cur = con.cursor()

        query = """INSERT INTO scout
              (scout_id, archetype_id, region_preference, assigned_region)
              VALUES(?, ?, ?, ?)
              """        
        
        data = (
          self.id, self.team_id, self.archetype_id, self.location_pref, self.region
          )

        cur.execute(query,data)  

    
        con.commit()
        con.close()
     

    def __str__(self):
        return self.firstname + " " + self.lastname
    


    #Think about how to intentionally obfuscate definite truths




    