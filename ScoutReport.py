from ProspectClass import Prospect
import random
import sqlite3

RECCOMENDATION_ARRAY = ['C', '2W', 'PO', 'CB', 'MI', 'CF']
REPORT_COUNT = 1

class ScoutReport:
    
    """
    Functions needed
    read/write from sql table to get all prospects in region
    translate from bit stream
    """

    def __init__(self, scout_id, player_id):
        self.scout_id = scout_id
        self.player_id = player_id

   #To String Mini Functions + Consolidation 
    def height_str(self):
        mod = self.prospect.height % 12

        match mod:
            case 0: return str(self.prospect.height // 12) + "' "
            case _: return str(self.prospect.height // 12) + "'" + str(self.prospect.height % 12) + "\" "
                 
    def intro__str__(self):
        age = ""
        match self.prospect.age < 183:
            case True: age = "SPRING"
            case _: age = "FALL"
        return f"{self.prospect.first_name} {self.prospect.last_name} | Age: {age} | {self.prospect.origin} | Height: {self.height_str()}| Weight: {self.prospect.weight} | " + self.prospect.bats + "/" + self.prospect.throws
    
    def pos__played__str__(self):
        pos = ""
        for x in self.prospect.position_history:
            pos = pos + x + ", "

        return f"POSITIONS PLAYED: " + pos[:len(pos) - 2]

    def injury__str__(self):
        return 'INJURY HISTORY'

    def hit__tool__str__(self):
        grades = self.prospect.hit_tool_dic.keys()
        comp = ""

        for key in grades:
            comp = comp + key + ': ' + str(self.prospect.hit_tool_dic.get(key)) + '\n'


        return 'HIT TOOL\n' + comp
    
    def plate__discipline__str(self):
        grades = self.prospect.plate_discipline_dic.keys()
        comp = ""

        for key in grades:
            comp = comp + key + ': ' + str(self.prospect.plate_discipline_dic.get(key)) + '\n'
        return 'PLATE DISCIPLINE\n' + comp
    
    def raw__power__str__(self):
        grades = self.prospect.raw_power_dic.keys()
        comp = ""

        for key in grades:
            comp = comp + key + ': ' + str(self.prospect.raw_power_dic.get(key)) + '\n'


        return 'RAW POWER\n' + comp
    
    def game__power__str__(self):
        grades = self.prospect.game_power_dic.keys()
        comp = ""

        for key in grades:
            comp = comp + key + ': ' + str(self.prospect.game_power_dic.get(key)) + '\n'


        return 'GAME POWER\n' + comp
    
    def speed__str__(self):
        grades = self.prospect.speed_dic.keys()
        comp = ""

        for key in grades:
            comp = comp + key + ': ' + str(self.prospect.speed_dic.get(key)) + '\n'


        return 'SPEED\n' + comp
    
    def defense__str__(self):
        grades = self.prospect.defense_dic.keys()
        comp = ""

        for key in grades:

            if self.prospect.defense_dic.get(key) != 20:
                comp = comp + key + ': ' + str(self.prospect.defense_dic.get(key)) + '\n'
            else:    
                comp = comp + key + ": N/A\n"
                
        return 'DEFENSE\n' + comp
    
    

    def __str__(self):
        return self.intro__str__() + "\n\n" + self.pos__played__str__() + "\n\n" + self.injury__str__() + "\n\n" + self.hit__tool__str__() + "\n\n" + self.plate__discipline__str() + "\n\n" + self.raw__power__str__() + "\n\n" + self.game__power__str__() + "\n\n" + self.speed__str__() + "\n\n" + self.defense__str__() + "\n"
    