#Nicky Julyatrika Sari L200200101
#Modul 4
class MhsTIF(object):
    def __init__(self,nama,umur,kota,saku):
        self.nama = nama
        self.umur = umur
        self.kota = kota
        self.saku = saku

    
c0 = MhsTIF('Ika',10,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',51,'Sragen', 230000)
c2 = MhsTIF('Ahmad',2,'Surakarta', 250000)
c3 = MhsTIF('Chandra',18,'Surakarta', 235000)
c4 = MhsTIF('Eka',4,'Boyolali', 240000)
c5 = MhsTIF('Fandi',31,'Salatiga', 250000)
c6 = MhsTIF('Deni',13,'Klaten', 245000)
c7 = MhsTIF('Galuh',5,'Wonogiri', 245000)
c8 = MhsTIF('Janto',23,'Klaten', 245000)
c9 = MhsTIF('Hasan',64,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',29,'Purwodadi', 265000)

#Lalu kita membuat daftar mahasiswa dalam bentuk list seperti ini:

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#Nomer 1
def cariPosisi(target):
    x =[]
    for i in range(len(Daftar)):
        if target == Daftar[i].kota:
            x.append(i)
    if len(x) > 0:
        print(x)
        return True
    else:
        print(x)
        return False

#Nomor 2
def uangSakuTerkecil():
    terkecil = Daftar[0].saku
    for i in range(len(Daftar)):
        if terkecil > Daftar[i].saku:
            terkecil = Daftar[i].saku
    return terkecil

#Nomor 3
def sakuTerkecil2(a):
    terkecil = Daftar[0].saku
    list = []
    for i in range(len(a)):
        if a[i].saku < terkecil:
            terkecil = a[i].saku
    for i in range(len(a)):
        if a[i].saku == terkecil:
            list.append(a[i].nama)
    return list

#Nomor 4
def sakuKurang():
    list = []
    for i in range(len(Daftar)):
        if Daftar[i].saku < 250000:
            list.append(Daftar[i].nama)
    for x in list:
        print(x, end=' ')

#Nomor 5
class Node():
    def __init__(self, data, link=None):
        self.data = data
        self.next = link

    def cariItem(self, cari):
        x = self
        awal = 1
        while x != None:
            if x.data == cari:
                return "Nomer 5 = Item berada di simpul ke - " + str(awal)
            else:
                awal += 1
                x = x.next
        return "Nomer 5 = Item tidak ditemukan"

c = Node(10)
c.next = Node(15)
c.next.next = Node(20)

#Nomor 6
kumpulan=[2,4,6,8,10,12,14,16,18,20]
def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan)-1

    while low <=high:
        mid =(high + low)//2
        if kumpulan[mid]==target:
            return 'Nomer 6 = ditemukan pada indeks ke-'+str(mid)
        elif target < kumpulan[mid]:
            high = mid -1
        else:
            low = mid+1
        return False


