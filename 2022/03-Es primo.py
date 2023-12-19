"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo(num): 
    divisores = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    if len(divisores) == 2:
        return True
    else:
        return False

primos = []

for i in range(1, 101):
    if es_primo(i):
        primos.append(i)

print(primos)