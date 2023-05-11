#loops: For es un ciclo que se utiliza para cuando ya tenemos un numero de elementos o condiciones dadas.
''''
for element in range(1, 20):
    print(element)
#range se puede modificar para darle el rango que queremos que recorra
'''

#ejemplo para recorrer una lista

my_list = [23, 45, 67, 89, 43]
for element in my_list:
 print(element)

my_tuple = ('esteban', 'nico', 'javi')
for element in my_tuple:
  print(element)

producto = {
  'name' : 'camisa',
  'prie' : 100,
  'stock' : 89  
}

for key in producto:
  print(key, '=>', producto[key])
