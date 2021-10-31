import json

f = open('14001/2903.txt', "r")

b = f.read()
f.close()
a = json.loads(b)

c = []
for i in a.values():
    # i = a.values()
    # print(i)
    print(i["title"])
    print(i['time_room'])
    print(i['group'])
    print(i['teacher'])
    print(i['gender'])
    print(i['vahed'])
    print(i['unit'])
    print(i['final_date'])
    print(i['students'])
    print("*****************************")
    # print(i[0])
#     c.append(i['title'])
# d = ''
# for i in c:
#     d += i
#     d += '\n'
# f = open('13991/compcourses.txt', 'w', encoding="utf-8")
# f.write(d)
# f.close()
