# sample of O(N)

min = 50
max = 100

numbers =[ 10, 20, 50, 200, 100]

for number in numbers:
    if number < min:
        min = number
    if number > max:
        max = number

print(f"minimum:{min},maximum:{max}")