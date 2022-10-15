#Modul 3 Nicky Julyatrika Sari L200200101
#Nomer 1
a = [[2, 3], [5, 7]]
b = [[2, 4], [8, 9]]
c = [[3, 4], [5, 9], [1, 2,5]]

#Memastikan isi dan ukuran matriks sudah sesuai
def cekMatrix(x):
    for i in x :
        if len(i) != len(x):
            return "Isi dan ukuran matriks tidak konsisten"
            break
        else:
            return "isi dan ukuran matriks sudah konsisten"

#Mengambil ukuran Matrix
def ambilUkMatrix(x):
    hasil = len(x), len(x[0])
    return hasil

#Menjumlahkan dua matrix
def jmlMatrix(x, y):
    hasil = []
    for i in range(len(x)):
        new = []
        for j in range(len(x[i])):
            new.append(x[i] [j] + y[i] [j])
        hasil.append(new)
    return hasil

#Mengalikan dua Matrix       
def kaliMatrix(x, y):
    hasil = []
    for i in range(len(x)):
        new = []
        for j in range(len(x[i])):
            new.append(x[i] [j] *  y[i] [j])
        hasil.append(new)
    return hasil

#Menghitung Determinan Matrix
def detMatrix(x):
    hasil = []
    for i in range(len(x)):
        if i == 0:
            ad = x[i][i] * x[i+1][i+i]
        elif i == 1 :
            bc = x[i-1][i] * x[i][i-1]
    hasil = (ad - bc)
    return hasil
