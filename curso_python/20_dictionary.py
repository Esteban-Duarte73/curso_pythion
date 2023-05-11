persona = {
    'name' : 'Esteban',
    'last_name' : 'Duarte',
    'langs' : ['python', 'java'],
    'age' : 33 
}

print(persona)

#actualizacion de nobre al diccionario
persona['name'] = 'Alejandro'

#restar o sumar a un numero
persona['age'] -= 13

#podemos agregar con .append
persona['langs'].append('gooland')

#elminar del diccionario
del persona['last_name']

persona.pop('age')
print(persona)

#obtener items de un diccionario
print('items')
print(persona.items())

#obtener las keys
print('keys')
print(persona.keys())

#obtener values
print('values')
print(persona.values())
