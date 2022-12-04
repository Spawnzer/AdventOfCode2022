class A:
    def __init__(self, str):
        a, b= str.split("-")
        self.min, self.max = int(a), int(b)

def contains(c, d):
    if c.min >= d.min and c.max <= d.max:
        return 1
    if d.min >= c.min and d.max <= c.max:
        return 1
    return 0

def overlap(c, d):
    if len(set(range(c.min, c.max + 1)).intersection(set(range(d.min, d.max + 1)))) > 0:
        return 1
    return 0
    

total = 0
total1 = 0

with open("data", "r") as fd:
    lines = fd.readlines()

for line in lines:
    a, b = line.split(',')
    c = A(a)
    d = A(b)
    total = total + contains(c, d)
    total1 = total1 + overlap(c, d)

print(f"{total}, {total1}")
