# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 13:49:23 2020

@author: Tumtum
"""
import re  #fuck you, I DIDNT NEED YOU ANYWAY
with open('day4', 'r') as file:
    file = file.read().strip()
byr_min = 1920
byr_max = 2002
iyr_min = 2010
iyr_max = 2020
eyr_min = 2020
eyr_max = 2030
hin_min = 59
hin_max = 76
hcm_min = 150
hcm_max = 193
gecl = ['amb','blu','gry','brn','grn','hzl','oth']
cnt = 0
    

def validate_pp (byr , iyr , eyr , hgt , ecl , hcl , pid):
    if len(byr) == 4 and (byr_min <= int(byr) <= byr_max):
        # print('good byr:' , byr)
        if len(iyr) == 4 and (iyr_min <= int(iyr) <= iyr_max):
            # print('good iyr:' , iyr)
            if len(eyr) == 4 and (eyr_min <= int(eyr) <= eyr_max):
                # print('good eyr:' , eyr)
                if ecl in gecl:
                    # print('good ecl:' , ecl)
                    if len(pid) == 9 and pid.isdigit():
                        # print('good pid:' , pid)
                        if hexcolor(hcl):
                            # print('good hcl:' , hcl)
                            if hgt.endswith('cm'):
                                hgt = hgt.rstrip('cm')
                                if hcm_min <= int(hgt) <= hcm_max:
                                    # print('CM good height:' , hgt)
                                    return True
                            elif hgt.endswith('in'):
                                hgt = hgt.rstrip('in')
                                if hin_min <= int(hgt) <= hin_max:
                                    # print('IN good height:' , hgt)
                                    return True
                            else:
                                # print ('bad hgt', hgt)
                                return False
    #                     else:
    #                        print('bad hcl:' , hcl)
    #                 else:
    #                     print('bad pid:' , pid)
    #             else:
    #                 print('bad ecl:' , ecl)
    #         else:
    #             print('bad eyr:' , eyr)
    #     else:
    #         print('bad iyr:' , iyr)
    # else:
    #     print('bad byr:' , byr)
def hexcolor (inp):
    hex_letters = ['a', 'b', 'c' , 'd' , 'e' , 'f']
    count = 0
    if len(inp) == 7 and inp.startswith('#'):
        # print ('pass length and # check')
        inp = inp.lstrip('#')
        # print(inp)
        for x in inp:
            # print (x)
            if x.isdigit() or (x.lower() in hex_letters):
                # print('hex check good')
                count +=1
            else:
                # print('hex check fail')
                return False
        return True
    else:
        # print ('bad hex format')
        return False
    
pps = file.split('\n\n')
all_pps = []
for i in pps:
    fields = i.split()
    dtemp = dict(entry.split(':') for entry in fields)
    if all (key in dtemp for key in('ecl', 'pid', 'eyr', 'iyr', 'byr' , 'hcl' , 'hgt')):
        all_pps.append(dtemp)
        if validate_pp(dtemp['byr'],dtemp['iyr'],dtemp['eyr'],dtemp['hgt'],dtemp['ecl'],dtemp['hcl'],dtemp['pid']):
            # print(validate_pp(dtemp['byr'],dtemp['iyr'],dtemp['eyr'],dtemp['hgt'],dtemp['ecl'],dtemp['hcl'],dtemp['pid']))
            cnt += 1
print ('valid passports:' ,cnt)
        