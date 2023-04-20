x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(y == x)
#Aunque la suma de y equivale a x la preciosion en decimales (numeros flotantes) es diferente, por lo que al compararlos daria False
#Se soluciona pasando a string para quitarle los decimales. Le cambio el formato y solo le pido dos digitos con "2g"
y_str = format(y, "2g")
print(y_str)
#Esto dará como resultado string "3.3" y para que la comparacion sea True debemos pasar X a string tambien
print(y_str == str(x))
#ahora si la comparacion de strings da True

#====================================
# Solucion Matematica
tolerancia = 0.0001
print(abs(y - x) < tolerancia)
#restamos el x - y, si el resultado esta dentro de la tolerancia porque los numeros son casi iguales, entonces dara True. abs = valor absoluto