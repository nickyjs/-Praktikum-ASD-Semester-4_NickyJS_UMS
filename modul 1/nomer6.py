#Nomer 6 Nicky Julyatrika Sari l200200101
#Modul 1
def bilanganPrima(n):
    for i in range(2, n):
        prima = True
        for j in range(2,i):
            if(i%j==0):
                prima = False
        if(prima):
                print(i)
                
