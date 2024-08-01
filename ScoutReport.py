from ProspectClass import Prospect
import random
import sqlite3

REPORT_COUNT = 1

class ScoutReport:

    def __init__(self, reg):
        self.region = reg
        self.jake = Prospect()
    """
    Functions needed
    read/write from sql table to get all prospects in region
    translate from bit stream
    """

   #To String Mini Functions + Consolidation 
    def height_str(self):
        mod = self.jake.height % 12

        match mod:
            case 0: return str(self.jake.height // 12) + "' "
            case _: return str(self.jake.height // 12) + "'" + str(self.jake.height % 12) + "\" "
                 
    def intro__str__(self):
        return f"{self.jake.firstname} {self.jake.lastname} | Age: {self.jake.age} | {self.jake.origin} | Height: {self.height_str()}| Weight: {self.jake.weight} | " + self.jake.bats + "/" + self.jake.throws
    
    def pos__played__str__(self):
        pos = ""
        for x in self.jake.position_history:
            pos = pos + x + ", "

        return f"POSITIONS PLAYED: " + pos[:len(pos) - 2]

    def injury__str__(self):
        return 'INJURY HISTORY'

    def athletic__str__(self):
        grades = self.jake.AA.keys()
        comp = ""

        for key in grades:
            comp = comp + key + ': ' + str(self.jake.AA.get(key)) + '\n'


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
    