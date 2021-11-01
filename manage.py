import sys
import json
from courses import courses

f = open('14001/2903.txt', "r")

b = f.read()
f.close()
a = json.loads(b)

"""
use cmp to cmpare n courses
and write the name of n courses

"""

res = []
if len(sys.argv) > 0:
	if sys.argv[1].lower() == 'cmp':
		c = a[courses[sys.argv[2]]]['students']
		for i in range(len(c)):
			flag = 1
			for x in range(3,len(sys.argv)):
				if c[i] not in a[courses[sys.argv[x]]]['students']:
					flag = 0
					break
			if flag:
				res.append(c[i])
	if sys.argv[1].lower() == 'get_student':
		print("will be implemented soon")

	print(len(res))
	print(res)

else:
	print("nothing to do :)")