from ProspectClass import Prospect
from CreationClass import ClassGen
from ScoutReport import ScoutReport
import random
import sqlite3

REGIONS = ['West', 'Central', 'Northeast', 'Southeast', 'International']
class Scout:

    def __init__(self):
        self.firstname = "Elliot"
        self.lastname = "Urgent"
        self.location_pref = REGIONS[random.randrange(0,4)]
        print(self.location_pref)
        self.CAA = random.randrange(40,80)


    def first_name(self):
        return ""

    def _assignment__(self, loc):
        #if matches location pref improve report acc rating
        self.report_one = ScoutReport(loc, self.location_pref == loc)

    def _hire_(self,org):
        self.organization = org


    def __str__(self):
        return self.firstname + " " + self.lastname
    


    #Think about how to intentionally obfuscate definite truths




    