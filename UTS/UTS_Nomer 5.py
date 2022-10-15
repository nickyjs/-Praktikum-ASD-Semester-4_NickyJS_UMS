#Nicky julyatrika Sari L200200101
#UTS Praktikum ASD

#Nomer 5
class dataPersonal(object):
    def __init__(self, nama, umur, kulit):
        self.nama = nama
        self.umur = umur
        self.kulit = kulit

a1 = dataPersonal("Julya", 15, "Kuning Langsat")
a2 = dataPersonal("Cindi", 18, "Sawo Matang")
a3 = dataPersonal("Rida", 23, "Putih")
a4 = dataPersonal("Dionica", 24, "Sawo Matang")
a5 = dataPersonal("Fajar", 14, "Sawo Matang")
a6 = dataPersonal("Nicky", 21, "Putih")
a7 = dataPersonal("Diego", 19, "Putih")
a8 = dataPersonal("Alfian", 20, "Kuning Langsat")
a9 = dataPersonal("Arina", 22, "Putih")
a10 = dataPersonal("Andro", 16, "Sawo Matang")

Daftar = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]

def urutkan(x):
    a = len(x)
    for i in range(1, a):
        angka = x[i]
        posisi = i

        while posisi > 0 and angka.umur < x[posisi-1].umur:
            x[posisi] = x[posisi-1]
            posisi = posisi - 1
        x[posisi] = angka

def urutkanUsia(y):
    for i in y:
        print(i.nama, i.umur, i.kulit)
