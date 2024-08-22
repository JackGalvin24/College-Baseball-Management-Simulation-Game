from ProspectClass import Prospect
from CreationClass import ClassGen
from ScoutReport import ScoutReport
import random
import sqlite3

REGIONS = ['West', 'Central', 'Northeast', 'Southeast', 'International']

class Scout:

    def __init__(self):
        self.firstname = self.name_gen('FirstName')
        self.lastname = self.name_gen('LastName')
        self.location_pref = REGIONS[random.randrange(0,4)]
        self.CAA = random.randrange(40,80)


    def name_gen(self, col):
        conn = sqlite3.connect("D:\\Prospect_Sim\\DB Data\\PlayerGen.db")
        cur = conn.cursor()
        rows = cur.execute(f'SELECT {col} FROM Names ORDER BY RANDOM() LIMIT 1').fetchall()
        conn.close()
        return rows[0][0]

    def _assignment__(self, loc):
        #if matches location pref improve report acc rating
        self.report_one = ScoutReport(loc, self.location_pref == loc)

    def _hire_(self,org):
        self.organization = org


    def __str__(self):
        return self.firstname + " " + self.lastname
    


    #Think about how to intentionally obfuscate definite truths




    