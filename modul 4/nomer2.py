#Nomor 7
data = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]

def binSe2(kumpulan,target):
    low = 0
    high = len(kumpulan)-1
    ketemu = False
    x = []

    while low <= high and not ketemu :
        mid = (high + low)//2
        if kumpulan[mid] == target:
            ketemu = True
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if not ketemu:
        print('Data tidak ditemukan')
    for i in range(len(kumpulan)):
        if kumpulan[i] == target:
            x.append(mid)
            mid+=1
    return x
