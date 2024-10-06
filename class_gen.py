from prospect_gen import ProspectGen
from report_gen import ReportGen
import numpy as np
import random
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from connect import engine
from prospect_models import Base, Prospect, Attributes, Performance, PositionsPlayed, Pitch






class ClassGen:
  
  def __init__(self): 
      self.prospects = self.populate_class()
      self.to_db()

  def populate_class(self):
    Base.metadata.create_all(bind=engine)
    pros = []
    p = ProspectGen()
    reg_weights = [.17,.16,.157, .17,.16,.17,.013]
    #Northwest, Midwest, Northeast, Southwest, South, Southeast, International
    regs = [0,1,2,3,4,5,6]
    for x in range(random.randrange(200,300)):  
      r = np.random.choice(regs, 1, False, reg_weights)
      pros.append(p.make_player(reg = r.tolist()[0]))
    #Will eventually be ~1200 each region
    return pros
  
  def to_db(self):
    session = Session(bind=engine)
    session.add_all(self.prospects)
    session.commit()
    
     #adding all players from generated prospect list to database specifically for prospects

  def __str__(self):
    return "" 

  def prospect__sort(self):
     idk_yet = ""
     #sorting all prospects based on general rank, could maybe have player generate a star rating and then sort using that

     
  

