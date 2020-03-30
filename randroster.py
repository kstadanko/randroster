import csv
from NameGenerator import *

path = "head coach original roster.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)

data = []
for row in reader:

    # Contract Info                         Column Header
    salary1 = int(row[0])                   # PSA0
    bonus1 = int(row[1])                    # PSB0
    salary2 = int(row[2])                   # PSA1
    bonus2 = int(row[3])                    # PSB1
    salary3 = int(row[4])                   # PSA2
    bonus3 = int(row[5])                    # PSB2
    salary4 = int(row[6])                   # PSA3
    bonus4 = int(row[7])                    # PSB3
    salary5 = int(row[8])                   # PSA4
    bonus5 = int(row[9])                    # PSB4
    salary6 = int(row[10])                  # PSA5
    bonus6 = int(row[11])                   # PSB5
    salary7 = int(row[12])                  # PSA6
    bonus7 = int(row[13])                   # PSB6
    current_salary = int(row[28])           # PCSA
    total_salary = int(row[31])             # PTSA
    player_signing_bonus = int(row[37])     # PVSB
    years_left = int(row[99])               # PCYL
    orig_contract_years = int(row[109])     # PCON
    signing_bonus = int(row[113])           # PSBO
    contract_years = int(row[114])          # PVCO
    holdout = int(row[115])                 # PFHO
    player_total_salary = int(row[147])     # PVTS
    years_with_team = int(row[162])         # PYWT

    # Appearance
    ankle_def = int(row[14])                # BSAA
    butt_def = int(row[15])                 # BSBA
    calf_def = int(row[16])                 # BSCA
    foot_def = int(row[18])                 # BSFA
    gut_def = int(row[19])                  # BSGA
    left_hand = int(row[20])                # PLHA
    right_hand = int(row[22])               # PRHA
    pad_def = int(row[27])                  # BSPA
    shoulder_def = int(row[30])             # BSSA
    thigh_def = int(row[32])                # BSTA
    waist_def = int(row[34])                # BSWA
    mouthpiece = int(row[45])               # PMPC
    player_face = int(row[55])              # PGHE
    player_head = int(row[56])              # PUHE
    nasal_strip = int(row[58])              # PBRE
    eye_paint = int(row[60])                # PEYE
    skin_color = int(row[68])               # PCPH
    left_shoe = int(row[69])                # PLSH
    right_shoe = int(row[70])               # PRSH
    left_knee = int(row[72])                # PLTH
    right_knee = int(row[73])               # PRTH
    skin_tone = int(row[76])                # PSKI
    neck_pad = int(row[83])                 # PNEK
    face_mask = int(row[84])                # PFMK
    hair_color = int(row[86])               # PHCL
    left_elbow = int(row[89])               # PLEL
    right_elbow = int(row[91])              # PREL
    left_ankle = int(row[95])               # PSPL
    sleeves = int(row[97])                  # PGSL
    helmet = int(row[101])                  # PHLM
    left_knee2 = int(row[107])              # PLKN
    right_knee2 = int(row[108])             # PRKN
    sleeves2 = int(row[125])                # PJER
    right_ankle = int(row[129])             # PSPR
    left_wrist = int(row[135])              # PLWR
    right_wrist = int(row[137])             # PRWR
    visor = int(row[142])                   # PRBS
    arm_size = int(row[148])                # BSAT
    butt_size = int(row[149])               # BSBT
    calf_size = int(row[150])               # BSCT
    foot_size = int(row[151])               # BSFT
    height = int(row[152])                  # PHGT
    gut_size = int(row[153])                # BSGT
    weight = int(row[154])                  # PWGT
    pad_size = int(row[157])                # BSPT
    shoulder_size = int(row[159])           # BSST
    thigh_size = int(row[160])              # BSTT
    waist_size = int(row[161])              # BSWT

    # Player Info
    first_name = name_generator(0)          # PFNA row[25]  
    last_name = name_generator(1).title()   # PLNA row[26]
    pro_bowl = int(row[36])                 # PFPB
    player_id = int(row[49])                # PGID
    team_id = int(row[50])                  # TGID
    original_id = int(row[51])              # POID
    age = int(row[54])                      # PAGE
    draft_pick_num = int(row[77])           # PDPI
    acquired_from = int(row[78])            # PPTI
    college = int(row[93])                  # PCOL
    player_role_id = int(row[94])           # PROL
    preferred_hand = int(row[104])          # PHAN
    jersey_number = int(row[105])           # PJEN
    player_tendency = int(row[106])         # PTEN
    homestate = int(row[111])               # PHSN
    hometown = row[112]                     # PHTN
    round_drafted = int(row[117])           # PDRO
    years_pro = int(row[121])               # PYRP
    portrait_id = int(row[122])             # PSXP
    position = int(row[144])                # PPOS
    celebration = row[145]                  # PEPS
    player_audio = int(row[156])            # PCMT

    # Ratings
    throw_acc = int(row[24])                # PTHA
    stiff_arm = int(row[29])                # PLSA
    stamina = int(row[33])                  # PSTA
    impact_block = int(row[35])             # PLIB
    kick_acc = int(row[38])                 # PKAC
    acceleration = int(row[41])             # PACC
    man_coverage = int(row[44])             # PLMC
    spec_catch = int(row[47])               # PLSC
    zone_coverage = int(row[48])            # PLZC
    speed = int(row[53])                    # PSPD
    press_coverage = int(row[57])           # PLPE
    pass_blk_footwork = int(row[62])        # PPBF
    run_blk_footwork = int(row[63])         # PRBF
    block_shedding = int(row[66])           # PBSG
    toughness = int(row[67])                # PTGH
    catch = int(row[71])                    # PCTH
    catch_traffic = int(row[74])            # PLCI
    agility = int(row[75])                  # PAGI
    injury = int(row[79])                   # PINJ
    tackle = int(row[80])                   # PTAK
    pass_block = int(row[81])               # PPBK
    run_block = int(row[82])                # PRBK
    celebration_chance = int(row[88])       # PCEL
    release = int(row[96])                  # PLRL
    juke = int(row[100])                    # PLJM
    spin_move = int(row[102])               # PLSM
    throw_power = int(row[118])             # PTHP
    importance = int(row[119])              # PIMP
    jump = int(row[120])                    # PJMP
    carry = int(row[123])                   # PCAR
    morale = int(row[126])                  # PMOR
    kick_power = int(row[127])              # PKPR
    play_recognition = int(row[128])        # PLPR
    route_running = int(row[130])           # PLRR
    trucking = int(row[131])                # PLTR
    strength = int(row[132])                # PSTR
    overall = int(row[133])                 # POVR
    awareness = int(row[134])               # PAWR
    pass_blk_strength = int(row[139])       # PPBS
    run_blk_strength = int(row[140])        # PRBS
    finesse_move = int(row[143])            # PFMS
    hit_power = int(row[155])               # PLHT
    kick_return = int(row[158])             # PKRT
    elusiveness = int(row[163])             # PELU
    pursuit = int(row[164])                 # PLPU
    carrier_vision = int(row[165])          # PBCV

    # Unknown Values
    PBDA = int(row[17])                     # PBDA
    TLHA = int(row[21])                     # TLHA
    TRHA = int(row[23])                     # TRHA
    PLAC = int(row[39])                     # PLAC
    PRAC = int(row[40])                     # PRAC
    PHDC = int(row[42])                     # PHDC
    PLLC = int(row[43])                     # PLLC
    PTRC = int(row[46])                     # PTRC
    PUND = int(row[52])                     # PUND
    PRSE = int(row[59])                     # PRSE
    PCAF = int(row[61])                     # PCAF
    PSEF = int(row[64])                     # PSEF
    PCUF = int(row[65])                     # PCUF
    PTAL = int(row[85])                     # PTAL
    PUCL = int(row[87])                     # PUCL
    TLEL = int(row[90])                     # TLEL
    TREL = int(row[92])                     # TREL
    PTSL = int(row[98])                     # PTSL
    PSTM = int(row[103])                    # PSTM
    PLRN = int(row[110])                    # PLRN
    PBMO = int(row[116])                    # PBMO
    PTAR = int(row[124])                    # PTAR
    TLWR = int(row[136])                    # TLWR
    TRWR = int(row[138])                    # TRWR
    PLES = int(row[141])                    # PLES
    POPS = int(row[146])                    # POPS
    PCAX = int(row[166])                    # PCAX
    PKAX = int(row[167])                    # PKAX
    PLAX = int(row[168])                    # PLAX
    PRAX = int(row[169])                    # PRAX
    PSAX = int(row[170])                    # PSAX
    PTAX = int(row[171])                    # PTAX
    PIBX = int(row[172])                    # PIBX
    PPBX = int(row[173])                    # PPBX
    PRBX = int(row[174])                    # PRBX
    PACX = int(row[175])                    # PACX
    PBCX = int(row[176])                    # PBCX
    PLCX = int(row[177])                    # PLCX
    PSCX = int(row[178])                    # PSCX
    PHDX = int(row[179])                    # PHDX
    PSDX = int(row[180])                    # PSDX
    PPEX = int(row[181])                    # PPEX
    PPFX = int(row[182])                    # PPFX
    PRFX = int(row[183])                    # PRFX
    PAGX = int(row[184])                    # PAGX
    PTGX = int(row[185])                    # PTGX
    PLHX = int(row[186])                    # PLHX
    PLJX = int(row[187])                    # PLJX
    PTKX = int(row[188])                    # PTKX
    PELX = int(row[189])                    # PELX
    PLLX = int(row[190])                    # PLLX
    PRLX = int(row[191])                    # PRLX
    PFMX = int(row[192])                    # PFMX
    PIMX = int(row[193])                    # PIMX
    PJMX = int(row[194])                    # PJMX
    PLMX = int(row[195])                    # PLMX
    PPMX = int(row[196])                    # PPMX
    PINX = int(row[197])                    # PINX
    PMOX = int(row[198])                    # PMOX
    PKPX = int(row[199])                    # PKPX
    PTPX = int(row[200])                    # PTPX
    PKRX = int(row[201])                    # PKRX
    PLRX = int(row[202])                    # PLRX
    PPRX = int(row[203])                    # PPRX
    PRRX = int(row[204])                    # PRRX
    PTRX = int(row[205])                    # PTRX
    PBSX = int(row[206])                    # PBSX
    PLSX = int(row[207])                    # PLSX
    PPSX = int(row[208])                    # PPSX
    PRSX = int(row[209])                    # PRSX
    PCTX = int(row[210])                    # PCTX
    PLTX = int(row[211])                    # PLTX
    PSTX = int(row[212])                    # PSTX
    PPUX = int(row[213])                    # PPUX
    PAWX = int(row[214])                    # PAWX
    PLZX = int(row[215])                    # PLZX
    PJTY = int(row[216])                    # PJTY
    PSTY = int(row[217])                    # PSTY
    PRLc = int(row[218])                    # PRLc
    PTId = int(row[219])                    # PTId
    PLPm = int(row[220])                    # PLPm
    HDAp = int(row[221])                    # HDAp
    PRLx = int(row[222])                    # PRLx
    PSMx = int(row[223])                    # PSMx
    PRSx = int(row[224])                    # PRSx

    data.append([salary1, bonus1, salary2, bonus2, salary3, bonus3, salary4, bonus4, salary5, bonus5, salary6, bonus6,
                 salary7, bonus7, ankle_def, butt_def, calf_def, PBDA, foot_def, gut_def, left_hand, TLHA,
                 right_hand, TRHA, throw_acc, first_name, last_name, pad_def, current_salary, stiff_arm,
                 shoulder_def, total_salary, thigh_def, stamina, waist_def, impact_block, pro_bowl,
                 player_signing_bonus, kick_acc, PLAC, PRAC, acceleration, PHDC, PLLC, man_coverage, mouthpiece, PTRC,
                 spec_catch, zone_coverage, player_id, team_id, original_id, PUND, speed, age, player_face,
                 player_head, press_coverage, nasal_strip, PRSE, eye_paint, PCAF, pass_blk_footwork,
                 run_blk_footwork, PSEF, PCUF, block_shedding, toughness, skin_color, left_shoe, right_shoe,
                 catch, left_knee, right_knee, catch_traffic, agility, skin_tone, draft_pick_num, acquired_from,
                 injury, tackle, pass_block, run_block, neck_pad, face_mask, PTAL, hair_color, PUCL,
                 celebration_chance, left_elbow, TLEL, right_elbow, TREL, college, player_role_id, left_ankle,
                 release, sleeves, PTSL, years_left, juke, helmet, spin_move, PSTM, preferred_hand,
                 jersey_number, player_tendency, left_knee2, right_knee2, orig_contract_years, PLRN,
                 homestate, hometown, signing_bonus, contract_years, holdout, PBMO, round_drafted, throw_power,
                 importance, jump, years_pro, portrait_id, carry, PTAR, sleeves2, morale, kick_power,
                 play_recognition, right_ankle, route_running, trucking, strength, overall, awareness, left_wrist,
                 TLWR, right_wrist, TRWR, pass_blk_strength, run_blk_strength, PLES, visor,
                 finesse_move, position, celebration, POPS, player_total_salary, arm_size, butt_size,
                 calf_size, foot_size, height, gut_size, weight, hit_power, player_audio, pad_size, kick_return,
                 shoulder_size, thigh_size, waist_size, years_with_team, elusiveness, pursuit, carrier_vision,
                 PCAX, PKAX, PLAX, PRAX, PSAX, PTAX, PIBX, PPBX, PRBX, PACX, PBCX, PLCX, PSCX, PHDX, PSDX, PPEX, PPFX,
                 PRFX, PAGX, PTGX, PLHX, PLJX, PTKX, PELX, PLLX, PRLX, PFMX, PIMX, PJMX, PLMX, PPMX, PINX, PMOX, PKPX,
                 PTPX, PKRX, PLRX, PPRX, PRRX, PTRX, PBSX, PLSX, PPSX, PRSX, PCTX, PLTX, PSTX, PPUX, PAWX, PLZX, PJTY,
                 PSTY, PRLc, PTId, PLPm, HDAp, PRLx, PSMx, PRSx])

with open('Roster Randomized.csv', mode='w', newline='') as newfile:
    roster_writer = csv.writer(newfile, delimiter=',')
    for i in range(len(data)):
        roster_writer.writerow(data[i])

print("done")