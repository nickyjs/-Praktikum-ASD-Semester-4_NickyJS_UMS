#NICKY JULYATRIKA SARI NIM L200200101
#Modul 7
#nomer 3

import re
op = open("indonesia.txt","r")
s = op.read()
op.close()
pola = r'di\s\w+'
tampil = re.findall(pola, s)
print(tampil)
