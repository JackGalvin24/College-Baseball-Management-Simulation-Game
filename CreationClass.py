from ProspectClass import Prospect
from ScoutReport import ScoutReport
import numpy as np
import random
import sqlite3



class ClassGen:
    
  def __init__(self): 
      self.prospects = self.region__gen()
      self.to__db()

  def region__gen(self):
    pros = []
    
    reg_weights = [.17,.16,.157, .17,.16,.17,.013]
    #Northwest, Midwest, Northeast, Southwest, South, Southeast, International
    regs = [0,1,2,3,4,5,6]
    for x in range(random.randrange(200,300)):  
      r = np.random.choice(regs, 1, False, reg_weights)
      pros.append(Prospect(r.tolist()[0]))
    #Will eventually be ~1200 each region
    


    return pros
  
  def to__db(self):
    con = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\RecruitingClasses.db")
    cur = con.cursor()

    for x in range(0,len(self.prospects)):

      pro = self.prospects[x]

      # PROSPECT GENERAL

      query = """INSERT INTO prospect
              (player_id, first_name, last_name, age, region_id, origin_id, height, weight, bats, throws)
              VALUES(?,?,?,?,?,?,?,?,?,?)
              """

      data = (pro.prospect_id, pro.first_name, pro.last_name, pro.age, pro.region_id, pro.origin_id, pro.height, pro.weight, pro.bats, pro.throws)
      cur.execute(query,data)  
      con.commit()

      # PROSPECT ATTRIBUTES

      query = """INSERT INTO prospect_atr
              (player_id, direct_to_ball, plate_vision, baseball_movements,
              explosiveness, strength, rotationality, max_frame,
              home_first, sixty_yd, velo_of, velo_if,
              framing, pop_time, agility, adaptability)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
              """

      #Needs to be updated with accurate attributes
      data = (pro.prospect_id, pro.hit_tool_dic.get('DirectToBall'), pro.hit_tool_dic.get('PlateVision'), pro.hit_tool_dic.get('BaseballMovements'), 
          pro.raw_power_dic.get('Explosiveness'), pro.raw_power_dic.get('Strength'), pro.raw_power_dic.get('Rotationality'), pro.raw_power_dic.get('FrameMaximization'),
          pro.speed_dic.get('H1'), pro.speed_dic.get('60Yd'), 
           pro.defense_dic.get('VeloOF'), pro.defense_dic.get('VeloIF'), pro.defense_dic.get('Framing'), pro.defense_dic.get('PopTime'),pro.defense_dic.get('Agility'),
          pro.plate_discipline_dic.get('adaptability') )
      cur.execute(query,data)  
      con.commit()


      # PROSPECT POSITIONS PLAYED

      query = f"""INSERT INTO positions_played
              (prospect_id)
              VALUES(?)
              """

      data = (pro.prospect_id,)
      cur.execute(query, data)  
      con.commit()

      for x in range(1,len(pro.position_history)+1):
        query = f"""UPDATE positions_played
              SET pos_{x} = '{pro.position_history[x-1]}'
              WHERE prospect_id = {pro.prospect_id}
              """

        cur.execute(query)  
        con.commit()
    

      #PROSPECT PITCHING DATA IF APPLICABLE
      if 'P' in pro.position_history:
        for x in range(0, len(pro.pitch_mix) ):
          query = f"""INSERT INTO pitches_thrown
              (player_id, pitch_id)
              VALUES(?,?)
              """
          data = (pro.prospect_id, pro.pitch_mix[x])
          cur.execute(query, data)  
          con.commit()


    cur.close()

     #adding all players from generated prospect list to database specifically for prospects

  def __str__(self):
    return "" 

  def prospect__sort(self):
     idk_yet = ""
     #sorting all prospects based on general rank, could maybe have player generate a star rating and then sort using that

     
  

