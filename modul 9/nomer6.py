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

#nomer 6

def ukuranPohon(akar):
    if akar is None :
        return 0
    else :
        return (ukuranPohon(akar.kiri) + 1 + ukuranPohon(akar.kanan))
print('Ukuran pohon A : ', ukuranPohon(A))
                

