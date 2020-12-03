puzzle = []
with open('input', 'r') as f:
    for line in f.readlines():
        puzzle.append(line.strip())
# print(puzzle)

r, c = len(puzzle), len(puzzle[0])

# Part One
tree_count = 0

i, j = 0, 0
for i in range(r):
    j = (i*3)%c 
    # print(puzzle[i][j])
    if '#' == puzzle[i][j]:
        tree_count += 1
print(f'>> tree_count = {tree_count}\n')

#Part Two 
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
final_answer = 1

for right, down in slopes:
    tree_count = 0

    i, j, k = 0, 0, 0 
    while k * down < r: 
        i = k * down
        j = (k*right)%c
        # print(f'puzzle[i][j] = {puzzle[i][j]}')
        if '#' == puzzle[i][j]:
            tree_count += 1
        k += 1

    print(f'Right {right} down {down} > tree_count = {tree_count}')
    final_answer *= tree_count

print(f'>> final_answer = {final_answer}')

