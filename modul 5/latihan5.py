def insertionSort(nim):
    a = len(nim)
    for i in range(1, a):
        nilai = nim[i]
        posisi = i
        while posisi > 0 and nilai < nim[posisi - 1]:
            nim[posisi] = nim[posisi - 1]
            posisi = posisi - 1
            nim[posisi] = nilai
