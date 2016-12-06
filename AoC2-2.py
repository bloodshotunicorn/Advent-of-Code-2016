file = open(r'C:\Users\jsaur\Desktop\Advent of Code Input\2.txt')
directions = file.read().split('\n')
index = [2,0]
keypad = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
code = ''
for line in directions:
    for c in line:
        if c == 'U' and index[0] > 0 and not keypad[index[0] - 1][index[1]] == 0:
            index[0] -= 1
        elif c == 'D' and index[0] < 4 and not keypad[index[0] + 1][index[1]] == 0:
            index[0] += 1
        elif c == 'L' and index[1] > 0 and not keypad[index[0]][index[1] - 1] == 0:
            index[1] -= 1
        elif c == 'R' and index[1] < 4 and not keypad[index[0]][index[1] + 1] == 0:
            index[1] += 1
    code += str(keypad[index[0]][index[1]])
print('The code is ' + code)