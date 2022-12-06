with open("starting", "r") as fd:
    lines = fd.readlines()

b = [[0 for x in range(9)] for y in range(9)]

i = 1
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        a = lines[i][j]
        if a >= 'A' and a <= 'Z':
            b[j//4][i-1] = a
        j = j + 1
    i = i + 1

for line in b:
    line = [i for i in line if i != 0]
    line.reverse()


#res.append(line[len(line) - 1])
print(''.join(res))