"""
Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO
  estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
  estén presentes en str1.
"""

vacio = ""
str1 = "hola vez"
str2 = "hole beca"

def eliminando_caracteres(str1, str2):

    str1, str2 = str1.replace(" ", ""), str2.replace(" ", "")

    def no_esta_presente(str1, str2): 
        out = ""
        for char in str1:
            if not char in str2:
                out += char
        return out

    out1 = no_esta_presente(str1, str2)
    out2 = no_esta_presente(str2, str1)

    return f" out1: '{out1}'\n out2: '{out2}'"

print(eliminando_caracteres(str1, str2))
