class rotors:
    '''backend'''
    def check_value_list(self, list1, rotor):
        for x in list1:
            if list1[list1.index(x)] > 25:
                rotor.circuit3[list1.index(x)] = x%26
            elif list1[list1.index(x)] < 0:
                rotor.circuit3[list1.index(x)] = 26-(x*-1)
            else:
                rotor.circuit3[list1.index(x)] = x
        return rotor.circuit3

    def ring_increase(self, sel_rotor1, sel_rotor2, sel_rotor3, sel_rotor_greek, ring1, ring2, ring3, ringgreek):
        sel_rotor1.circuit2 = rotors.check_value_list(self, [x+ring1 for x in sel_rotor1.circuit], sel_rotor1)
        sel_rotor2.circuit2 = rotors.check_value_list(self, [x+ring2 for x in sel_rotor2.circuit], sel_rotor2)
        sel_rotor3.circuit2 = rotors.check_value_list(self, [x+ring3 for x in sel_rotor3.circuit], sel_rotor3)
        sel_rotor_greek.circuit2 = rotors.check_value_list(self, [x+ringgreek for x in sel_rotor_greek.circuit], sel_rotor_greek)
    
    class m3m4:
        def __init__(self, c, r):
            self.circuit = c
            self.notch1 = r
            self.neighbour = 0
            self.rotation = 0
            self.circuit2 = 0
            self.circuit3 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

        def rotor_rotation(self, man_rotation = 0, ring_setting = 0, order = 0, amount = 0, previous_rotor = 0):
            self.neighbour = 0
            if order == 1 and (man_rotation + amount)%26 == (self.notch1 + 1)%26:
                self.neighbour = 1
                if (man_rotation + amount - ring_setting)%26 >= 0:
                    self.rotation = man_rotation + amount - ring_setting
                else:
                    self.rotation = 26 - ((man_rotation + amount - ring_setting*-1)%26)
            elif order == 1:
                if (man_rotation + amount - ring_setting)%26 >= 0:
                    self.rotation = man_rotation + amount - ring_setting
                else:
                    self.rotation = 26 - ((man_rotation + amount - ring_setting*-1)%26)
            elif order == 2 and (man_rotation + previous_rotor)%26 == (self.notch1 + 1)%26:
                self.neighbour = 1
                if (man_rotation + previous_rotor - ring_setting)%26 >= 0:
                    self.rotation = man_rotation + previous_rotor - ring_setting
                else:
                    self.rotation = 26 - ((man_rotation + previous_rotor - ring_setting*-1)%26)
            elif order == 2:
                if (man_rotation + previous_rotor - ring_setting)%26 >= 0:
                    self.rotation = man_rotation + previous_rotor - ring_setting
                else:
                    self.rotation = 26 - ((man_rotation + previous_rotor - ring_setting*-1)%26)
            else:
                if (man_rotation + previous_rotor - ring_setting)%26 >= 0:
                    self.rotation = man_rotation + previous_rotor - ring_setting
                else:
                    self.rotation = 26 - ((man_rotation + previous_rotor - ring_setting*-1)%26)

    class m4:
        def __init__(self, c, r, p):
            self.circuit = c
            self.notch1 = r
            self.notch2 = p
            self.neighbour = 0
            self.rotation = 0
            self.circuit2 = 0
            self.circuit3 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

        def rotor_rotation(self, man_rotation = 0, ring_setting = 0, order = 0, amount = 0, previous_rotor = 0):
            self.neighbour = 0
            if order == 1 and (man_rotation + amount)%26 == (self.notch1 + 1)%26 or (man_rotation + amount)%26 == (self.notch2 + 1)%26:
                self.neighbour = 1
                if (man_rotation + amount - ring_setting)%26 >= 0:
                    self.rotation = man_rotation + amount - ring_setting
                else:
                    self.rotation = 26 - (((man_rotation + amount - ring_setting)*-1)%26)
            elif order == 1:
                if (man_rotation + amount - ring_setting)%26 >= 0:
                    self.rotation = man_rotation + amount - ring_setting
                else:
                    self.rotation = 26 - (((man_rotation + amount - ring_setting)*-1)%26)
            elif order == 2 and (man_rotation + previous_rotor)%26 == (self.notch1 + 1)%26 or (man_rotation + previous_rotor)%26 == (self.notch2 + 1)%26:
                self.neighbour = 1
                if (man_rotation + previous_rotor - ring_setting)%26 >= 0:
                    self.rotation = man_rotation + previous_rotor - ring_setting
                else:
                    self.rotation = 26 - (((man_rotation + previous_rotor - ring_setting)*-1)%26)
            elif order == 2:
                if (man_rotation + previous_rotor - ring_setting)%26 >= 0:
                    self.rotation = man_rotation + previous_rotor - ring_setting
                else:
                    self.rotation = 26 - (((man_rotation + previous_rotor - ring_setting)*-1)%26)
            else:
                if (man_rotation + previous_rotor - ring_setting)%26 >= 0:
                    self.rotation = man_rotation + previous_rotor - ring_setting
                else:
                    self.rotation = 26 - (((man_rotation + previous_rotor - ring_setting)*-1)%26)

    class greek:
        def __init__(self, c):
            self.circuit = c
            self.rotation = 0
            self.circuit2 = 0
            self.circuit3 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

        def rotor_rotation(self, man_rotation = 0, ring_setting = 0):
            if (man_rotation - ring_setting)%25 >= 0:
                self.rotation = man_rotation - ring_setting
            else:
                self.rotation = 26 - ((man_rotation - ring_setting)%25)

    class plugboard:
        def __init__(self, c):
            self.circuit = c

    class reflectors:
        def __init__(self, c):
            self.circuit = c