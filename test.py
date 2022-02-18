from copy import deepcopy

def split(word):
	return [char for char in word]

s = input()
H, W = list(map(int,s.split()))
newlst = []
i=0

for height in range (0,H):
    data = input()
    clean = split(data)
    newlst.append(clean)
    newlst1 = deepcopy(newlst)


for height in range (0,H):
    for width in range (0,W):
        if any('#' in s for s in newlst[height]):
            newlst[height][width] = "#"

for height in range (0,H):
    for width in range (0,W):
        if any('#' in s for s in newlst1[width]):
            if height < H-1:
                newlst1[height+1][width] = "#"

        if newlst[height][width] == "#" and newlst1[height][width] == ".":
            newlst1[height][width] = "#"


print(newlst1)
print(sum(x.count('#') for x in newlst1))








# 入力例1
# 4 4
# #.#.
# ....
# ..#.
# ....
# 出力例1
# 12
# 入力例2
# 5 8
# .#.#....
# ........
# ........
# ........
# .....#..
# 出力例2
# 25


    