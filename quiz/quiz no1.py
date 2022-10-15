#Nicky Julyatrika Sari NIM L200200101
#QUIZ
#NOmer 1

import re
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A_Z|a-z]{2,})+')

def check(email):
    if(re.search(regex,email)):
        print("True")
    else:
        print("False")

if __name__ == '__main__' :
    
    email = "nicky@yahoo.co.id"
    check(email)

    email = "nicky@gmail.com"
    check(email)

    email = "nicky@com"
    check(email)

