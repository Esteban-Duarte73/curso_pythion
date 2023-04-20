# listados de numeros aunque puede contener datos de todo tipo, numero, string, booleans etc
numbers = [1, 2, 3, 4]
types = [1, True, "hola"]
print(numbers)
print(type(numbers))

#Puedo actualizar el valor de una o varias posicines de la lista, en este caso, de numeros
numbers[0] = "uno"
print(numbers)
#la salida será ['uno', 2, 3, 4]

#puedo impirmir solo una parte de la lista
print(numbers[0:3]) # == print(numbers[:3])