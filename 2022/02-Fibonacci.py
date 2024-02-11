"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

fibo = [0, 1]

for i in range(0, 48):
    fibo.append(fibo[-2]+fibo[-1])

print(fibo)

"""
lista_fibo = []

lista_fibo.append(0)
lista_fibo.append(1)

while len(lista_fibo) < 50:
    penultimo_index, ultimo_index = len(lista_fibo)-2, len(lista_fibo)-1
    nuevo_valor = (lista_fibo[penultimo_index] + lista_fibo[ultimo_index])
    lista_fibo.append(nuevo_valor)

print("lista: ", lista_fibo)
"""