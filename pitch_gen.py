import itertools
from prospect_models import Pitch

class PitchGen:

    def release_gen(self):
            # probably make sense to be generated together
            #calc includes mound pos
        return 51, 51
    
    def spin_rate_gen(self):
            # Measured in RPM (ranges per pitch type prob make sense)
        return 2500

    def spin_eff_gen(self):
            # 20-80 Grade (random gen?)
        return 45

    def hand_pos_gen(self):
            # 0-100 hidden until on team
        return 51

    def velo_con_gen(self):
            # 20-80 Grade
        return 45

    def mound_pos_gen(self):
            # random but tight range, 0 - 100
        return 51

        
        
    def vert_move_sharp_gen(self):
            # 20-80 grade, replaces 'feel'
        return 45

    def delivery_eff_gen(self):
            # 0-100, frame max equivalent
        return 51

    def h_move_gen(self, velo):
            # measured in inches
            # calc will factor in spin rate/eff, release y, mound/hand pos, pitcher velo grade
        return 10

    def h_move_sharp_gen(self):
            # 20-80 grade, replaces 'feel'
         return 45

    def sub_id_gen(self, velo):
            # identifies a slider from curveball, for example
            # calc includes pitcher velo grade, pitch type id, h/v movement
        return 3
    
    def make_pitch(self, type = 0, velo = 90):

        rel_x, rel_y = self.release_gen()
       
        return Pitch(
            pitch_type_id = type,
            spin_rate = self.spin_rate_gen(),
            spin_eff = self.spin_eff_gen(),
            hand_position = self.hand_pos_gen(),
            velo_consistency = self.velo_con_gen(),
            mound_pos = self.mound_pos_gen(), 
            release_x = rel_x,
            release_y = rel_y,
            v_movement_sharpness = self.vert_move_sharp_gen(),
            delivery_eff = self.delivery_eff_gen(),
            horizontal_movement = self.h_move_gen(velo),
            h_movement_sharpness = self.h_move_sharp_gen(),
            pitch_sub_id = self.sub_id_gen(velo)
            )






    
   