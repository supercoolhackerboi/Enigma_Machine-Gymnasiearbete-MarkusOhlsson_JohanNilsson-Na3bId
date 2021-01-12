from tkinter import *
from enigma import enigma_m4
from rotors import rotors as m4rotors

'''frontend'''

rotor_info = {
    #switchable rotors 1 to 5 used by both m3 and m4 + 6 to 8 used only by m4. lets fucking go
    "r1": [[4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9], 16], #rotates regurlarly after the letter Q(notch)
    "r2": [[0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4], 4], #rotates regurlarly after the letter E(notch)
    "r3": [[1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14], 21], #rotates regurlarly after the letter V(notch)
    "r4": [[4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1], 9], #rotates regurlarly after the letter J(notch)
    "r5": [[21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10], 25], #rotates regurlarly after the letter Z(notch)
    "r6": [[9, 15, 6, 21, 14, 20, 12, 5, 24, 16, 1, 4, 13, 7, 25, 17, 3, 10, 0, 18, 23, 11, 8, 2, 19, 22], 25, 12], #rotates regurlarly after the letters Z and M(notches)
    "r7": [[13, 25, 9, 7, 6, 17, 2, 23, 12, 24, 18, 22, 1, 14, 20, 5, 0, 8, 21, 11, 15, 4, 10, 16, 3, 19], 25, 12], #rotates regurlarly after the letters Z and M(notches)
    "r8": [[5, 10, 16, 7, 19, 11, 23, 14, 2, 1, 9, 18, 15, 3, 25, 17, 0, 12, 4, 22, 13, 8, 20, 24, 6, 21], 25, 12], #rotates regurlarly after the letters Z and M(notches)
    #Thin disc reflectors b and c.
    "rUKWc": [17, 3, 14, 1, 9, 13, 19, 10, 21, 4, 7, 12, 11, 5, 2, 22, 25, 0, 23, 6, 24, 8, 15, 18, 20, 16], 
    "rUKWb": [4, 13, 10, 16, 0, 20, 24, 22, 9, 8, 2, 14, 15, 1, 11, 12, 3, 23, 25, 21, 5, 19, 7, 17, 6, 18],
    #Greek wheel rotors beta and gamma.
    "rBeta": [11, 4, 24, 9, 21, 2, 13, 8, 23, 22, 15, 1, 16, 12, 3, 17, 19, 0, 10, 25, 6, 5, 20, 7, 14, 18],
    "rGamma": [5, 18, 14, 10, 0, 13, 20, 4, 17, 7, 12, 1, 19, 8, 24, 2, 22, 11, 16, 15, 25, 23, 21, 6, 9, 3]
}

enigma_m4 = enigma_m4(rotor_info)

#lägg till ring setting och rotation i rotor_info och plugboard osv.
#fixa variablar in i rotor rotation. De behöver inte vara lika med resp. namn.
#fixa ringsetting i signal.
#fixa negativa tal efter typ 1.5 varv

root = Tk()
root.title('Enigma Simulation')


# Root

# Globals
prevRotorNum1 = 10
prevRotorNum2 = 10
prevRotorNum3 = 10

r1TEST = 0
r2TEST = 0
r3TEST = 0
zwTEST = 0
ukwTEST = 0

rotorList = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8']
alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

pos1Start = 'A'
pos2Start = 'A'
pos3Start = 'A'
zwUkwStart = 'A'
pos1RingSetting = 1
pos2RingSetting = 1
pos3RingSetting = 1
zwUkwRingSetting = 1

prevOutput = 0

turnoverRotationPos1 = 0
turnoverRotationPos2 = 0
turnoverRotationPos3 = 0

# Defining tkinter variables
rotorMenuText1 = StringVar()
rotorMenuText1.set('Rotor position 1')
rotorMenuText2 = StringVar()
rotorMenuText2.set('Rotor position 2')
rotorMenuText3 = StringVar()
rotorMenuText3.set('Rotor position 3')

zwText = StringVar()
zwText.set('Thin')

ukwText = StringVar()
ukwText.set('Reflector')


