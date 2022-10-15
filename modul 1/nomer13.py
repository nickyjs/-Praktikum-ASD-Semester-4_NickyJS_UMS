#Soal Nomer 10 Nicky Julyatrika Sari L200200101
#Modul 1
def Terbilang(n):
    nilai = ['','Satu','Dua','Tiga','Empat','Lima',
              'Enam','Tujuh','Delapan','Sembilan','Sepuluh','Sebelas']
    if n <= 1000000000:
        hasil=''
        if n >= 0 and n <= 11:
            hasil = nilai[n]
        elif n <20:
            hasil = nilai[n-10] + ' Belas'
        #puluhhan (30,40m50 dst)
        elif n < 100:
            hasil = Terbilang(int(n/10)) + " Puluh " + nilai[n%10]
        elif n < 200:
            hasil = 'Seratus ' + Terbilang(int(n-100))
        elif n < 1000:
            hasil = Terbilang(int(n/100)) + ' Ratus '+ Terbilang(int(n%100))
        elif n < 2000:
            hasil = 'Seribu '+Terbilang(n-1000)
        elif n < 1000000:
            hasil = Terbilang(int(n/1000)) + ' Ribu ' + Terbilang(int(n%1000))
        elif n < 1000000000:
            hasil = Terbilang(int(n/1000000)) + ' Juta '+ Terbilang(int(n%1000000))
        elif n == 1000000000:
            hasil = "Satu Milyar"
        
        return str(hasil)

    else:
        return "Jumlah tidak boleh lebih dari 1 milyar"
