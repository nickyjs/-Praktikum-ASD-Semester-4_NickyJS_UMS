#Nicky Julyatrika Sari L200200101 Modul 2
class Manusia(object):
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan",s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2
    
class Mahasiswa(Manusia):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal =kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM '+ str(self.NIM)\
            + '. Tinggal di '+ self.kotaTinggal \
            + '. Uang saku Rp '+ str(self.uangSaku)\
            + ' tiap bulannya.'
        return s
#nomer 4
    listKuliah = []
    def ambilKuliah(self,Makul):
        self.listKuliah.append(Makul)

        
#nomer 5
    def hapusKuliah(self,Makul):
        if Makul in self.listKuliah:
            self.listKuliah.remove(Makul)
            print("Berhasil Menghapus Kuliah",Makul,"dari List")
        else:
            print("Mata Kuliah",Makul,"belum diambil")
