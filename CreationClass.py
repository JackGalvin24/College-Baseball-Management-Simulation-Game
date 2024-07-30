from ProspectClass import Prospect
import random
import sqlite3



class ClassGen:

  def __init__(self): 
      self.prospects = []
      for x in range(random.randrange(4750,5250)):
        self.prospects.append(Prospect())

  
  

