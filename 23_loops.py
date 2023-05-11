#ciclos dentro de ciclos

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[0][2])
#Lo anterior impreme la lista que se encuentra en la primer posicion = 0 y dentro de esa lista el numero que esta en posicion 2 = 3

for element in matriz:
    print(element)
    for item in element:
        print(item)
