#2016 Advent of Code Day 1 Part 2
file = open(r'C:\Users\jsaur\Desktop\Advent of Code Input\1-1.txt')
directions = file.read().split(', ')
#Cardinal directions: 0N, 1E, 2S, 3W
card = 0
mult = [1, 1, -1, -1]
x_loc = 0
y_loc = 0
loc_list = [[0,0]]
for d in directions:
    if d[0] == 'R':
        if card == 3:
            card = 0
        else:
            card += 1
    elif d[0] == 'L':
        if card == 0:
            card = 3
        else:
            card -= 1
    distance = int(d[1:])
    if card%2 == 0:
        for d in range(0,distance):
            y_loc += mult[card]
            loc = [x_loc,y_loc]
            if loc in loc_list:
                print(loc)
                break
            else:
                loc_list.append(loc)
    elif card%2 == 1:
        for d in range(0,distance):
            x_loc += mult[card]
            loc = [x_loc,y_loc]
            if loc in loc_list:
                print(loc)
                break
            else:
                loc_list.append(loc)