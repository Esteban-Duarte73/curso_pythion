# esta funcion solo escoje la letra que está en la posicion solicitada del string
text = "El sabe python"
print(text[0])
print(text[1])
print(text[8])
# Para conocer la posicion del ultimo caracter del texto [-1]
print(text[-1])
# Para conocer la posicion del penultimo caracter del texto [-2] y etc
print(text[-2])

# para poder sacar una palabra basada en su posicion o ciertos caracteres sehace asi
print(text[0:8]) # esto es igual a colocar
print(text[:8]) # si no hay nada antes de los : el por default recibe un 0
print(text[1:]) # si no hay nada despues de los : por defoult el va al ultimimo caracter
print(text[:]) # lo mismo aplica si solo estan los :
#Si quiero que haga algunos saltos lo podemos hacer al final con :
print(text[0:-1:2])
print(text[::2])