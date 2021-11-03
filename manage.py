import sys
import json
from courses import courses

f = open('14001/2903.txt', "r")

scrap = f.read()
f.close()
data = json.loads(scrap)

"""
use cmp to cmpare n courses
and write the name of n courses

use stu to get list of a student's courses

"""

res = []
if len(sys.argv) > 0:
	if sys.argv[1].lower() == 'cmp':
		c = data[courses[sys.argv[2]]]['students']
		for i in range(len(c)):
			flag = 1
			for x in range(3,len(sys.argv)):
				if c[i] not in data[courses[sys.argv[x]]]['students']:
					flag = 0
					break
			if flag: 
				res.append(c[i])
		print(len(res))
		print(res)

	if sys.argv[1].lower() == 'stu':
		name = [sys.argv[2], sys.argv[3]]
		for i in data.keys():
			if name in data[i]["students"]:
				res.append(data[i]["title"])

		print(len(res))
		print(res)

	if sys.argv[1].lower() == 'all':
		for _ in data.values():
			print(_["title"])
			print(_['time_room'])
			print(_['group'])
			print(_['teacher'])
			print(_['gender'])
			print(_['vahed'])
			print(_['unit'])
			print(_['final_date'])
			print(_['students'])
			print("*****************************")		

else:
	print("nothing to do :)")