#NICKY JULYATRIKA SARI NIM L200200101
#Modul 7
#nomer 2

import re
op = open("indonesia.txt","r")
s = op.read()
op.close()
pola = r'di\w+'
tampil = re.findall(pola, s)
print(tampil)
