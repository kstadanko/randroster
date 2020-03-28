import csv

path = "head coach original roster.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)

data = []
for row in reader:

    # Contract Info
    salary1 = int(row[0])           #PSA0
    bonus1 = int(row[1])            #PSB0
    salary2 = int(row[2])           #PSA1
    bonus2 = int(row[3])            #PSB1
    salary3 = int(row[4])           #PSA2
    bonus3 = int(row[5])            #PSB2
    salary4 = int(row[6])           #PSA3
    bonus4 = int(row[7])            #PSB3
    salary5 = int(row[8])           #PSA4
    bonus5 = int(row[9])            #PSB4
    salary6 = int(row[10])          #PSA5
    bonus6 = int(row[11])           #PSB5
    salary7 = int(row[12])          #PSA6
    bonus7 = int(row[13])           #PSB6

    # Body Definition
    ankle_def = int(row[14])        #BSAA
    butt_def = int(row[15])         #BSBA
    calf_def = int(row[16])         #BSCA
    unknown1 = int(row[17])         #PBDA
    foot_def = int(row[18])         #BSFA
    gut_def = int(row[19])          #BSGA
    left_hand = int(row[20])        #PLHA
    unknown2 = int(row[21])         #TLHA
    right_hand = int(row[22])       #PRHA
    unknown3 = int(row[23])         #TRHA

    throw_acc = int(row[24])        #PTHA

    # Player Names
    first_name = row[25]            #PFNA
    last_name = row[26]             #PLNA

    pad_def = int(row[27])          #BSPA
    current_salary = int(row[28])   #PCSA
    stiff_arm = int(row[29])        #PLSA
    shoulder_def = int(row[30])     #BSSA
    total_salary = int(row[31])     #PTSA


    data.append([salary1, bonus1, salary2, bonus2, salary3, bonus3, salary4, bonus4, salary5, bonus5, salary6, bonus6,
                 salary7, bonus7, ankle_def, butt_def, calf_def, unknown1, foot_def, gut_def, left_hand, unknown2,
                 right_hand, unknown3, throw_acc, first_name, last_name, pad_def, current_salary, stiff_arm,
                 shoulder_def, total_salary])

print(data[0])