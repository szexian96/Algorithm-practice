#adds adjacent elements between 0 and n

def parSumSequence(n):
    sum = 0
    j = 0
    count = int(n)
    for i in range(count):
        sum += pairSum(j, j + 1)
        j += 1
    return sum

def pairSum(a, b):
	return a + b

print(parSumSequence(5))
print(parSumSequence(4))
print(parSumSequence(3))
print(parSumSequence(2))
print(parSumSequence(1))