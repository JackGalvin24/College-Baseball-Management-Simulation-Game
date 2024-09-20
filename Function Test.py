import random
import sqlite3
import numpy as np
from collections import Counter
import itertools

conn = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\RecruitingClasses.db")
cur = conn.cursor()
        
prospect_ids = cur.execute(f"SELECT player_id FROM prospect WHERE region_id = 0").fetchall()

for prospect in prospect_ids:
    print(prospect[0])

print(prospect_ids[0][0])