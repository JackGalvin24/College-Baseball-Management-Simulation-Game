from prospect_gen import ProspectGen
from class_gen import ClassGen
from scout_gen import ScoutGen
from report_gen import ReportGen
import sqlite3
from prospect_models import Base, Prospect, Attributes, Performance, PositionsPlayed, Pitch
from sqlalchemy.orm import Session
from connect import engine


d = ClassGen()



"""p = Prospect(0)

if p.position_history.__contains__('P'):
    for x in range(0, len(p.pitch_mix)):
        print( p.pitch_mix[x])"""

"""s = Scout()
s._assignment__(0)
s.scout_report()"""


