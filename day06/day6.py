count_sum_1 = 0 
count_sum_2 = 0

with open('input', 'r') as f:
    groups = f.read().split('\n\n')

# Part One
for group in groups:
    yes_set = set(group.strip())
    if '\n' in yes_set:
        yes_set.remove('\n') 
    yes_count = len(yes_set)
    # print(f'yes_count = {yes_count}, yes_set = {yes_set}')
    count_sum_1 += yes_count

print(f'count_sum_1 = {count_sum_1}')

# Part Two 
for group in groups: 
    group = group.strip().split('\n')
    ques_set = set(group[0])
    if len(group) == 1: 
        ques_count = len(ques_set)
    else:
        for g in group:
            ques_set = ques_set.intersection(set(g))
        ques_count = len(ques_set)
    # print(f'ques_count = {ques_count}, ques_set = {ques_set}')
    count_sum_2 += ques_count

print(f'count_sum_2 = {count_sum_2}')
