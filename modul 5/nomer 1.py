#Modul 5 Nicky Julyatrika Sari L200200101
#Nomer 1

class MhsTIF(object):
    def __init__(self,nama,nim,kota,saku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.saku = saku
        
def insertionSort(nim):
    a = len(nim)
    for i in range(1, a):
        nilai = nim[i]
        posisi = i
        while posisi > 0 and nilai < nim[posisi - 1]:
            nim[posisi] = nim[posisi - 1]
            posisi = posisi - 1
            nim[posisi] = nilai
    
c0 = MhsTIF('Ika',10,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',19,'Sragen', 230000)
c2 = MhsTIF('Ahmad',12,'Surakarta', 250000)
c3 = MhsTIF('Chandra',17,'Surakarta', 235000)
c4 = MhsTIF('Eka',13,'Boyolali', 240000)
c5 = MhsTIF('Fandi',11,'Salatiga', 250000)
c6 = MhsTIF('Deni',16,'Klaten', 245000)
c7 = MhsTIF('Galuh',18,'Wonogiri', 245000)
c8 = MhsTIF('Janto',20,'Klaten', 245000)
c9 = MhsTIF('Hasan',14,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',15,'Purwodadi', 265000)

#Lalu kita membuat daftar mahasiswa dalam bentuk list seperti ini:

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def urutanNIM(nim):
    new = []
    for x in nim:
        new.append(x.nim)
    insertionSort(new)
    return new

print(urutanNIM(Daftar))
