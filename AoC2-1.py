file = open(r'C:\Users\jsaur\Desktop\Advent of Code Input\2.txt')
directions = file.read().split('\n')
index = [1,1]
keypad = [[1,2,3],[4,5,6],[7,8,9]]
code = ''
for line in directions:
    for c in line:
        if c == 'U' and index[0] > 0:
            index[0] -= 1
        elif c == 'D' and index[0] < 2:
            index[0] += 1
        elif c == 'L' and index[1] > 0:
            index[1] -= 1
        elif c == 'R' and index[1] < 2:
            index[1] += 1
    code += str(keypad[index[0]][index[1]])
print('The code is ' + code)