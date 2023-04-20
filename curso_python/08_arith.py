print(10 + 10)
print(10 - 10)
print(10 * 10)
print(10 / 10)
#Con doble slash el resultado muestra solo el numero entero
print(10 // 10)
#Si queremos ver el residuo de la division usamos % para detectar si un numero es par o impar
print(10 % 10)
#El numero exponencial o elevado a, se hace con un ** asterisco doble
print(10 ** 2)
#tambien podemos multiplicar un string
print("hola " * 3) #output = hola hola hola

#El orden en que python resuelva las ecuaciones es:
# P - parentesis
# E - exponentse
# M - multiplicacion
# D - division
# A - adicion
# S - sustraccion
#esta prioridad debemos usarla de izquierda a derecha
print(2 ** 3 + 3 - 7 /1 //4)
#asi las cosas primero se resuelve 2 elevado a la 3, luego 7 / 1 y el resultado se divide entre // 4 pero con resultado entero quedanso asi:
# 8 + 3 - 1 = 10
