total = 1
max = 0
result = []
cur = []

with open("data", "r") as fd:
    lines = fd.readlines()

for line in lines:
    if line == "\n":
        result.append(cur)
        cur = []
    else:
        cur.append(int(line.strip()))

top3 = [0,0,0]

for i in result:
    total = sum(i)
    if total > min(top3):
        top3.remove(min(top3))
        top3.append(total)

print(sum(top3), top3)