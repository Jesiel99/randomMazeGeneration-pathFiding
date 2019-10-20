wall = 9

mood = [
[wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall],
[wall, wall, wall, 0, 0, 0, 0, 0, wall, wall, wall, 0, wall],
[wall, wall, wall, 0, wall, wall, wall, 0, wall, wall, wall, 0, wall],
[wall, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, wall],
[wall, wall, 0, wall, wall, wall, 0, wall, wall, wall, wall, 0, wall],
[wall, 0, 0, 0, wall, wall, 0, wall, wall, wall, wall, 0, wall],
[wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall],
    ]

screen = [
['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@'],
['@', '@', '@', ' ', ' ', ' ', ' ', ' ', '@', '@', '@', ' ', '@'],
['@', '@', '@', ' ', '@', '@', '@', ' ', '@', '@', '@', ' ', '@'],
['@', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '@'],
['@', '@', '@', ' ', '@', '@', ' ', '@', '@', '@', '@', ' ', '@'],
['@', ' ', ' ', ' ', '@', '@', ' ', '@', '@', '@', '@', ' ', '@'],
['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@']]

len_l = 7
len_c = 13

for l in range(0, len_l):  # prints de matrizes
    for c in range(0, len_c):
        print(screen[l][c], end='')
    print()
for l in range(0, len_l):
    for c in range(0, len_c):
        print(mood[l][c], end='|')
    print()
