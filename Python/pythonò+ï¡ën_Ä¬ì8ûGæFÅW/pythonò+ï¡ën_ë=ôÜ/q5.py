#3次正方行列とその余因子行列(余因子を並べて出来た行列の転置を取った行列)の
#積の非対角成分(1行2列目、1行3列目、2行1列目、2行3列目、3行1列目、3行2列目)が
#必ず0になることを確かめるためのプログラム

import numpy as np

#値を代入
a11 = int(input('1行1列目:'))
a12 = int(input('1行2列目:'))
a13 = int(input('1行3列目:'))
a21 = int(input('2行1列目:'))
a22 = int(input('2行2列目:'))
a23 = int(input('2行3列目:'))
a31 = int(input('3行1列目:'))
a32 = int(input('3行2列目:'))
a33 = int(input('3行3列目:'))

A = np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])#行列にする
print('\n')
print('A=')
print(A,'\n')

#余因子の計算
a_11 = a22 * a33 - a23 * a32
a_12 = a23 * a31 - a21 * a33
a_13 = a21 * a32 - a22 * a31
a_21 = a13 * a32 - a12 * a33
a_22 = a11 * a33 - a13 * a31
a_23 = a12 * a31 - a11 * a32
a_31 = a12 * a23 - a13 * a22
a_32 = a13 * a21 - a11 * a23
a_33 = a11 * a22 - a12 * a21

#余因子を並べて行列にする
A_ = np.array([[a_11,a_12,a_13],[a_21,a_22,a_23],[a_31,a_32,a_33]])
print('A~=')
print(A_,'\n')

AT = A_.T#行列の転置をとる(Tはtranspose()でも可)
print('(A~)^T=')
print(AT,'\n')

print('A*((A~)^T)=')
print(np.dot(A,AT))#行列同士の積を出力
