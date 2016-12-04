#2016 Advent of Code Day 1 Part 1
file = open(r'C:\Users\jsaur\Desktop\Advent of Code Input\1-1.txt')
directions = file.read().split(', ')
#Cardinal directions: 0N, 1E, 2S, 3W
card = 0
#Direction in which to move based on cardinal direction
mult = [1, 1, -1, -1]
x_loc = 0
y_loc = 0
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
    #If facing North or South
    if card%2 == 0:
        #mult[card] defines direction, int(d[1:]) defines magnitude of movement
        y_loc += (mult[card] * int(d[1:]))
    #If facing East or West
    elif card%2 == 1:
        x_loc += (mult[card] * int(d[1:]))
print(str(x_loc) + ' ' + str(y_loc))
print('Distance = ' + str(abs(x_loc) + abs(y_loc)) + ' blocks')