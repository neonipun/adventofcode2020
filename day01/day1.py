input = set()
with open('input', 'r') as f: 
    for n in f.readlines():
        input.add(int(n))

for i in input:
    if abs(2020 - i) in input:
        print(f'Numbers: {i}, {abs(2020 - i)}')
        print(f'Part 1 Answer: {abs(2020 - i) * i}\n')
        break

from itertools import combinations
for x, y, z in combinations(input, 3):
    if x + y + z == 2020: 
        print(f'Numbers: {x}. {y}, {z}')
        print(f'Part 2 Answer: {x * y * z}')
        break
