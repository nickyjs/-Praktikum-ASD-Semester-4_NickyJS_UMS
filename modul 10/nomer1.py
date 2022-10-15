#Nicky Julyatrika sari l200200101
#modul 10
#nomer 1a


import time
from timeit import timeit
def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
    return hasilnya

for i in range(5):
    siap = 'from __main__ import jumlahkan_cara_1'
    h = jumlahkan_cara_1(1000000)
    t = timeit('jumlahkan_cara_1(1000000)', setup = siap, number=1)
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, t))




