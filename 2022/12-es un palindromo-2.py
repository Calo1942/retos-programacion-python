"""
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
"""

ejemplo1 = "áéíóúñ"
ejemplo2 = "abcdefghijklm"
ejemplo3 = "Anita lava la tina."
ejemplo4 = "Dábale arroz a la zorra el abad."


ejemplo = "Aná lleva al oso la avellana"
def palindromo(text_input):

    def limpiando_input(texto):

        reemplazos = {
            "á": "a",
            "é": "e",
            "í": "i",
            "ó": "o",
            "ú": "u",
            ",": "",
            " ": "",
            ".": "",
        }

        texto = texto.lower()

        for char in reemplazos:
            if char in texto:
                texto = texto.replace(char, reemplazos[char]) 
        return texto

    return True if limpiando_input(text_input) == limpiando_input(text_input)[::-1] else False

print(palindromo(ejemplo3))
