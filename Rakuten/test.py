a = input()
my_input = a.split()

lst = []
for one in my_input:
    lst.append(one)
    if one == "-":
        after = int(lst.index(one))-1
        before = int(lst.index(one))-2
        result = int(lst[after]) - int(lst[before])
        for loop in range (3):
            lst.pop()
        lst.append(result)
    elif one == "+":
        after = int(lst.index(one))-1
        before = int(lst.index(one))-2
        result = int(lst[after]) + int(lst[before])
        for loop in range (3):
            lst.pop()
        lst.append(result)
    elif one == "DUP":
        before = int(lst.index(one))-1
        lst.pop()
        lst.append(lst[before])
    elif one == "POP":
        for loop in range (2):
            lst.pop()

print(lst[-1])