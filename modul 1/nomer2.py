#Nomer 2 Nicky Julyatrika Sari l200200101
#Modul 1
def Gambarlahpersegiempat(x,y):
    for i in range(x):
        if i == 0  or i == x-1:
            print ('@'*y)
        else:
           print ('@' + ' ' *(y-2)+'@')
