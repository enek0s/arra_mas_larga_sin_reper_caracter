"""
Ejerc: Coger la cadena de letras mas larga sin repetir caracteres

Logica:

Mirar uno por  (caracter) y contar cuanta distancia hay hasta que se repite
---------------------------------------------------------------------------
Solucion:
for caracter in len(lista)
    cantidad_de_caracteres=0
    lista mas larga = []
    lista mas larga 2 = []
    while caracter != caracter+1
        cantidad_de_caracteres mas uno
        lista mas larga.append(caracter)

"""


array = ['abcabcbb']
lista = list(array[0])
print(lista)

lista_mas_larga = []

for i, caracter in enumerate(lista):

    lista_aux = []

    posicion_siguiente = i

    while posicion_futura < len(lista) and lista[posicion_futura] not in lista_aux:
        
        lista_aux.append(lista[posicion_futura])
        posicion_futura += 1

    if len(lista_aux) > len(lista_mas_larga):

        lista_mas_larga = lista_aux

print(len(lista_mas_larga))




        
