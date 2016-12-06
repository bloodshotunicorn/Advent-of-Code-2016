file = open(r'C:\Users\jsaur\Desktop\Advent of Code Input\3.txt')
list = file.read().split('\n')
counter = 0
for side in list:
    side = side.split()
    side = [int(i) for i in side]
    side = sorted(side)
    if side[0] + side[1] > side[2]:
        counter += 1
print(counter)