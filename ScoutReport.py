from ProspectClass import Prospect
import random
import sqlite3

REPORT_COUNT = 1

class ScoutReport:

    def __init__(self, reg):
        self.region = reg
        print(reg)

   #To String Mini Functions + Consolidation 
    """def height_str(self):
        mod = self.height % 12

        match mod:
            case 0: return str(self.height // 12) + "' "
            case _: return str(self.height // 12) + "'" + str(self.height % 12) + "\" "
                 
    def intro__str__(self, pros):
        return f"{self.first_name} {self.last_name} | Age: {self.age} | {self.nationality} | Height: {self.height_str()}| Weight: {self.weight} | " + self.bats + "/" + self.throws
    
    def pos__played__str__(self):
        return ""

    def injury__str__(self):
        return 'INJURY HISTORY'

    def athletic__str__(self):
        return 'ATHLETIC PROFILE'
    
    def defense__str__(self):
        return 'DEFENSE'
    
    def hitting__str__(self):
        return 'HITTING'
    
    def pitching__str__(self):
        return 'PITCHING'
    
    def pedigree__str__(self):
        return 'PEDIGREE'

    def __str__(self, pros):
        return self.intro__str__() + "\n\n" + self.pos__played__str__() + "\n\n" + self.injury__str__() + "\n\n" + self.athletic__str__() + "\n\n" + self.defense__str__() + "\n\n" + self.hitting__str__() + "\n\n" + self.pitching__str__() + "\n\n" + self.pedigree__str__() + "\n"
    """