#podemos cambiar el tipado del codigo y la manera como lo interpreta python
name = "Esteban"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

#No se puede concatenar diferentes tipos, como vemos en el siguiente ejemplo
# age = 33
# print("mi edad es " + age)
# esto nos genera error. pero podemos hacer que el numero sea tratado como string de la siguiente manera
age = 33
print("mi edad es " + str(age))
#agregando el str = string
print(f"mi edad es {age}")

age = input("Escribe tu edad ")
print(type(age))
#Python trata todo lo que entra en un input como string, aunque sea un numero
age = int(age)
#por lo que tuvimos que transformarlo a numero con int = entero
age += 10
print(f"Tu eadad en 10 años será {age} años")
#pero podriamos tomar la expresion de la linea 18 y pasarla de una vez a int de la siguiente manera
age = int(input("Escribe tu edad "))
print(type(age))