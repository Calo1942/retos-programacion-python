"""
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
"""

ejemplo = "Aná lleva al oso la avellana"
ejemplo1 = "áéíóúñ"
ejemplo2 = "abcdefghijklm"
ejemplo3 = "Anita lava la tina."
ejemplo4 = "Dábale arroz a la zorra el abad."


def palindromo(text_input):

    def limpiando_input(texto):

        reemplazos = {
            "á": "a",
            "é": "e",
            "í": "i",
            "ó": "o",
            "ú": "u",
        }

        texto = texto.lower()
        texto = texto.replace(" ", "")
        texto = texto.replace(".", "")
        texto = texto.replace(",", "")
        resultado = ""

        for char in texto:
            if char in reemplazos.keys():
                char = reemplazos[char]
                resultado += char
            else:
                resultado += char
        return resultado

    texto_original = limpiando_input(text_input)

    texto = texto_original
    texto_reversa = ""

    while texto != "":
        texto_reversa += texto[-1]
        texto = texto[:-1]

    print(text_input)
    print(texto_reversa)

    if texto_reversa == texto_original:
        return True
    else:
        return False
    
print(palindromo(ejemplo4))