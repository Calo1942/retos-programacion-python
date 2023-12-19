"""
* Crea un programa se encargue de transformar un número
* decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

num = 3001
num = str(num)

num_bi = ""

for i in num:
    if i == "0":
        cifra_bi = "000000 "
    elif i == "1":
        cifra_bi = "000001 "
    elif i == "2":
        cifra_bi = "000010 "
    elif i == "3":
        cifra_bi = "000011 "
    elif i == "4":
        cifra_bi = "000100 "
    elif i == "5":
        cifra_bi = "000101 "
    elif i == "6":
        cifra_bi = "000110 "
    elif i == "7":
        cifra_bi = "000111 "
    elif i == "8":
        cifra_bi = "001000 "
    elif i == "9":
        cifra_bi = "001001 "
    num_bi = num_bi + cifra_bi
    
print(num_bi)