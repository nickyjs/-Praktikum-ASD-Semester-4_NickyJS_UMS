#Nomer 3 Nicky Julyatrika Sari L200200101 Modul 2
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
        s = self.nama + ',Dengan NIM '+ str(self.NIM)\
            + '. Tinggal di '+ self.kotaTinggal \
            + '. Memiliki Uang saku Rp '+ str(self.uangSaku)\
            + ' tiap bulannya.'
        return s
