"""
* Crea un programa que cuente cuantas veces se repite cada palabra
* y que muestre el recuento final de todas ellas.
* - Los signos de puntuación no forman parte de la palabra.
* - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
* - No se pueden utilizar funciones propias del lenguaje que
*   lo resuelvan automáticamente.
"""

texto = "Las personas tienen miedo de que otras personas las lastimen, las mismas que dicen amarlas"
texto = texto.casefold()
texto = texto.replace(",", "")

lista_palabras = texto.split()

lista_repeticiones = []

for i in lista_palabras:
    
    contador = 0
    ciclo = 0

    while ciclo < len(lista_palabras):
        if i == lista_palabras[ciclo]:
            contador += 1
        ciclo += 1

    palabra = [i, contador]
    if palabra not in lista_repeticiones:
        lista_repeticiones.append(palabra)

print(lista_repeticiones)
