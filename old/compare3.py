import json
from courses import courses

f = open('14001/2903.txt', "r")

b = f.read()
f.close()
a = json.loads(b)

indent1 = courses["narm"]
indent2 = courses["mohasebat"]
indent3 = courses["algo"]

s1 = a[indent1]["students"]
s2 = a[indent2]["students"]
s3 = a[indent3]["students"]

print(a[indent1]["title"])
print(a[indent2]["title"])
print(a[indent3]["title"])

c = []
for i in s1:
    if i in s2 and i in s3:
        c.append(i)

print(c)
print(len(c))
