from collections import Counter

valid_count_1 = 0 
valid_count_2 = 0

# Password Policy checker
with open('input', 'r') as f: 
    for line in f.readlines():
        policy, password = line.strip().split(':')
        password = password.strip()
        password_c = Counter(password)

        # Part One
        # Lower Limit, Upper Limit of Policy and Policy Letter Count
        ll, ul = list(map(int, policy.strip().split()[0].split('-')))
        pl = policy.strip().split()[1]
        plc = password_c[pl]

        if plc >= ll and plc <= ul:
            valid_count_1 += 1  
        
        # Part Two
        # Position 1 and 2 
        p1, p2 = ll - 1, ul - 1

        # # Logic 1
        # if password[p1] == pl:
        #     if password[p2] != pl:
        #         valid_count_2 += 1
        # else:
        #     if password[p2] == pl:
        #         valid_count_2 += 1 
        
        # Logic 2 
        if password[p1] != password[p2]:
            if password[p1] == pl or password[p2] == pl:
                valid_count_2 += 1
    
print(f'>> valid_count_1 = {valid_count_1}')
print(f'>> valid_count_2 = {valid_count_2}')