# Defining rotor functions
# Rotor Choice
def rotorChoice1(rotorNum1):
    global prevRotorNum1
    global rotor1
    global r1TEST
    rotorRoman = rotorNum1
    if rotorRoman == 1:
        rotorRoman = 'I'
    if rotorRoman == 2:
        rotorRoman = 'II'
    if rotorRoman == 3:
        rotorRoman = 'III'
    if rotorRoman == 4:
        rotorRoman = 'IV'
    if rotorRoman == 5:
        rotorRoman = 'V'
    if rotorRoman == 6:
        rotorRoman = 'VI'
    if rotorRoman == 7:
        rotorRoman = 'VII'
    if rotorRoman == 8:
        rotorRoman = 'VIII'
    rotorMenuText1.set(f'Rotor {rotorRoman}')
    rotor_choice1.menu.entryconfig(prevRotorNum1 - 1, state=ACTIVE)
    rotor_choice2.menu.entryconfig(prevRotorNum1 - 1, state=ACTIVE)
    rotor_choice3.menu.entryconfig(prevRotorNum1 - 1, state=ACTIVE)
    rotor_choice1.menu.entryconfig(rotorNum1 - 1, state=DISABLED)
    rotor_choice2.menu.entryconfig(rotorNum1 - 1, state=DISABLED)
    rotor_choice3.menu.entryconfig(rotorNum1 - 1, state=DISABLED)
    prevRotorNum1 = rotorNum1
    r1TEST = 1
    rotor1 = rotorList[rotorNum1 - 1]
    enigma_m4.select_rotor1(rotor1)


def rotorChoice2(rotorNum2):
    global prevRotorNum2
    global rotor2
    global r2TEST
    rotorRoman = rotorNum2
    if rotorRoman == 1:
        rotorRoman = 'I'
    if rotorRoman == 2:
        rotorRoman = 'II'
    if rotorRoman == 3:
        rotorRoman = 'III'
    if rotorRoman == 4:
        rotorRoman = 'IV'
    if rotorRoman == 5:
        rotorRoman = 'V'
    if rotorRoman == 6:
        rotorRoman = 'VI'
    if rotorRoman == 7:
        rotorRoman = 'VII'
    if rotorRoman == 8:
        rotorRoman = 'VIII'
    rotorMenuText2.set(f'Rotor {rotorRoman}')
    rotor_choice1.menu.entryconfig(prevRotorNum2 - 1, state=ACTIVE)
    rotor_choice2.menu.entryconfig(prevRotorNum2 - 1, state=ACTIVE)
    rotor_choice3.menu.entryconfig(prevRotorNum2 - 1, state=ACTIVE)
    rotor_choice1.menu.entryconfig(rotorNum2 - 1, state=DISABLED)
    rotor_choice2.menu.entryconfig(rotorNum2 - 1, state=DISABLED)
    rotor_choice3.menu.entryconfig(rotorNum2 - 1, state=DISABLED)
    prevRotorNum2 = rotorNum2
    r2TEST = 1
    rotor2 = rotorList[rotorNum2 - 1]
    enigma_m4.select_rotor2(rotor2)


def rotorChoice3(rotorNum3):
    global prevRotorNum3
    global rotor3
    global r3TEST
    rotorRoman = rotorNum3
    if rotorRoman == 1:
        rotorRoman = 'I'
    if rotorRoman == 2:
        rotorRoman = 'II'
    if rotorRoman == 3:
        rotorRoman = 'III'
    if rotorRoman == 4:
        rotorRoman = 'IV'
    if rotorRoman == 5:
        rotorRoman = 'V'
    if rotorRoman == 6:
        rotorRoman = 'VI'
    if rotorRoman == 7:
        rotorRoman = 'VII'
    if rotorRoman == 8:
        rotorRoman = 'VIII'
    rotorMenuText3.set(f'Rotor {rotorRoman}')
    rotor_choice1.menu.entryconfig(prevRotorNum3 - 1, state=ACTIVE)
    rotor_choice2.menu.entryconfig(prevRotorNum3 - 1, state=ACTIVE)
    rotor_choice3.menu.entryconfig(prevRotorNum3 - 1, state=ACTIVE)
    rotor_choice1.menu.entryconfig(rotorNum3 - 1, state=DISABLED)
    rotor_choice2.menu.entryconfig(rotorNum3 - 1, state=DISABLED)
    rotor_choice3.menu.entryconfig(rotorNum3 - 1, state=DISABLED)
    prevRotorNum3 = rotorNum3
    r3TEST = 1
    rotor3 = rotorList[rotorNum3 - 1]
    enigma_m4.select_rotor3(rotor3)


def zwChoice(zwNum):
    global zw
    global zwTEST
    if zwNum == 1:
        zwText.set('Gamma')
        zwTEST = 1
        zw = 'rGamma'
        enigma_m4.select_rotor_greek(zw)
    if zwNum == 2:
        zwTEST = 1
        zwText.set('Beta')
        zw = 'rBeta'
        enigma_m4.select_rotor_greek(zw)
    

def ukwChoice(ukwNum):
    global ukwTEST
    global ukw
    if ukwNum == 1:
        ukwText.set('UKW-B')
        ukwTEST = 1
        ukw = 'rUKWb'
        enigma_m4.select_rotor_reflector(ukw)
    if ukwNum == 2:
        ukwText.set('UKW-C')
        ukwTEST = 1
        ukw = 'rUKWc'
        enigma_m4.select_rotor_reflector(ukw)
    

