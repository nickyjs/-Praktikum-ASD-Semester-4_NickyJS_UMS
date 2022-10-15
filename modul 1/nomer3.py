#Nomer 3a Nicky Julyatrika Sari l200200101
#Modul 1
def JumlahHurufVokal(hrf):
    vokal = 'aiueoAIUEO'
    a = 0
    hasil = 0
    for i in hrf:
        if i in vokal:
            a += len(i)
        else:
            a +=0

    hasil = len(hrf), a
    return hasil



#Nomer 3b Nicky Julyatrika Sari l200200101
def JumlahHurufKonsonan(hrf):
    konsonan = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    b = 0
    hasil = 0
    for i in hrf:
        if i in konsonan:
            b += len(i)
        else:
            b += 0

    hasil = len(hrf), b
    return hasil
