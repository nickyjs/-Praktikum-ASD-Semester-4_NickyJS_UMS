#Soal Nomer 12 Nicky Julyatrika Sari L200200101
#Modul 1


def tebakAngka(angka):
    import random
    angka = random.randint(1,100)
    percobaan = 1
    print("Permainan tebak angka")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")
    while(percobaan<=7):
        tebak = input("Masukkan tebakan ke-"+str(percobaan)+":> ")
        if int(tebak) < angka:
            print("Itu terlalu kecil. Coba lagi.")
        elif int(tebak) > angka:
            print("Itu terlalu besar. Coba lagi.")
        else:
            print("Ya. Anda benar")
            break
        percobaan += 1
