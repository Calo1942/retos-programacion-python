"""
* Crea un programa que invierta el orden de una cadena de texto
* sin usar funciones propias del lenguaje que lo hagan de forma automática.
* - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

entrada = input("escribe una palabra o frase a invertir: ")
end_index = len(entrada)-1
inverted = ""
while end_index > -1:
    inverted = inverted + entrada[end_index]
    end_index -= 1
print(inverted)