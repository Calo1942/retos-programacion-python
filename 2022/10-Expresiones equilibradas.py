"""
 Crea un programa que comprueba si los paréntesis, llaves y corchetes
 de una expresión están equilibrados.
 - Equilibrado significa que estos delimitadores se abren y cieran
   en orden y de forma correcta.
 - Paréntesis, llaves y corchetes son igual de prioritarios.
   No hay uno más importante que otro.
 - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

expresion1 = "{[a*(c+d)]-5}"
expresion2 = "{ a * ( c + d ) [] - [(5)] }"

# lo primero que necesitamos es crear una pila (lista) y 
# que se tienen que cerrar en el orden exacto en el que lo tienen que hacer

def equilibrada(expresion):

  pila = []
  delim = { "}" : "{", "]" : "[", ")" : "("} # así la clave es final y el valor es el comienzo

  for caracter in expresion:
      if caracter in delim.values():
          pila.append(caracter)
      elif caracter in delim.keys():
          if pila.pop() != delim[caracter]:
              return False
  return not pila

print(equilibrada(expresion1))
