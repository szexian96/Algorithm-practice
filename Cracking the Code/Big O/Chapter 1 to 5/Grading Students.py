n = int(input())
marks = []
for i in range(n):
    marks.append(int(input()))

for mark in marks:
	
	if mark >= 38:
		
		if mark % 5 == 3:
			mark += 2
		
		elif mark % 5 == 4:
			mark += 1

	print(mark)