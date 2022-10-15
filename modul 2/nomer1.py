#Nomer 1 Nicky Julyatrika Sari L200200101 Modul 2
class pesan(object):
    """."""
    def __init__(self,string):
        self.teks = string
    def ucapPesan(Self):
        print(self.teks)
    def cetakPakaiHrfKapital(self):
        print(str.upper(Self.teks))
    def cetakPakaiHrfKecil(self):
        print(str.lower(self.teks))
    def jml(self):
        return len(self.teks)
    def cetakJmlKarakter(self):
        print("Kalimatku mempunyai", len(self.teks), "karakter")
    def perbarui(self, StringNew):
        self.teks = SringNew

#Nomer 1a
    def apakahTerkandung(self,kata):
        if str(kata) in self.teks:
            return True
        else:
            return False
#Nomer 1b
    def hitungKonsonan(self):
        vokal = 'aiueo'
        a = 0
        for i in self.teks:
            if i not in vokal and i != ' ':
               a += 1
        return a
h            
#Nomer 1c
    def hitungVokal(self):
        vokal = 'aiueoAIUEO'
        a = 0
        for i in self.teks:
            if i in vokal and i != ' ':
               a += 1
        return a
        
        
  
