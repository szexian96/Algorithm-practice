s,t = map(int, input().split())
a,b = map(int, input().split())
m,n = map(int, input().split())
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

count_a = 0
count_o = 0

for d in apples:
	if a+d >= s and a+d<=t:
		count_a+=1

for d in oranges:
	if b+d >= s and b+d<=t:
		count_o+=1

print(count_a)
print(count_o)