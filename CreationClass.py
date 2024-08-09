from ProspectClass import Prospect
from ScoutReport import ScoutReport
import random
import sqlite3


class ClassGen:

  def __init__(self, year): 
      self.west_prospects = self.region__gen()
      self.northeast_prospects = self.region__gen()
      self.southeast_prospects = self.region__gen()
      self.central__prospects = self.region__gen()
      self.classyear = year
      self.prospects = self.west_prospects + self.northeast_prospects + self.southeast_prospects + self.central__prospects
      self.to__db()
      

  def region__gen(self):
    regs = []
    #Will eventually be ~1200 each region
    for x in range(random.randrange(75,125)):
        pros = Prospect()
        regs.append(pros)
    
    return regs
  
  def to__db(self):
    con = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\RecruitingClasses.db")
    cur = con.cursor()

    for x in range(len(self.prospects)):

      pro = self.prospects[x]

      query = """INSERT INTO ClassGen1
              (FirstName, LastName, Age, Origin, Height, Weight, Bats, Throws, 
              DirectToBall, PlateVision, BaseballMovements, 
              Explosiveness, Strength, Rotationality, FrameMaximization,
              H1, SixtyYd, 
              PositionFeel, VeloOF, VeloIF, Framing, PopTime, Agility,
              Experience)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
              """

      data = (
          pro.firstname, pro.lastname, pro.age, pro.origin, pro.height, pro.weight, pro.bats, pro.throws, # 8
          pro.hit_tool_dic.get('DirectToBall'), pro.hit_tool_dic.get('PlateVision'), pro.hit_tool_dic.get('BaseballMovements'), # 3
          pro.raw_power_dic.get('Explosiveness'), pro.raw_power_dic.get('Strength'), pro.raw_power_dic.get('Rotationality'), pro.raw_power_dic.get('FrameMaximization'), # 4
          pro.speed_dic.get('H1'), pro.speed_dic.get('60Yd'), # 2
          # 6
          pro.defense_dic.get('PositionFeel'), pro.defense_dic.get('VeloOF'), pro.defense_dic.get('VeloIF'), pro.defense_dic.get('Framing'), pro.defense_dic.get('PopTime'),pro.defense_dic.get('Agility'),
          pro.plate_discipline_dic.get('Experience') # 1
          )
          
      
      cur.execute(query,data)  

    
    con.commit()
    con.close()

     #adding all players from generated prospect list to database specifically for prospects

  def __str__(self):
    for pro in self.prospects:
        print(ScoutReport('West',pro))
    return "" 

  def prospect__sort(self):
     idk_yet = ""
     #sorting all prospects based on general rank, could maybe have player generate a star rating and then sort using that

     
  

