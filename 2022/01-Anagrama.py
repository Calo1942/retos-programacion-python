"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """

def es_anagrama():
    
    entrada1 = input("Primera palabra: ")
    entrada2 = input("segunda palabra: ")
    caracteres1 = list(entrada1)
    caracteres2 = list(entrada2)

    if caracteres1 != caracteres2 and len(caracteres1) == len(caracteres2):
        for i in caracteres1:
            if i in caracteres2:
                caracteres2.remove(i)
            else:
                print(False)
                break
        if len(caracteres2) == 0:
            print(True)
    elif len(caracteres1) != len(caracteres2):
        print("las palabras no tienen el mismo tamaño")        
    else:
        print("No es un anagrama")

es_anagrama()
