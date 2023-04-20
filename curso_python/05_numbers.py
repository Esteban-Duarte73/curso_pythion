lives_jumanji = 3
print(lives_jumanji)
print(type(lives_jumanji))
age = 33
buget = 100
temperature = 12.2
print(type(temperature))

#restar 
lives_jumanji -= 2
print(lives_jumanji)

#sumar
lives_jumanji += 2
print(lives_jumanji)

#la salida de numeros muy grandes la expresa de una manera diferente
numbera = 0.00000000000004
print(numbera)
# la salida fue 4e-14

#ejemplo de porcentaje de presupuesto de 3 mese

enero = 100
febrero = 180
marzo = 120

presupuesto = enero + febrero + marzo
porcentaje = presupuesto / 3
print(f"El valor maximo que se puede gastar en el primer trimestre del año por mes es de {porcentaje}")