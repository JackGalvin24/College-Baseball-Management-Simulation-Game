from ProspectClass import Prospect
import random

class ScoutReport:
    
    def __init__(self):

        self.prospects = []
        for x in range(random.randrange(15,20)):
            self.prospects.append(Prospect())
            


    def __str__(self):
        for prospect in self.prospects:
            print(prospect)
        return ""