# Turnover
def pos1TurnoverGet():
    pos1Test = (pos1Turnover.get())
    if len(pos1Test) > 1 or len(pos1Test) < 1 or type(pos1Test) == int:
        print('Starting position for rotor must be ONE letter!')
    else:
        global pos1Start
        pos1StartAlph = pos1Test.upper()
        pos1Start = alphabetList.index(pos1StartAlph)
        enigma_m4.man_rotor1_rotation(pos1Start)
        

def pos2TurnoverGet():
    pos2Test = (pos2Turnover.get())
    if len(pos2Test) > 1 or len(pos2Test) < 1 or type(pos2Test) == int:
        print('Starting position for rotor must be ONE letter!')
    else:
        global pos2Start
        pos2StartAlph = pos2Test.upper()
        pos2Start = alphabetList.index(pos2StartAlph)
        enigma_m4.man_rotor2_rotation(pos2Start)


def pos3TurnoverGet():
    pos3Test = (pos3Turnover.get())
    if len(pos3Test) > 1 or len(pos3Test) < 1 or type(pos3Test) == int:
        print('Starting position for rotor must be ONE letter!')
    else:
        global pos3Start
        pos3StartAlph = pos3Test.upper()
        pos3Start = alphabetList.index(pos3StartAlph)
        enigma_m4.man_rotor3_rotation(pos3Start)
        

def zwUkwTurnoverGet():
    zwUkwTest = (zwUkwTurnover.get())
    if len(zwUkwTest) > 1 or len(zwUkwTest) < 1 or type(zwUkwTest) == int:
        print('Starting position for rotor must be ONE letter!')
    else:
        global zwUkwStart
        zwUkwStartAlph = zwUkwTest.upper()
        zwUkwStart = alphabetList.index(zwUkwStartAlph)
        enigma_m4.man_rotor_greek_rotation(zwUkwStart)



# Ring Setting
def pos1RingGet():
    pos1Test = int((pos1Ring.get()))
    if type(pos1Test) == str or pos1Test < 1 or pos1Test > 26:
        print('Ring setting must be a number between 1-26!')
    else:
        global pos1RingSetting
        pos1RingSetting = pos1Test
        enigma_m4.rotor1_ring_setting(pos1RingSetting - 1)


def pos2RingGet():
    pos2Test = int((pos2Ring.get()))
    if type(pos2Test) == str or pos2Test < 1 or pos2Test > 26:
        print('Ring setting must be a number between 1-26!')
    else:
        global pos2RingSetting
        pos2RingSetting = pos2Test
        enigma_m4.rotor2_ring_setting(pos2RingSetting - 1)


def pos3RingGet():
    pos3Test = int((pos3Ring.get()))
    if type(pos3Test) == str or pos3Test < 1 or pos3Test > 26:
        print('Ring setting must be a number between 1-26!')
    else:
        global pos3RingSetting
        pos3RingSetting = pos3Test
        enigma_m4.rotor3_ring_setting(pos3RingSetting - 1)


def zwUkwRingGet():
    test = int((zwUkwRing.get()))
    if type(test) == str or test < 1 or test > 26:
        print('Ring setting must be a number between 1-26!')
    else:
        global zwUkwRingSetting
        zwUkwRingSetting = test
        enigma_m4.rotor_greek_ring_setting(zwUkwRingSetting - 1)


# Defining key functions
def keyStroke(key):
    if r1TEST == 0 or r2TEST == 0 or r3TEST == 0 or zwTEST == 0 or ukwTEST == 0:
        print('All rotors must be selected')
    else:
        enigma_m4.signal(key)
        output()
        ringPos1 = int((pos1Ring.get()))
        turnoverRotationPos1 = (pos1Turnover.get())
        turnoverRotPos1Num = alphabetList.index(turnoverRotationPos1.upper()) + ringPos1
        if turnoverRotPos1Num >= 26:
            add = turnoverRotPos1Num - 26
            turnoverRotPos1Num = 0 + add
            ringPos2 = int((pos2Ring.get()))
            turnoverRotationPos2 = (pos2Turnover.get())
            turnoverRotPos2Num = alphabetList.index(turnoverRotationPos2.upper()) + ringPos2
            if turnoverRotPos2Num >= 26:
                add = turnoverRotPos2Num - 26
                turnoverRotPos2Num = 0 + add
                ringPos3 = int((pos3Ring.get()))
                turnoverRotationPos3 = (pos3Turnover.get())
                turnoverRotPos3Num = alphabetList.index(turnoverRotationPos3.upper()) + ringPos3
                if turnoverRotPos3Num >= 26:
                    add = turnoverRotPos3Num - 26
                    turnoverRotPos3Num = 0 + add
                turnoverRotationPos3 = alphabetList[turnoverRotPos3Num]
                pos3Turnover.delete(0, END)
                pos3Turnover.insert(0, turnoverRotationPos3)
            turnoverRotationPos2 = alphabetList[turnoverRotPos2Num]
            pos2Turnover.delete(0, END)
            pos2Turnover.insert(0, turnoverRotationPos2)
        turnoverRotationPos1 = alphabetList[turnoverRotPos1Num]
        pos1Turnover.delete(0, END)
        pos1Turnover.insert(0, turnoverRotationPos1)
        


