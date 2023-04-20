#if es un cocndicional, si la  condicion es True se ejecuta, si es False, no se ejecutará
if True:
  print("deberia ejecutarse")
if False:
  print("no deberia ejecutarse")

pet = input("¿Qué mascota tienes?")

if pet == "perro":
  print("que bien, pero no lo llames Popi")
#elif se coloca para que despues de determinar una respuesta el programama no siga validando las demas opciones, que son las que tienen elif
elif pet == "gato":
  print("Genial, pero esconde la comida del perro")

#if viene acompañado del condicional else = entonces. Asi que si algo no es True, entonces... va a hacer lo que le pidamos.
else:
  print("mejor un perro o un gato")
  