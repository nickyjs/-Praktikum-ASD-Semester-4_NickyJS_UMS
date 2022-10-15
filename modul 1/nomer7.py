#Nomer 6 Nicky Julyatrika Sari l200200101
#Modul 1
def faktorPrima(x):
    bilList = []
    loop = 2
    while loop <= x:
        if x % loop == 0:
            x /= loop
            bilList.append(loop)
        else:
            loop += 1
    return bilList
