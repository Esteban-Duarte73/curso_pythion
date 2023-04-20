#CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])

#con .append podemos agregar un numero al final de la lista
numbers.append(700)
print(numbers)

#con .insert podemos agregar en la posicion que queramos
numbers.insert(0, "hola")
print(numbers)

numbers.insert(3, "chao")
print(numbers)

#Podemos fusionar listas

letras = ['uno', 'dos', 'tres', 'cuartro']
new_list = numbers + letras
print(new_list)

#preguntemos en que posicion esta un elemento

print(new_list.index('dos'))
#la salida me muestra la posicion en la que está

# para eliminar de la lista usamos .remove
new_list.remove('tres')
print(new_list)
# elimininamos el ultimo de la lista con  .pop() o le puedo agregar la posicion .pop(1)
new_list.pop()
print(new_list)

new_list.pop(1)
print(new_list)

# cambiar el orden de la lista con .reverse()
new_list.reverse()
print(new_list)

# puedo pedirle ordenar una lista de numeros en orden ascendente con .sort
numbers_ordenar = [4 , 7, 2, 8, 12]
numbers_ordenar.sort()
print(numbers_ordenar)