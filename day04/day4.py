valid_count_1 = 0
valid_count_2 = 0 
with open('input', 'r') as f: 
    passports = f.read().split('\n\n')

for passport in passports: 
    passport = passport.split()
    if len(passport) == 8:
        valid_count_1 += 1
    elif len(passport) == 7:
        if 'cid' not in ''.join(passport):
            valid_count_1 += 1
    # print(list(map(str.split(':'), passport)))

print(valid_count_1)

# # Part Two 
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
def valid_data(passport):
    for field in passport:
        k, v = field.split(':')
        if k == 'byr': 
            if not (len(v) == 4 and int(v) >= 1920 and int(v) <= 2002):
                return False
        elif k == 'iyr':
            if not (len(v) == 4 and int(v) >= 2010 and int(v) <= 2020):
                return False
        elif k == 'eyr':
            if not (len(v) == 4 and int(v) >= 2020 and int(v) <= 2030):
                return False
        elif k == 'hgt':
            if not ((v[-2:] == 'cm' and int(v[:-2]) >= 150 and int(v[:-2]) <= 193) or (v[-2:] == 'in' and int(v[:-2]) >= 59 and int(v[:-2]) <= 76)):
                return False
        elif k == 'hcl':
            if not (v[0] == '#' and v[1:].isalnum() and len(v[1:]) == 6):
                return  False
        elif k == 'ecl':
            if v not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                return False
        elif k == 'pid':
            if len(v) != 9:
                return False
    return True

for passport in passports: 
    passport = passport.split()
    if len(passport) == 8 and valid_data(passport):
        valid_count_2 += 1
    elif len(passport) == 7 and valid_data(passport):
        if 'cid' not in ''.join(passport):
            valid_count_2 += 1

print(valid_count_2)