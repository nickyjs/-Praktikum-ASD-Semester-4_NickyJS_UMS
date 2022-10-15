#Nicky Julyatrika sari l200200101
#modul 10
#nomer 1b

import random
from timeit import timeit
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos -1
        A[pos] = nilai
print("------average case scenario------") 

for i in range(5):
    siap = 'from __main__ import insertionSort, L'
    L = list(range(3000))
    random.shuffle(L)
    t = timeit('insertionSort(L)', setup = siap, number=1)
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), t))
 
print("------worst case scenario------") 
for i in range(5):
    siap = 'from __main__ import insertionSort, L'
    L = list(range(3000))
    L = L[::-1]
    t = timeit('insertionSort(L)', setup = siap, number=1)
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), t))
 
print("------best case scenario------") 
for i in range(5):
    siap = 'from __main__ import insertionSort, L'
    L = list(range(3000))
    t = timeit('insertionSort(L)', setup = siap, number=1)
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L), t))

