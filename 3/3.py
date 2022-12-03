def get_value(key):
    if key.islower():
        return ord(key) - ord('a') + 1
    else:
        return ord(key) - ord('A') + 27


total = 0
total1 = 0
i = 0
key = 'a'
with open("data", "r") as fd:
    lines = fd.readlines()

for line in lines:
    m = len(line) // 2
    a = line[:m]
    b = line[m:]
    key = list(set(a).intersection(b))[0]
    total = total + get_value(key)
    if i % 3 == 0:
        set1 = set(set(lines[i].strip()).intersection(lines[i+1].strip()))
        key = list(set1.intersection(lines[i + 2].strip()))[0]
        total1 = total1 + get_value(key)
    i = i + 1

print(total, total1)
