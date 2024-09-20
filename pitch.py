import itertools

class Pitch:
    id_iter = itertools.count()
    def __init__(self, type = 0):
        self.pitch_id = next(self.id_iter)
        self.pitch_type_id = type
        self.spin_rate = self.spin_rate_gen()
        self.spin_eff = self.spin_eff_gen()
        self.hand_position = self.hand_pos_gen()
        self.velo_consistency = self.velo_con_gen()
        self.mound_pos = self.mound_pos_gen()
        self.release_x, self.release_y = self.release_gen()
        self.vert_move_sharp = self.vert_move_sharp_gen()
        self.delivery_eff = self.delivery_eff_gen()
        self.hor_movement = self.h_move_gen()
        self.h_movement_sharp = self.h_move_sharp_gen()
        self.pitch_sub_id = self.sub_id_gen()


        def spin_rate_gen(self):
            # Measured in RPM (ranges per pitch type prob make sense)
            ''

        def spin_eff_gen(self):
            # 20-80 Grade (random gen?)
            ''

        def hand_pos_gen(self):
            # 0-100 hidden until on team
            ''

        def velo_con_gen(self):
            # 20-80 Grade
            ''

        def mound_pos_gen(self):
            # random but tight range, 0 - 100
            ''

        def release_gen(self):
            # probably make sense to be generated together
            #calc includes mound pos
            return [0][0]
        
        def vert_move_sharp_gen(self):
            # 20-80 grade, replaces 'feel'
            ''

        def delivery_eff_gen(self):
            # 0-100, frame max equivalent
            ''

        def h_move_gen(self, velo):
            # measured in inches
            # calc will factor in spin rate/eff, release y, mound/hand pos, pitcher velo grade
            ''

        def h_move_sharp_gen(self):
            # 20-80 grade, replaces 'feel'
            ''

        def sub_id_gen(self, velo):
            # identifies a slider from curveball, for example
            # calc includes pitcher velo grade, pitch type id, h/v movement
            ''




    
   