def get_value(key):
    if key.islower():
        return ord(key) - ord('a') + 1
    else:
        return ord(key) - ord('A') + 27


total = 0
key = 'a'
with open("data", "r") as fd:
    lines = fd.readlines()

for line in lines:
    m = len(line) // 2
    a = line[:m]
    b = line[m:]
    key = list(set(a).intersection(b))[0]
    total = total + get_value(key)

print(total)
