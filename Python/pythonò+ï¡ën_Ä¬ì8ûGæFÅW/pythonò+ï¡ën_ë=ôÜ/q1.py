#素数(1とその数自身でしか割り切れない数)を表示するプログラム

limit = int(input('上限数:'))#いくつまで表示するか決める

#素数を特定してはじき出す関数
def genPrime(maxnum):
    for num in range(1,maxnum+1):
        c = []
        for d in range(1,num+1):
            if num % d == 0:
                c.append(d)#dはnumでも可
        if len(c) == 2:
            yield num#numはdでも可

#イテレータオブジェクトを取得
it = genPrime(limit)

#for構文で繰り返し表示
for i in it:
    print(i, end=",")
