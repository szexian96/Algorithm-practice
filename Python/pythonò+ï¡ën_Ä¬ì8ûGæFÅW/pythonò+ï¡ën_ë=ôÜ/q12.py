#csv >> json

import csv
import json

with open('q12.py_kenko.csv' , encoding = 'utf8') as c:
	with open('q12.py_kenko.json' , mode = 'w' , encoding = 'utf8') as j:
		reader = csv.DictReader(c)
		l = [row for row in reader]
		#print(l)
		json.dump(l , j, indent = 4 , ensure_ascii = False)
