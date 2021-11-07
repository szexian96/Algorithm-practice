#ポアソン分布をするプログラム

import numpy as np
import math
import matplotlib.pyplot as plt

def poisson(lambda_, k):
    k = int(k)
    result = (lambda_**k) * (math.exp(-lambda_))  / math.factorial(k)
    return result

input_lam1 = int(input('λ1:'))
input_lam2 = int(input('λ2:'))
input_lam3 = int(input('λ3:'))
input_ran = int(input('k:'))#※範囲の問題点あり
y1= [poisson(input_lam1,i) for i in range(1, input_ran)]
y2= [poisson(input_lam2,i) for i in range(1, input_ran)]
y3= [poisson(input_lam3,i) for i in range(1, input_ran)]

plt.bar(range(1, input_ran), y1, align="center", width=0.4, color="red"
                ,alpha=0.5, label="Poisson λ= %d" % 10)

plt.bar(range(1, input_ran), y2, align="center", width=0.4, color="green"
                ,alpha=0.5, label="Poisson λ= %d" % 20)

plt.bar(range(1, input_ran), y3, align="center", width=0.4, color="blue"
                ,alpha=0.5, label="Poisson λ= %d" % 30)

plt.legend()
plt.savefig("q13.py_Poisson.png")
print('グラフを保存した。')
plt.show()
