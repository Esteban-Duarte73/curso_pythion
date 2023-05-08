#Las tuplas son una estrucutra de datos que contiene un secuencia ordenada de elementos inmutables (no podemso hacer cambios sobre ellas)
numbers = (1,2,3,4,5)
string = ('esteban', 'yolanda', 'juanda', 'esteban')

print(type(numbers))
print(type(string))
#la salida lo identifica como una tuple (tupla)

#para encontrar la posicion de un elemento de la tupla usamos index
print(string.index('esteban'))

# para saber cuantas veces hay un elemento en la tupla usamos count
print(string.count('esteban'))
#el resultado será 2 en este caso

#podemos transformar una tupla a lista para poder modificar los valores
nueva_lista = list(numbers)
print(nueva_lista)
print(type(nueva_lista))

#tambien podemos cambiar de lista a tuple
nueva_tuple = tuple(nueva_lista)
print(nueva_tuple)
print(type(nueva_tuple))