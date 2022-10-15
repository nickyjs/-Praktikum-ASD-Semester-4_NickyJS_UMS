#Nicky julyatrika Sari L200200101
#UTS Praktikum ASD

#Nomer 1a
print("---->> Program Menghitung Luas Persegi <<-----")
sisi = int(input("Masukkan sisi =  " ))
def Persegi(sisi):
    Luas = sisi * sisi
    return Luas
print("Luas persegi dengan sisi =", sisi, "adalah" , Persegi(sisi), "satuan luas")
print(" ")

#Nomer 1b
print("---->> Program Menghitung Luas Lingkaran <<-----")
jari = int(input("Masukkan jari-jari =  " ))
def Lingkaran(jari):
    phi = 3.14
    Luas = phi * (jari**2)
    return Luas
print("Luas lingkaran dengan jari-jari =", jari, "adalah" , Lingkaran(jari), "satuan luas")
print(" ")

#Nomer 1c
print("---->> Program Menghitung Luas Segitiga Samasisi <<-----")
alas = int(input("Masukkan alas =  " ))
tinggi = int(input("Masukkan tinggi =  " ))
def Segitiga(alas, tinggi):
    Luas = 0.5 * (alas * tinggi)
    return Luas
print("Luas segitiga samasisi dengan alas =", alas, "dan tinggi =", tinggi, "adalah" , Segitiga(alas, tinggi), "satuan luas")
print(" ")

#Nomer 1d
print("---->> Program Menghitung Belah Ketupat <<-----")
d1 = int(input("Masukkan diagonal 1 =  " ))
d2 = int(input("Masukkan diagonal 2 =  " ))
def belahKetupat(d1, d2):
    Luas = 0.5 * (d1 * d2)
    return Luas
print("Luas belah ketupat dengan diagonal 1 =", d1, "dan diagonal 2 =", d2, "adalah" , belahKetupat(d1, d2), "satuan luas")


