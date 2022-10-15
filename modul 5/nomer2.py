#Modul 5 Nicky Julyatrika Sari L200200101
#Nomer 2

def insertionSort(nim):
    a = len(nim)
    for i in range(1, a):
        nilai = nim[i]
        posisi = i
        while posisi > 0 and nilai < nim[posisi - 1]:
            nim[posisi] = nim[posisi - 1]
            posisi = posisi - 1
            nim[posisi] = nilai

a = [11, 1, 50, 10, 22, 48, 34, 21]
b = [8, 43, 19, 25, 17, 13, 67]
 
def urutanAB(a, b):
    c = a + b
    insertionSort(c)
    return c
print(urutanAB(a,b))
