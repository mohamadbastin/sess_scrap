import json
from courses import courses

f = open('14001/2903.txt', "r")

b = f.read()
f.close()
a = json.loads(b)

indent1 = courses["shabake"]
indent2 = courses["or"]

s1 = a[indent1]["students"]
s2 = a[indent2]["students"]

print(a[indent1]["title"])
print(a[indent2]["title"])

c = []
for i in s1:
    if i in s2:
        c.append(i)

print(c)
print(len(c))
