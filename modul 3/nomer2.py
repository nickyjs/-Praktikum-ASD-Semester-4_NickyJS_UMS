#Modul 3 Nicky Julyatrika Sari L200200101

#Nomer 2a
def buatNol(a, b):
    x = [[0 for i in range(a)] for j in range(b)]
    print(x)

def buatNoll(a):
    x = [[0 for i in range(a)] for j in range(a)]
    print(x)

b = [[2, 3], [1, 2]]

#Nomer 2b
def buatIdentitas(a):
    x = [[1 if j == 1
    else 0 for j in range(a) for i in range(a)]]
    print(x)

b = [[0, 1], [9, 8]]
