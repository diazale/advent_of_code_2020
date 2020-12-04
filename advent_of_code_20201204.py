"""
Passport data contains the following fields

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

Passports are separated by blank lines

In order to be valid, passports must have all fields (cid is optional)
"""

f = open("input_20201204.txt", "r")

passports = list()

# Strings are apparently immutable, so transform them to lists
for line in f.readlines():
    passports.append(line.strip("\n"))

f.close()

# Store our data as a list of dicts
passport_dicts = list()
cur_dict = dict()

for p in passports:
    if p!="":
        # If the line is not blank, add information to the current passport dictionary
        for item in p.split():
            key,val = item.split(":")
            cur_dict[key] = val
    else:
        # If it's a blank line, we're on a new passport
        passport_dicts.append(cur_dict)
        cur_dict = dict()

# Edge case: Last passport
passport_dicts.append(cur_dict)

# Part 1: Check if all required keys are present
required_keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

valid_passports = 0
for p in passport_dicts:
    if set(required_keys).issubset(p.keys()):
        valid_passports+=1

print("Valid passports:", valid_passports)

# Part 2: The other fields need to have valid data

# Define valid values for certain variables
hex_vals = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
ecl_vals = ["amb","blu","brn","gry","grn","hzl","oth"]
dig_vals = ["0","1","2","3","4","5","6","7","8","9"]

def valid_input(var_, val_):
    if var_=="byr":
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if 1920 <= int(val_) <= 2002:
            return True
    elif var_=="iyr":
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if 2010 <= int(val_) <= 2020:
            return True
    elif var_=="eyr":
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if 2020 <= int(val_) <= 2030:
            return True
    elif var_=="hgt":
        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        if "cm" in val_:
            if 150 <= int(val_.split("cm")[0]) <= 193:
                return True
        elif "in" in val_:
            if 59 <= int(val_.split("in")[0]) <= 76:
                return True
    elif var_=="hcl":
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if len(val_)==7:
            if val_[0]=="#" and set(val_[1:]).issubset(hex_vals):
                return True
    elif var_=="ecl":
        # ecl (Eye Color) - exactly one of: "amb","blu","brn","gry","grn","hzl","oth"
        if val_ in ecl_vals:
            return True
    elif var_=="pid":
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if len(val_)==9 and set(val_).issubset(dig_vals):
            return True
    elif var_=="cid":
        return True

    return False

valid_passports = 0

for p in passport_dicts:
    if set(required_keys).issubset(p.keys()):
        # Check if it has all the keys
        # Assume it is valid so far
        valid = True
        for key, value in p.items():
            # Then check if the keys are all valid
            if not valid_input(key, value):
                valid = False

        if valid:
            print(p)
            valid_passports+=1

print(valid_passports)