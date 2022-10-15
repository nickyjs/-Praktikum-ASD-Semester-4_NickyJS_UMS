#Soal Nomer 14 Nicky Julyatrika Sari L200200101
#Modul 1
def formatRupiah(bil):
    a = str(bil)
    if len(a) <= 3:
        return "Rp" + a
    else:
        c = a[-3:]
        d = a[:-3]
        return formatRupiah(d) + "." + c
        print ("Rp") + formatRupiah(d) + "." + c
