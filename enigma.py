from rotors import rotors as m4rotors

class enigma_m4:
    '''midgård'''
    def __init__(self, rotor_info):
        self.rotor_dict = {
            "r1" : m4rotors.m3m4(rotor_info['r1'][0], rotor_info['r1'][1]),
            "r2" : m4rotors.m3m4(rotor_info['r2'][0], rotor_info['r2'][1]),
            "r3" : m4rotors.m3m4(rotor_info['r3'][0], rotor_info['r3'][1]),
            "r4" : m4rotors.m3m4(rotor_info['r4'][0], rotor_info['r4'][1]),
            "r5" : m4rotors.m3m4(rotor_info['r5'][0], rotor_info['r5'][1]),
            "r6" : m4rotors.m4(rotor_info['r6'][0], rotor_info['r6'][1], rotor_info['r6'][2]),
            "r7" : m4rotors.m4(rotor_info['r7'][0], rotor_info['r7'][1], rotor_info['r7'][2]),
            "r8" : m4rotors.m4(rotor_info['r8'][0], rotor_info['r8'][1], rotor_info['r8'][2]),
            "rUKWc" : m4rotors.reflectors(rotor_info['rUKWc']),
            "rUKWb" : m4rotors.reflectors(rotor_info['rUKWb']),
            "rBeta" : m4rotors.greek(rotor_info['rBeta']),
            "rGamma" : m4rotors.greek(rotor_info['rGamma'])
        }
        self.plug_board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])


    def plug_board(self, plug_list):
        self.plugboard1 = m4rotors.plugboard(plug_list)

    def select_rotor1(self, rotor_pos1):
        self.reset_rotation()
        self.sel_rotor1 = self.rotor_dict[rotor_pos1]
        self.reset_rotation()

    def select_rotor2(self, rotor_pos2):
        self.reset_rotation()
        self.sel_rotor2 = self.rotor_dict[rotor_pos2]
        self.reset_rotation()

    def select_rotor3(self, rotor_pos3):
        self.reset_rotation()
        self.sel_rotor3 = self.rotor_dict[rotor_pos3]
        self.reset_rotation()

    def select_rotor_greek(self, rotor_pos_greek):
        self.reset_rotation()
        self.sel_rotor_greek = self.rotor_dict[rotor_pos_greek]
        self.reset_rotation()

    def select_rotor_reflector(self, rotor_pos_reflector):
        self.sel_rotor_reflector = self.rotor_dict[rotor_pos_reflector]
        self.reset_rotation()

    def man_rotor1_rotation(self, rotor_pos1_rotation):
        self.man_rotation1 = rotor_pos1_rotation
        self.reset_rotation()

    def man_rotor2_rotation(self, rotor_pos2_rotation):
        self.man_rotation2 = rotor_pos2_rotation
        self.reset_rotation()

    def man_rotor3_rotation(self, rotor_pos3_rotation):
        self.man_rotation3 = rotor_pos3_rotation
        self.reset_rotation()

    def man_rotor_greek_rotation(self, rotor_pos_greek_rotation):
        self.man_rotation_greek = rotor_pos_greek_rotation
        self.reset_rotation()

    def rotor1_ring_setting(self, rotor_pos1_ring):
        self.ring_setting1 = rotor_pos1_ring
        self.reset_rotation()

    def rotor2_ring_setting(self, rotor_pos2_ring):
        self.ring_setting2 = rotor_pos2_ring
        self.reset_rotation()

    def rotor3_ring_setting(self, rotor_pos3_ring):
        self.ring_setting3 = rotor_pos3_ring
        self.reset_rotation()

    def rotor_greek_ring_setting(self, rotor_pos_greek_ring):
        self.ring_setting_greek = rotor_pos_greek_ring
        self.reset_rotation()

    def reset_rotation(self):
        self.pos1_rotations = 0
        self.neighbour_rot1 = 0
        self.neighbour_rot2 = 0

    def signal(self, key):
        self.pos1_rotations += 1
        self.sel_rotor1.rotor_rotation(man_rotation = self.man_rotation1, ring_setting = self.ring_setting1, order = 1, amount = self.pos1_rotations)
        self.neighbour_rot1 += self.sel_rotor1.neighbour
        self.sel_rotor2.rotor_rotation(man_rotation = self.man_rotation2, ring_setting = self.ring_setting2, order = 2, previous_rotor = self.neighbour_rot1)
        self.neighbour_rot2 += self.sel_rotor2.neighbour
        self.sel_rotor3.rotor_rotation(man_rotation = self.man_rotation3, ring_setting = self.ring_setting3, order = 3, previous_rotor = self.neighbour_rot2)
        self.sel_rotor_greek.rotor_rotation(self.man_rotation_greek, self.ring_setting_greek)
        m4rotors.ring_increase(m4rotors, self.sel_rotor1, self.sel_rotor2, self.sel_rotor3, self.sel_rotor_greek, self.ring_setting1,self.ring_setting2, self.ring_setting3, self.ring_setting_greek)

        plugc = self.check_value(self.plugboard1.circuit[key]+self.sel_rotor1.rotation)
        mo1c = self.check_value(self.sel_rotor1.circuit2[plugc]+self.sel_rotor2.rotation-self.sel_rotor1.rotation-self.ring_setting1)
        mo2c = self.check_value(self.sel_rotor2.circuit2[mo1c]+self.sel_rotor3.rotation-self.sel_rotor2.rotation-self.ring_setting2)
        mo3c = self.check_value(self.sel_rotor3.circuit2[mo2c]+self.sel_rotor_greek.rotation-self.sel_rotor3.rotation-self.ring_setting3)
        grc = self.check_value(self.sel_rotor_greek.circuit2[mo3c]-self.sel_rotor_greek.rotation-self.ring_setting_greek)
        rrc =  self.check_value(self.sel_rotor_reflector.circuit[grc]+self.sel_rotor_greek.rotation+self.ring_setting_greek)
        gr_index = self.check_value(self.sel_rotor_greek.circuit2.index(rrc)-self.sel_rotor_greek.rotation+self.sel_rotor3.rotation+self.ring_setting3)
        mo3_index = self.check_value(self.sel_rotor3.circuit2.index(gr_index)-self.sel_rotor3.rotation+self.sel_rotor2.rotation+self.ring_setting2)
        mo2_index = self.check_value(self.sel_rotor2.circuit2.index(mo3_index)-self.sel_rotor2.rotation+self.sel_rotor1.rotation+self.ring_setting1)
        mo1_index = self.check_value(self.sel_rotor1.circuit2.index(mo2_index)-self.sel_rotor1.rotation)
        self.encrypted_signal = self.plugboard1.circuit.index(mo1_index)

    def check_value(self, val):
        if val > 25:
            return val%26
        elif val < 0:
            return 26-(val*-1)
        else:
            return val
