#Nicky Julyatrika Sari NIM L200200101
#QUIZ
#NOmer 2

import re

email = (input ("Masukkan Email : " ))
cocok = re.search("ums[^@]+[^@]+\.[^@]+", email)
if cocok:
    print("True")
else:
    print("False")

#nicky@ums.ac.id
#nicky@ums.com
#nicky@student.ums.ac.id
#nicky@uns.ac.id
