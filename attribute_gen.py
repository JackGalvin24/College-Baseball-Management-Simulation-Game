from pitch_gen import PitchGen
from prospect_models import Prospect, Attributes, Performance, PositionsPlayed, Pitch#, Scout, ScoutingReport
from sqlalchemy.orm import Session
from connect import engine
import random


GRADE_ARRAY = [20] * 235 + [30] * 1350 + [40] * 2272 + [45] * 2272 + [50] * 2272 + [55] * 675 + [60] * 675 + [70] * 235 + [80] * 30

class AtrGen:
    

    def attribute_gen(self):
        self.atrs = self.random_atrs()


        return self.attribute_compiler()

        
    
    def random_atrs(self):
        ags = {
                'plate_vision': str(random.sample(GRADE_ARRAY, k=1))[1:3],
                'Explosiveness': str(random.sample(GRADE_ARRAY, k=1))[1:3],
                'Strength': str(random.sample(GRADE_ARRAY, k=1))[1:3],
                'Rotationality': str(random.sample(GRADE_ARRAY, k=1))[1:3],
                'Experience': str(random.sample(GRADE_ARRAY, k=1))[1:3],
                'Adaptability': str(random.sample(GRADE_ARRAY, k=1))[1:3],
                'Agility': str(random.sample(GRADE_ARRAY, k=1))[1:3],
                'MakeupOn': str(random.sample(GRADE_ARRAY, k=1))[1:3],
                'MakeupOff': str(random.sample(GRADE_ARRAY, k=1))[1:3],
                'Personality': str(random.randrange(0,100)),
                'FrameMax': str(random.sample(GRADE_ARRAY, k=1))[1:3],
                'AthleticMax': str(random.sample(GRADE_ARRAY, k=1))[1:3],  
                }
                
        return ags
    
    def derived_atrs(self):
        ''

    def attribute_compiler(self):
        return Attributes(
            direct_to_ball = self.atrs.get(),
            plate_vision = self.atrs.get('plate_vision'),
            baseball_movements = self.atrs.get(),
            explosiveness = self.atrs.get(),
            strength = self.atrs.get(),
            rotationality = self.atrs.get(),
            max_frame = self.atrs.get(),
            home_first = self.atrs.get(),
            sixty_yd = self.atrs.get(),
            velo_of = self.atrs.get(),
            velo_if = self.atrs.get(),
            arm_consistency = self.atrs.get(),
            framing = self.atrs.get(),
            pop_time = self.atrs.get(),
            agility = self.atrs.get(),
            adabtability = self.atrs.get(),
            velo_fb = self.atrs.get(),
            velo_ch = self.atrs.get(),
            velo_bb = self.atrs.get(),
            experience = self.atrs.get(),
            pos_feel = self.atrs.get(),
            catcher_feel = self.atrs.get(),
            durability = self.atrs.get(),
            availability = self.atrs.get(),
            pro_super_split = self.atrs.get(),
        )