from ProspectClass import Prospect
import random
import sqlite3

REPORT_COUNT = 1

class ScoutReport:
    
    def __init__(self, reg, pro):
        self.region = reg
        self.prospect = pro
    """
    Functions needed
    read/write from sql table to get all prospects in region
    translate from bit stream
    """

   #To String Mini Functions + Consolidation 
    def height_str(self):
        mod = self.prospect.height % 12

        match mod:
            case 0: return str(self.prospect.height // 12) + "' "
            case _: return str(self.prospect.height // 12) + "'" + str(self.prospect.height % 12) + "\" "
                 
    def intro__str__(self):
        return f"{self.prospect.firstname} {self.prospect.lastname} | Age: {self.prospect.age} | {self.prospect.origin} | Height: {self.height_str()}| Weight: {self.prospect.weight} | " + self.prospect.bats + "/" + self.prospect.throws
    
    def pos__played__str__(self):
        pos = ""
        for x in self.prospect.position_history:
            pos = pos + x + ", "

        return f"POSITIONS PLAYED: " + pos[:len(pos) - 2]

    def injury__str__(self):
        return 'INJURY HISTORY'


    def athletic__str__(self):
        grades = self.prospect.AA.keys()
        comp = ""

        for key in grades:
            comp = comp + key + ': ' + str(self.prospect.AA.get(key)) + '\n'


        return 'ATHLETIC PROFILE\n' + comp
    
    def defense__str__(self):
        return 'DEFENSE'
    
    def hitting__str__(self):
        return 'HITTING'
    
    def pitching__str__(self):
        return 'PITCHING'
    
    def pedigree__str__(self):
        return 'PEDIGREE'

    def __str__(self):
        return self.intro__str__() + "\n\n" + self.pos__played__str__() + "\n\n" + self.injury__str__() + "\n\n" + self.athletic__str__() + "\n\n" + self.defense__str__() + "\n\n" + self.hitting__str__() + "\n\n" + self.pitching__str__() + "\n\n" + self.pedigree__str__() + "\n"
    