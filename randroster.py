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

    # Player Name
    first_name = row[25]            #PFNA
    last_name = row[26]             #PLNA

    pad_def = int(row[27])          #BSPA
    current_salary = int(row[28])   #PCSA
    stiff_arm = int(row[29])        #PLSA
    shoulder_def = int(row[30])     #BSSA
    total_salary = int(row[31])     #PTSA
    thigh_def = int(row[32])        #BSTA
    stamina = int(row[33])          #PSTA
    waist_def = int(row[34])        #BSWA
    impact_block = int(row[35])     #PLIB
    pro_bowl = int(row[36])         #PFPB
    player_signing_bonus = int(row[37]) #PVSB
    kick_acc = int(row[38])         #PKAC
    unknown4 = int(row[39])         #PLAC
    unknown5 = int(row[40])         #PRAC
    acceleration = int(row[41])     #PACC
    unknown6 = int(row[42])         #PHDC
    unknown7 = int(row[43])         #PLLC
    man_coverage = int(row[44])     #PLMC
    mouthpiece = int(row[45])       #PMPC
    unknown8 = int(row[46])         #PTRC
    spec_catch = int(row[47])       #PLSC
    zone_coverage = int(row[48])    #PLZC
    player_id = int(row[49])        #PGID
    team_id = int(row[50])          #TGID
    original_id = int(row[51])      #POID
    unknown9 = int(row[52])         #PUND
    speed = int(row[53])            #PSPD
    age = int(row[54])              #PAGE
    player_face = int(row[55])      #PGHE
    player_head = int(row[56])      #PUHE
    press_coverage = int(row[57])   #PLPE
    nasal_strip = int(row[58])      #PBRE
    unknown10 = int(row[59])        #PRSE
    eye_paint = int(row[60])        #PEYE
    unknown11 = int(row[61])        #PCAF
    pass_blk_footwork = int(row[62])    #PPBF
    run_blk_footwork = int(row[63])     #PRBF
    unknown12 = int(row[64])            #PSEF
    unknown13 = int(row[65])            #PCUF
    block_shedding = int(row[66])       #PBSG
    toughness = int(row[67])            #PTGH
    skin_color = int(row[68])           #PCPH
    left_shoe = int(row[69])            #PLSH
    right_shoe = int(row[70])           #PRSH
    catch = int(row[71])                #PCTH
    left_knee = int(row[72])            #PLTH
    right_knee = int(row[73])           #PRTH
    catch_traffic = int(row[74])        #PLCI
    agility = int(row[75])              #PAGI
    skin_tone = int(row[76])            #PSKI
    draft_pick_num = int(row[77])       #PDPI
    acquired_from = int(row[78])        #PPTI
    injury = int(row[79])               #PINJ
    tackle = int(row[80])               #PTAK
    pass_block = int(row[81])           #PPBK
    run_block = int(row[82])            #PRBK
    neck_pad = int(row[83])             #PNEK
    face_mask = int(row[84])            #PFMK
    unknown14 = int(row[85])            #PTAL
    hair_color = int(row[86])           #PHCL
    unknown15 = int(row[87])            #PUCL
    celebration = int(row[88])          #PCEL
    left_elbow = int(row[89])           #PLEL
    unknown16 = int(row[90])            #TLEL
    right_elbow = int(row[91])          #PREL
    unknown17 = int(row[92])            #TREL
    college = int(row[93])              #PCOL
    player_role_id = int(row[94])       #PROL
    left_ankle = int(row[95])           #PSPL
    release = int(row[96])              #PLRL
    sleeves = int(row[97])              #PGSL
    unknown18 = int(row[98])            #PTSL
    years_left = int(row[99])           #PCYL
    juke = int(row[100])                #PLJM
    helmet = int(row[101])              #PHLM
    spin_move = int(row[102])           #PLSM
    unknown19 = int(row[103])           #PSTM
    preferred_hand = int(row[104])      #PHAN
    jersey_number = int(row[105])       #PJEN
    player_tendency = int(row[106])     #PTEN
    left_knee2 = int(row[107])          #PLKN
    right_knee2 = int(row[108])         #PRKN
    orig_contract_years = int(row[109]) #PCON
    unknown20 = int(row[110])           #PLRN
    homestate = int(row[111])           #PHSN
    hometown = row[112]                 #PHTN
    signing_bonus = int(row[113])       #PSBO
    contract_years = int(row[114])      #PVCO
    holdout = int(row[115])             #PFHO
    unknown21 = int(row[116])           #PBMO
    round_drafted = int(row[117])       #PDRO
    throw_power = int(row[118])         #PTHP
    importance = int(row[119])          #PIMP
    jump = int(row[120])                #PJMP
    years_pro = int(row[121])           #PYRP
    portrait_id = int(row[122])         #PSXP
    carry = int(row[123])               #PCAR
    #PTAR DU

    data.append([salary1, bonus1, salary2, bonus2, salary3, bonus3, salary4, bonus4, salary5, bonus5, salary6, bonus6,
                 salary7, bonus7, ankle_def, butt_def, calf_def, unknown1, foot_def, gut_def, left_hand, unknown2,
                 right_hand, unknown3, throw_acc, first_name, last_name, pad_def, current_salary, stiff_arm,
                 shoulder_def, total_salary, thigh_def, stamina, waist_def, impact_block, pro_bowl, player_signing_bonus,
                 kick_acc, unknown4, unknown5, acceleration, unknown6, unknown7, man_coverage, mouthpiece, unknown8,
                 spec_catch, zone_coverage, player_id, team_id, original_id, unknown9, speed, age, player_face,
                 player_head, press_coverage, nasal_strip, unknown10, eye_paint, unknown11, pass_blk_footwork,
                 run_blk_footwork, unknown12, unknown13, block_shedding, toughness, skin_color, left_shoe, right_shoe,
                 catch, left_knee, right_knee, catch_traffic, agility, skin_tone, draft_pick_num, acquired_from,
                 injury, tackle, pass_block, run_block, neck_pad, face_mask, unknown14, hair_color, unknown15,
                 celebration, left_elbow, unknown16, right_elbow, unknown17, college, player_role_id, left_ankle,
                 release, sleeves, unknown18, years_left, juke, helmet, spin_move, unknown19, preferred_hand,
                 jersey_number, player_tendency, left_knee2, right_knee2, orig_contract_years, unknown20,
                 homestate, hometown, signing_bonus, contract_years, holdout, unknown21, round_drafted, throw_power,
                 importance, jump, years_pro, portrait_id, carry])

print(data[0])