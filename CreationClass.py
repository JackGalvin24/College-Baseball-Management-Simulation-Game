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
    for x in range(random.randrange(5,6)):
        pros = Prospect()
        regs.append(pros)
    
    return regs
  
  def to__db(self):
    con = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\RecruitingClasses.db")
    cur = con.cursor()
    for x in range(len(self.prospects)):
      pro = self.prospects[x]
      query = "INSERT INTO ClassGen1 (FirstName, LastName, Age, Origin, Height, Weight, Bats, Throws) VALUES(?,?,?,?,?,?,?,?)" 
      cur.execute(query, (pro.firstname, pro.lastname, pro.age, pro.origin, pro.height, pro.weight, pro.bats, pro.throws))

      #query = "INSERT INTO ClassGen1 (FirstName, LastName, Age, Origin, Height, Weight) VALUES(?,?,?,?,?,?)" 
    
    con.commit()

     #adding all players from generated prospect list to database specifically for prospects

  def __str__(self):
    for pro in self.prospects:
        print(ScoutReport('West',pro))
    return "" 

  def prospect__sort(self):
     idk_yet = ""
     #sorting all prospects based on general rank, could maybe have player generate a star rating and then sort using that

     
  

