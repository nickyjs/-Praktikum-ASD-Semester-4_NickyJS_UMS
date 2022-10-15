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
                return "Item berada di simpul ke - " + str(awal)
            else:
                awal += 1
                x = x.next
        return "Item tidak ditemukan"

c = Node(10)
c.next = Node(15)
c.next.next = Node(20)
