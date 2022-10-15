#Nicky Julyatrika sari l200200101
#modul 10
#nomer 3c

import timeit
import matplotlib.pyplot as plt
def kalangBersusuh(n):
    test = 0
    for i in range(n):
        test = test + 1
    for j in range(n):
        test = test - 1
    
def ujiKalangBersusuh(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = 'from __main__ import kalangBersusuh'
    for i in jangkauan:
        print('i = ', i)
        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap, number = 1)
        ls.append(t)
    return ls
n = 1000
LS = ujiKalangBersusuh(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()

