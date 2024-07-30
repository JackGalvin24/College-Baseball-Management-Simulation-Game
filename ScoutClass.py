from ProspectClass import Prospect
from CreationClass import ClassGen
from ScoutReport import ScoutReport
import random

REGIONS = ['West', 'Central', 'Northeast', 'Southeast', 'International']
class Scout:

    def __init__(self):
        self.first_name = "Elliot"
        self.last_name = "Urgent"
        self.location_pref = REGIONS[random.randrange(0,4)]
        print(self.location_pref)
        self.CAA = random.randrange(40,80)

    def _assignment__(self, loc):
        #if matches location pref improve report acc rating
        self.report_one = ScoutReport(loc, self.location_pref == loc)

    def _hire_(self,org):
        self.organization = org


    def __str__(self):
        return self.first_name + " " + self.last_name
    


    #Think about how to intentionally obfuscate definite truths




    