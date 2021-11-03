import json
from courses import courses

f = open('14001/2903.txt', "r")

b = f.read()
f.close()
a = json.loads(b)

name = ['عليرضا', 'بحراني']
c = []
for i in a.keys():
    if name in a[i]["students"]:
        c.append(i)

for i in c:
    print(a[i]["title"])
