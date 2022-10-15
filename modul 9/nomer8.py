#Nicky Julyatrika SariL200200101
#modul 9
#Soal pemrograman


class simpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri= None
        self.kanan= None

A = simpulPohonBiner('Ambarawa')
B = simpulPohonBiner('Bantul')
C = simpulPohonBiner('Cimahi')
D = simpulPohonBiner('Denpasar')
E = simpulPohonBiner('Enrekang')
F = simpulPohonBiner('Flores')
G = simpulPohonBiner('Garut')
H = simpulPohonBiner('Halmahera timur')
I = simpulPohonBiner('Indramayu')
J = simpulPohonBiner('Jakarta')

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; B.kanan = G
E.kiri = H
G.kanan = I

#nomer 8
d = [A.data, B.data, C.data, D.data, E.data, H.data, I.data, J.data]
def traverse(akar):
    levellist = []
    arlvl = [akar]
    lvl = 0
    while arlvl:
        nextlvl = list()
        for a in arlvl :
            if a.kiri :
                nextlvl.append(a.kiri)
                level.append(lvl + 1)
            if a.kanan :
                nextlvl.append(a.kanan)
                level.append(lvl + 1)
            arlvl = nextlvl
        lvl += 1
        levellist.append(lvl)
    return levellist

def cetak(akar):
    traverse(A)
    print(akar.data, ', level 0')
    for i in range(len(level)):
        print(d[i+1], ', Level', level[i])
level = []
cetak(A)
