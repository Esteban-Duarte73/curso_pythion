# in nos permite saber si una palabra o grase esta dentro de un string. De ser asi nos arrojara un true
text = "Ella sabe programar en Python"
print("Ella" in text)
print("sabe programar" in text)

if "Ella sabe" in text:
  print("claro que ella si sabe!")
else:
  print("ella no sabe programar")

# para el numero de caracteres INCLUYENDO espacios se usa len
numero_caracteres = len("amor")
print(numero_caracteres)

tamaño = len(text)
print(tamaño)

# podemos pasar todo un string a mayusculas con upper
print(text.upper())
# podemos pasar todo un string a minuscula con lower
print(text.lower())
# podemos invertir minusculas con mayusculas y biseversa con swapcase
print(text.swapcase())
# contar cuantas veces aparaece un caracter en un string con count. Por ejemplo contemos la "a"
print(text.count("a"))
#saber si un string inicio con una palabra especifica con startswith(palabra). Nos respodera con boolean True o False
print(text.startswith("Ella"))
#saber si un string inicio con una palabra especifica con endswith(palabra). Nos respodera con boolean True o False
print(text.endswith("Python"))
#Remplazar palabra en el string replace.("palabra_original", "nueva_palabra")
print(text.replace("Python", "Go"))
#Colocar el primer caracter en mayuscula capitalize text_2 = "yo tambien se programar"
text_2 = "yo tambien se programar"
print(text_2.capitalize())
#El inicio de cada plabra en mayuscula title
print(text_2.title())
# saber si un texto es un digito isdigit y responde con boolean
print(text_2.isdigit())