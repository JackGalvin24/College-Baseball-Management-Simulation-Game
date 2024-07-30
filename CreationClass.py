from ProspectClass import Prospect
import random
import sqlite3

YEAR = 2024

class ClassGen:

  def __init__(self): 
      self.west_prospects = self.region__gen()
      self.northeast_prospects = self.region__gen()
      self.southeast_prospects = self.region__gen()
      self.central__prospects = self.region__gen()
      
      self.prospects = self.west_prospects + self.northeast_prospects + self.southeast_prospects + self.central__prospects

      

  def region__gen(self):
    regs = []
    #Will eventually be ~1200 each region
    for x in range(random.randrange(10,20)):
        pros = Prospect()
        regs.append(pros)
    
    return regs
  
  def to__db(self):
     idk_yet = ""
     #adding all players from generated prospect list to database specifically for prospects


  def prospect__sort(self):
     idk_yet = ""
     #sorting all prospects based on general rank, could maybe have player generate a star rating and then sort using that

     
  

