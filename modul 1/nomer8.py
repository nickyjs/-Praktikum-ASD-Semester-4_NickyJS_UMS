#Nomer 6 Nicky Julyatrika Sari l200200101
#Modul 1
def apakahTerkandung(a, b):
    n = True
    for i in range(len(b)):
        if a in b:
            n = True
        else:
            n = False
    return n
