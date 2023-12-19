"""
 Crea un programa que sea capaz de transformar entrada natural a código
 morse y viceversa.
 - Debe detectar automáticamente de qué tipo se trata y realizar
   la conversión.
 - En morse se soporta raya "—", punto ".", un espacio " " entre letras
   o símbolos y dos espacios entre palabras "  ".
 - El alfabeto morse soportado será el mostrado en
   https://es.wikipedia.org/wiki/Código_morse.
"""

import string

todas_letras_num_sybols = string.ascii_letters + string.digits

morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# input
texto = "----- .---- ..---  ...-- ....- ....."
texto = ".... --- .-.. .-  .- -- .. --. --- ...  -.. .  -.-- --- ..- - ..- -... . -.-.--  --.- ..- .  - .- .-.. ..--.."
texto = "¡Hola mundo! ¿Que tal?"
texto = "Hoy es 24 de julio, y estoy muy feliz!"
texto = texto.replace("¿", "")
texto = texto.replace("¡", "")
entrada = texto.lower()
conversion = "" 

# verify if is morse or text
is_morse = True
for letra in entrada:
    if letra in todas_letras_num_sybols:
        is_morse = False
        break

# funtion to find value key
def encontrar_clave(diccionario, valor_buscado):
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            return clave
    return None

if is_morse:    # if is morse code
    # creating separation
    entrada += "|" 
    entrada = entrada.replace("  ", "|")
    # creating list of lists with the diferents words
    letras = []
    palabras = []
    caracter = ""
    for i in entrada:
        if i == "." or i == "-":
            caracter = caracter + i
        elif i == " ":
            letras.append(caracter)
            caracter = ""
        elif i == "|":
            letras.append(caracter)
            palabras.append(letras)
            letras = []
            caracter = ""
    
    for palabra in palabras:
        for letra in palabra:
            if letra in morse_code.values():
                caracter = encontrar_clave(morse_code, letra)
                conversion += caracter
        if palabra != "":
            conversion += " "
else:   # if not is morse code (is text)
    for letra in entrada:
        if letra != " ":
            clave = morse_code[letra]
            conversion = conversion + clave + " "
        elif letra == " ":
            clave = " "
            conversion = conversion + clave

print(f"Input :{texto}")
print(f"Output :{conversion}")