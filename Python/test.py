limit = int(input())

flavors = int(input())
flavors_info = []
for count in range(flavors):
    flavor,num = input.split()
    add = [flavor,int(num)]
    flavors_info.append(flavor)

print(flavors_info)