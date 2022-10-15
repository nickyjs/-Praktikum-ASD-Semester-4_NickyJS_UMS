#Nomer 1 Nicky Julyatrika Sari l200200101
#Modul 1
def CetakSiku(x):  
    for i in range(0, x, 1):
        for j in range(0, i + 1):
            print(' * ' , end='')
        print('')
















































#Nomer 2 Nicky l200200101
def Gambarlahpersegiempat(x,y):
    for i in range(x):
        if i == 0  or i == x-1:
            print ('@'*y)
        else:
           print ('@' + ' ' *(y-2)+'@')

#Nomer 3a Nicky l200200101

def JumlahHurufVokal(hrf):
    vokal = 'aiueoAIUEO'
    a = 0
    hasil = 0
    for i in hrf:
        if i in vokal:
            a += len(i)
        else:
            a +=0

    hasil = len(hrf), a
    return hasil



#Nomer 3b Nicky l200200101
def JumlahHurufKonsonan(hrf):
    konsonan = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    b = 0
    hasil = 0
    for i in hrf:
        if i in konsonan:
            b += len(i)
        else:
            b += 0

    hasil = len(hrf), b
    return hasil


#Nomer 4 Nicky l200200101
def rerata(b):
    jumlah =0
    for i in range (len(b)):
        jumlah += b[i]
    jumlah = jumlah/len(b)
    return jumlah

#Nomer 5 Nicky l200200101
from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrkecil:
        return False
    else:
        for i in range(2, int(sq(n))+1):
            if n%i == 0:
                return False
            return true
#Nomer 6 Nicky l200200101
    









