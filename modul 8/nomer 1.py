#Nicky Julyatrika Sari NIM L200200101
#Modul 8
#Nomer 1

class Stacks():
    def __init__(self):
        self.items =[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip."
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop."
        return self.items.pop()
    def push(self,data):
        self.items.append(data)

def cetakHexa(bil):
    x = Stacks()
    if bil == 0: x.push(0);
    while bil != 0:
        if bil % 16 == 10:
            sisa = "A"
        elif bil % 16 == 11:
            sisa = "B"
        elif bil%16 == 12:
            sisa = "C"
        elif bil % 16 == 13:
            sisa = "D"
        elif bil % 16 == 14:
            sisa = "E"
        elif bil % 16 == 15:
            sisa = "F"
        else:
            sisa = bil % 16
        bil = bil // 16
        x.push(sisa)
    string = ""
    for i in range (len(x)):
        string = string + str(x.pop())
    return string
                
                
