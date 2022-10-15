#Nicky julyatrika Sari L200200101
#UTS Praktikum ASD

#Nomer 2a
def kaliMatrix(x,y):
    a = 0
    t, u = 0, 0
    for i in range(len(x)):
        t += 1
        u = len(x[i])
    v, w = 0, 0
    for i in range(len(y)):
        v += 1
        w = len(y[i])

    if(u == v):
        print("Hasil Perklian Matrix = ")
        vwtu = [[0 for j in range(w)] for i in range(t)]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    vwtu[i] [j] =+ x[i] [k] * y[k] [j]
        print(vwtu)

    else:
        print("Tidak memenuhi syarat")
        
#Nomer 2b        
def buatIdentitas(angka):
    matriks = [[1 if b == a else 0 for b in range(angka)]
               for a in range(angka)]
    for i in matriks:
        print(i)
    print("Matriks identitas tersebut berordo",angka,'x',angka)
