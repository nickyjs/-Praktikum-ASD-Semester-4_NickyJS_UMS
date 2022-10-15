#Soal Nomer 10 Nicky Julyatrika Sari L200200101
#Modul 1
def apakahKabisat(th):
    hsl = False
    if(th%4==00 and th%100!=0 and th&400!=0):
        hsl = True
    elif(th%100==0 and th%400!=0):
        hsl = False
    elif(th%400==0):
        hsl = True
    else:
        hsl = False
    return hsl
