#Modul 5 Nicky Julyatrika Sari L200200101
#Nomer 3

from time import time as detak
from random import shuffle as kocok
 

#Latihan 1
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

#Latihan 2
def cariPosisiTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil = i
    return posisiTerkecil

#Latihan 3
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

#Latihan 4
def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        indexKecil = cariPosisiTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

#Latihan 5
def insertionSort(nim):
    a = len(nim)
    for i in range(1, a):
        nilai = nim[i]
        posisi = i
        while posisi > 0 and nilai < nim[posisi - 1]:
            nim[posisi] = nim[posisi - 1]
            posisi = posisi - 1
            nim[posisi] = nilai

 
k = list(range(1,6001))
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
aw=detak();bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw=detak();selectionSort(u_bub);ak=detak();print('selection: %g detik' %(ak-aw));
aw=detak();insertionSort(u_bub);ak=detak();print('insertion: %g detik' %(ak-aw));