# Output function
def output():
    global prevOutput
    outputList = [outputLabelA, outputLabelB, outputLabelC, outputLabelD, outputLabelE, outputLabelF, outputLabelG, outputLabelH, outputLabelI, outputLabelJ, outputLabelK, outputLabelL, outputLabelM, outputLabelN, outputLabelO, outputLabelP, outputLabelQ, outputLabelR, outputLabelS, outputLabelT, outputLabelU, outputLabelV, outputLabelW, outputLabelX, outputLabelY, outputLabelZ]
    outputShow = outputList[prevOutput]
    outputShow['bg'] = 'green'
    outputShow = outputList[enigma_m4.encrypted_signal]
    outputShow['bg'] = 'yellow'
    prevOutput = enigma_m4.encrypted_signal



# Defining the miscellaneous buttons

quitButton = Button(root, text='Quit', padx=33, pady=5, command=root.quit)
testButton = Button(root, text='Test', padx=33, pady=5, command=output)

# Defining rotor buttons

rotor_choice1 = Menubutton(root, relief=RAISED, textvariable=rotorMenuText1)
rotor_choice2 = Menubutton(root, relief=RAISED, textvariable=rotorMenuText2)
rotor_choice3 = Menubutton(root, relief=RAISED, textvariable=rotorMenuText3)

ZW = Menubutton(root, relief=RAISED, textvariable=zwText)

UKW = Menubutton(root, relief=RAISED, textvariable=ukwText)

pos1Turnover = Entry(root, width=2)
pos1TurnoverPass = Button(root, text='Turnover', command=pos1TurnoverGet)
pos2Turnover = Entry(root, width=2)
pos2TurnoverPass = Button(root, text='Turnover', command=pos2TurnoverGet)
pos3Turnover = Entry(root, width=2)
pos3TurnoverPass = Button(root, text='Turnover', command=pos3TurnoverGet)
zwUkwTurnover = Entry(root, width=2)
zwUkwTurnoverPass = Button(root, text='Turnover', command=zwUkwTurnoverGet)

pos1Ring = Entry(root, width=2)
pos1RingPass = Button(root, text='Ring Setting', command=pos1RingGet)
pos2Ring = Entry(root, width=2)
pos2RingPass = Button(root, text='Ring Setting', command=pos2RingGet)
pos3Ring = Entry(root, width=2)
pos3RingPass = Button(root, text='Ring Setting', command=pos3RingGet)
zwUkwRing = Entry(root, width=2)
zwUkwRingPass = Button(root, text='Ring Setting', command=zwUkwRingGet)

# Defining keys

buttonA = Button(root, text='A', bg='green', padx=41, pady=34, command=lambda: keyStroke(0))
buttonB = Button(root, text='B', bg='green', padx=41, pady=34, command=lambda: keyStroke(1))
buttonC = Button(root, text='C', bg='green', padx=40, pady=34, command=lambda: keyStroke(2))
buttonD = Button(root, text='D', bg='green', padx=41, pady=34, command=lambda: keyStroke(3))
buttonE = Button(root, text='E', bg='green', padx=42, pady=34, command=lambda: keyStroke(4))
buttonF = Button(root, text='F', bg='green', padx=41, pady=34, command=lambda: keyStroke(5))
buttonG = Button(root, text='G', bg='green', padx=40, pady=34, command=lambda: keyStroke(6))
buttonH = Button(root, text='H', bg='green', padx=40, pady=34, command=lambda: keyStroke(7))
buttonI = Button(root, text='I', bg='green', padx=43, pady=34, command=lambda: keyStroke(8))
buttonJ = Button(root, text='J', bg='green', padx=42, pady=34, command=lambda: keyStroke(9))
buttonK = Button(root, text='K', bg='green', padx=41, pady=34, command=lambda: keyStroke(10))
buttonL = Button(root, text='L', bg='green', padx=41, pady=34, command=lambda: keyStroke(11))
buttonM = Button(root, text='M', bg='green', padx=39, pady=34, command=lambda: keyStroke(12))
buttonN = Button(root, text='N', bg='green', padx=39, pady=34, command=lambda: keyStroke(13))
buttonO = Button(root, text='O', bg='green', padx=40, pady=34, command=lambda: keyStroke(14))
buttonP = Button(root, text='P', bg='green', padx=41, pady=34, command=lambda: keyStroke(15))
buttonQ = Button(root, text='Q', bg='green', padx=41, pady=34, command=lambda: keyStroke(16))
buttonR = Button(root, text='R', bg='green', padx=41, pady=34, command=lambda: keyStroke(17))
buttonS = Button(root, text='S', bg='green', padx=42, pady=34, command=lambda: keyStroke(18))
buttonT = Button(root, text='T', bg='green', padx=41, pady=34, command=lambda: keyStroke(19))
buttonU = Button(root, text='U', bg='green', padx=40, pady=34, command=lambda: keyStroke(20))
buttonV = Button(root, text='V', bg='green', padx=40, pady=34, command=lambda: keyStroke(21))
buttonW = Button(root, text='W', bg='green', padx=40, pady=34, command=lambda: keyStroke(22))
buttonX = Button(root, text='X', bg='green', padx=41, pady=34, command=lambda: keyStroke(23))
buttonY = Button(root, text='Y', bg='green', padx=41, pady=34, command=lambda: keyStroke(24))
buttonZ = Button(root, text='Z', bg='green', padx=41, pady=34, command=lambda: keyStroke(25))

# Defining output

outputSeparator = Label(root, text='Output', bg='green', padx=128, pady=15)

outputLabelA = Label(root, text='A', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelB = Label(root, text='B', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelC = Label(root, text='C', bg='green', padx=40, pady=34, relief=RAISED)
outputLabelD = Label(root, text='D', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelE = Label(root, text='E', bg='green', padx=42, pady=34, relief=RAISED)
outputLabelF = Label(root, text='F', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelG = Label(root, text='G', bg='green', padx=40, pady=34, relief=RAISED)
outputLabelH = Label(root, text='H', bg='green', padx=40, pady=34, relief=RAISED)
outputLabelI = Label(root, text='I', bg='green', padx=43, pady=34, relief=RAISED)
outputLabelJ = Label(root, text='J', bg='green', padx=42, pady=34, relief=RAISED)
outputLabelK = Label(root, text='K', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelL = Label(root, text='L', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelM = Label(root, text='M', bg='green', padx=39, pady=34, relief=RAISED)
outputLabelN = Label(root, text='N', bg='green', padx=39, pady=34, relief=RAISED)
outputLabelO = Label(root, text='O', bg='green', padx=40, pady=34, relief=RAISED)
outputLabelP = Label(root, text='P', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelQ = Label(root, text='Q', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelR = Label(root, text='R', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelS = Label(root, text='S', bg='green', padx=42, pady=34, relief=RAISED)
outputLabelT = Label(root, text='T', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelU = Label(root, text='U', bg='green', padx=40, pady=34, relief=RAISED)
outputLabelV = Label(root, text='V', bg='green', padx=40, pady=34, relief=RAISED)
outputLabelW = Label(root, text='W', bg='green', padx=40, pady=34, relief=RAISED)
outputLabelX = Label(root, text='X', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelY = Label(root, text='Y', bg='green', padx=41, pady=34, relief=RAISED)
outputLabelZ = Label(root, text='Z', bg='green', padx=41, pady=34, relief=RAISED)


# Placing the misc. buttons on the screen
# Row 0

quitButton.grid(row=0, column=0, rowspan=3)
#testButton.grid(row=0, column=1, rowspan=3)

# Placing the rotor buttons on the screen
# Row 0
# Rotor pos 1
rotor_choice1.grid(row=0, column=6)
rotor_choice1.menu = Menu(rotor_choice1, tearoff = 0)
rotor_choice1['menu'] = rotor_choice1.menu
rotor_choice1.menu.add_command(label='Rotor I', command=lambda: rotorChoice1(1), state=ACTIVE)
rotor_choice1.menu.add_command(label='Rotor II', command=lambda: rotorChoice1(2), state=ACTIVE)
rotor_choice1.menu.add_command(label='Rotor III', command=lambda: rotorChoice1(3), state=ACTIVE)
rotor_choice1.menu.add_command(label='Rotor IV', command=lambda: rotorChoice1(4), state=ACTIVE)
rotor_choice1.menu.add_command(label='Rotor V', command=lambda: rotorChoice1(5), state=ACTIVE)
rotor_choice1.menu.add_command(label='Rotor VI', command=lambda: rotorChoice1(6), state=ACTIVE)
rotor_choice1.menu.add_command(label='Rotor VII', command=lambda: rotorChoice1(7), state=ACTIVE)
rotor_choice1.menu.add_command(label='Rotor VIII', command=lambda: rotorChoice1(8), state=ACTIVE)
rotor_choice1.menu.add_separator()
rotor_choice1.menu.add_radiobutton(label='Choose rotor', state=DISABLED)

# Rotor pos 2
rotor_choice2.grid(row=0, column=5)
rotor_choice2.menu = Menu(rotor_choice2, tearoff = 0)
rotor_choice2['menu'] = rotor_choice2.menu
rotor_choice2.menu.add_command(label='Rotor I', command=lambda: rotorChoice2(1), state=ACTIVE)
rotor_choice2.menu.add_command(label='Rotor II', command=lambda: rotorChoice2(2), state=ACTIVE)
rotor_choice2.menu.add_command(label='Rotor III', command=lambda: rotorChoice2(3), state=ACTIVE)
rotor_choice2.menu.add_command(label='Rotor IV', command=lambda: rotorChoice2(4), state=ACTIVE)
rotor_choice2.menu.add_command(label='Rotor V', command=lambda: rotorChoice2(5), state=ACTIVE)
rotor_choice2.menu.add_command(label='Rotor VI', command=lambda: rotorChoice2(6), state=ACTIVE)
rotor_choice2.menu.add_command(label='Rotor VII', command=lambda: rotorChoice2(7), state=ACTIVE)
rotor_choice2.menu.add_command(label='Rotor VIII', command=lambda: rotorChoice2(8), state=ACTIVE)
rotor_choice2.menu.add_separator()
rotor_choice2.menu.add_radiobutton(label='Choose rotor', state=DISABLED)

# Rotor pos 3
rotor_choice3.grid(row=0, column=4)
rotor_choice3.menu = Menu(rotor_choice3, tearoff = 0)
rotor_choice3['menu'] = rotor_choice3.menu
rotor_choice3.menu.add_command(label='Rotor I', command=lambda: rotorChoice3(1), state=ACTIVE)
rotor_choice3.menu.add_command(label='Rotor II', command=lambda: rotorChoice3(2), state=ACTIVE)
rotor_choice3.menu.add_command(label='Rotor III', command=lambda: rotorChoice3(3), state=ACTIVE)
rotor_choice3.menu.add_command(label='Rotor IV', command=lambda: rotorChoice3(4), state=ACTIVE)
rotor_choice3.menu.add_command(label='Rotor V', command=lambda: rotorChoice3(5), state=ACTIVE)
rotor_choice3.menu.add_command(label='Rotor VI', command=lambda: rotorChoice3(6), state=ACTIVE)
rotor_choice3.menu.add_command(label='Rotor VII', command=lambda: rotorChoice3(7), state=ACTIVE)
rotor_choice3.menu.add_command(label='Rotor VIII', command=lambda: rotorChoice3(8), state=ACTIVE)
rotor_choice3.menu.add_separator()
rotor_choice3.menu.add_radiobutton(label='Choose rotor', state=DISABLED)

# Zusatzwalze
ZW.grid(row=0, column=3)
ZW.menu = Menu(ZW, tearoff = 0)
ZW['menu'] = ZW.menu
ZW.menu.add_command(label='Gamma', command=lambda: zwChoice(1), state=ACTIVE)
ZW.menu.add_command(label='Beta', command=lambda: zwChoice(2), state=ACTIVE)
ZW.menu.add_separator()
ZW.menu.add_radiobutton(label='Choose rotor', state=DISABLED)

# Reflector
UKW.grid(row=0, column=2)
UKW.menu = Menu(UKW, tearoff = 0)
UKW['menu'] = UKW.menu
UKW.menu.add_command(label='B', command=lambda: ukwChoice(1), state=ACTIVE)
UKW.menu.add_command(label='C', command=lambda: ukwChoice(2), state=ACTIVE)
UKW.menu.add_separator()
UKW.menu.add_radiobutton(label='Choose rotor', state=DISABLED)

# Row 1
pos1Turnover.grid(row=1, column=6)
pos1TurnoverPass.grid(row=1, column=6, columnspan=2)
pos2Turnover.grid(row=1, column=5)
pos2TurnoverPass.grid(row=1, column=5, columnspan=2)
pos3Turnover.grid(row=1, column=4)
pos3TurnoverPass.grid(row=1, column=4, columnspan=2)

zwUkwTurnover.grid(row=1, column=2, columnspan=2)
zwUkwTurnoverPass.grid(row=1, column=3)

# Row 2
pos1Ring.grid(row=2, column=6)
pos1RingPass.grid(row=2, column=6, columnspan=2)
pos2Ring.grid(row=2, column=5)
pos2RingPass.grid(row=2, column=5, columnspan=2)
pos3Ring.grid(row=2, column=4)
pos3RingPass.grid(row=2, column=4, columnspan=2)

zwUkwRing.grid(row=2, column=2, columnspan=2)
zwUkwRingPass.grid(row=2, column=3)

# Placing the keys on the screen
# Row 3
buttonQ.grid(row=3, column=0)
buttonW.grid(row=3, column=1)
buttonE.grid(row=3, column=2)
buttonR.grid(row=3, column=3)
buttonT.grid(row=3, column=4)
buttonY.grid(row=3, column=5)
buttonU.grid(row=3, column=6)
buttonI.grid(row=3, column=7)
buttonO.grid(row=3, column=8)
buttonP.grid(row=3, column=9)

# Row 4
buttonA.grid(row=4, column=0)
buttonS.grid(row=4, column=1)
buttonD.grid(row=4, column=2)
buttonF.grid(row=4, column=3)
buttonG.grid(row=4, column=4)
buttonH.grid(row=4, column=5)
buttonJ.grid(row=4, column=6)
buttonK.grid(row=4, column=7)
buttonL.grid(row=4, column=8)

# Row 5
buttonZ.grid(row=5, column=1)
buttonX.grid(row=5, column=2)
buttonC.grid(row=5, column=3)
buttonV.grid(row=5, column=4)
buttonB.grid(row=5, column=5)
buttonN.grid(row=5, column=6)
buttonM.grid(row=5, column=7)

# Output
# Row 6
outputSeparator.grid(row=6, column=0, columnspan=3)

# Row 7
outputLabelQ.grid(row=7, column=0)
outputLabelW.grid(row=7, column=1)
outputLabelE.grid(row=7, column=2)
outputLabelR.grid(row=7, column=3)
outputLabelT.grid(row=7, column=4)
outputLabelY.grid(row=7, column=5)
outputLabelU.grid(row=7, column=6)
outputLabelI.grid(row=7, column=7)
outputLabelO.grid(row=7, column=8)
outputLabelP.grid(row=7, column=9)

# Row 8
outputLabelA.grid(row=8, column=0)
outputLabelS.grid(row=8, column=1)
outputLabelD.grid(row=8, column=2)
outputLabelF.grid(row=8, column=3)
outputLabelG.grid(row=8, column=4)
outputLabelH.grid(row=8, column=5)
outputLabelJ.grid(row=8, column=6)
outputLabelK.grid(row=8, column=7)
outputLabelL.grid(row=8, column=8)

# Row 9
outputLabelZ.grid(row=9, column=0)
outputLabelX.grid(row=9, column=1)
outputLabelC.grid(row=9, column=2)
outputLabelV.grid(row=9, column=3)
outputLabelB.grid(row=9, column=4)
outputLabelN.grid(row=9, column=5)
outputLabelM.grid(row=9, column=6)


# Plugboard
plugboard = Toplevel(root)
plugboard.title('Plugboard')

# Defining globals
iteration = 1
colorIteration = 0
plugboardList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# Defining functions
def connect(key):
    global iteration
    global colorIteration
    global pairColor
    global firstButtonConfig
    global firstKey
    global buttonList
    global plugboardList
    buttonList = [plugButtonA, plugButtonB, plugButtonC, plugButtonD, plugButtonE, plugButtonF, plugButtonG, plugButtonH, plugButtonI, plugButtonJ, plugButtonK, plugButtonL, plugButtonM, plugButtonN, plugButtonO, plugButtonP, plugButtonQ, plugButtonR, plugButtonS, plugButtonT, plugButtonU, plugButtonV, plugButtonW, plugButtonX, plugButtonY, plugButtonZ]
    colorList = ['blue', 'red', 'orange', 'yellow', 'pink', 'brown4', 'magenta4', 'deep sky blue', 'gray20', 'purple4', 'sienna3', 'SeaGreen2', 'brown1', 'lime green']
    if iteration == 1:
        iteration += 1
        firstButtonConfig = buttonList[key - 1]
        firstButtonConfig.flash()
        firstButtonConfig['bg'] = 'white'
        firstKey = key
    else:
        iteration -= 1
        pairColor = colorList[colorIteration]
        secondButtonConfig = buttonList[key - 1]
        secondButtonConfig.flash()
        secondButtonConfig['bg'] = pairColor
        secondButtonConfig['state'] = DISABLED
        firstButtonConfig['bg'] = pairColor
        firstButtonConfig['state'] = DISABLED
        plugboardList[plugboardList.index(key - 1)] = firstKey - 1
        plugboardList[plugboardList.index(firstKey - 1)] = key - 1
        enigma_m4.plug_board(plugboardList)
        #print(plugboardList)
        colorIteration += 1
        
def clear():
    globals()['iteration'] = 1
    globals()['colorIteration'] = 0
    globals()['plugboardList'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    print(plugboardList)
    run = TRUE
    x = 0
    while run:
        buttonConfig = buttonList[x]
        buttonConfig['state'] = NORMAL
        buttonConfig['bg'] = 'green'
        x += 1
        if x == 26:
            run = FALSE

# Defining Keys
plugButtonA = Button(plugboard, text='A', bg='green', padx=41, pady=34, command=lambda: connect(1))
plugButtonB = Button(plugboard, text='B', bg='green', padx=41, pady=34, command=lambda: connect(2))
plugButtonC = Button(plugboard, text='C', bg='green', padx=40, pady=34, command=lambda: connect(3))
plugButtonD = Button(plugboard, text='D', bg='green', padx=41, pady=34, command=lambda: connect(4))
plugButtonE = Button(plugboard, text='E', bg='green', padx=42, pady=34, command=lambda: connect(5))
plugButtonF = Button(plugboard, text='F', bg='green', padx=41, pady=34, command=lambda: connect(6))
plugButtonG = Button(plugboard, text='G', bg='green', padx=40, pady=34, command=lambda: connect(7))
plugButtonH = Button(plugboard, text='H', bg='green', padx=40, pady=34, command=lambda: connect(8))
plugButtonI = Button(plugboard, text='I', bg='green', padx=43, pady=34, command=lambda: connect(9))
plugButtonJ = Button(plugboard, text='J', bg='green', padx=42, pady=34, command=lambda: connect(10))
plugButtonK = Button(plugboard, text='K', bg='green', padx=41, pady=34, command=lambda: connect(11))
plugButtonL = Button(plugboard, text='L', bg='green', padx=41, pady=34, command=lambda: connect(12))
plugButtonM = Button(plugboard, text='M', bg='green', padx=39, pady=34, command=lambda: connect(13))
plugButtonN = Button(plugboard, text='N', bg='green', padx=39, pady=34, command=lambda: connect(14))
plugButtonO = Button(plugboard, text='O', bg='green', padx=40, pady=34, command=lambda: connect(15))
plugButtonP = Button(plugboard, text='P', bg='green', padx=41, pady=34, command=lambda: connect(16))
plugButtonQ = Button(plugboard, text='Q', bg='green', padx=41, pady=34, command=lambda: connect(17))
plugButtonR = Button(plugboard, text='R', bg='green', padx=41, pady=34, command=lambda: connect(18))
plugButtonS = Button(plugboard, text='S', bg='green', padx=42, pady=34, command=lambda: connect(19))
plugButtonT = Button(plugboard, text='T', bg='green', padx=41, pady=34, command=lambda: connect(20))
plugButtonU = Button(plugboard, text='U', bg='green', padx=40, pady=34, command=lambda: connect(21))
plugButtonV = Button(plugboard, text='V', bg='green', padx=40, pady=34, command=lambda: connect(22))
plugButtonW = Button(plugboard, text='W', bg='green', padx=40, pady=34, command=lambda: connect(23))
plugButtonX = Button(plugboard, text='X', bg='green', padx=41, pady=34, command=lambda: connect(24))
plugButtonY = Button(plugboard, text='Y', bg='green', padx=41, pady=34, command=lambda: connect(25))
plugButtonZ = Button(plugboard, text='Z', bg='green', padx=41, pady=34, command=lambda: connect(26))
clearButton = Button(plugboard, text='Clear all', bg='red', padx=20, pady=20, command=clear)


# Placing keys on the plugboard screen
# Plugboard Row 0
clearButton.grid(row=0, column=0, columnspan=10)

# Plugboard Row 1
plugButtonQ.grid(row=1, column=0)
plugButtonW.grid(row=1, column=1)
plugButtonE.grid(row=1, column=2)
plugButtonR.grid(row=1, column=3)
plugButtonT.grid(row=1, column=4)
plugButtonY.grid(row=1, column=5)
plugButtonU.grid(row=1, column=6)
plugButtonI.grid(row=1, column=7)
plugButtonO.grid(row=1, column=8)
plugButtonP.grid(row=1, column=9)

# Plugboard Row 2
plugButtonA.grid(row=2, column=0)
plugButtonS.grid(row=2, column=1)
plugButtonD.grid(row=2, column=2)
plugButtonF.grid(row=2, column=3)
plugButtonG.grid(row=2, column=4)
plugButtonH.grid(row=2, column=5)
plugButtonJ.grid(row=2, column=6)
plugButtonK.grid(row=2, column=7)
plugButtonL.grid(row=2, column=8)

# Plugboard Row 3
plugButtonZ.grid(row=3, column=1)
plugButtonX.grid(row=3, column=2)
plugButtonC.grid(row=3, column=3)
plugButtonV.grid(row=3, column=4)
plugButtonB.grid(row=3, column=5)
plugButtonN.grid(row=3, column=6)
plugButtonM.grid(row=3, column=7)


root.mainloop()
