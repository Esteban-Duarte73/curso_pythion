name = "Esteban"
last_name = "Duarte Prieto"
age = "33 años"
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

#debemos usar las comillas dobles o sencillas para que no interfieran con la sintxis del python
quote = "I'm Esteban"
quote2 = ' She said "hello"'
print(quote + quote2)

#manipular el formato format
template1 = "Hola, mi nombre es" + " " + name + " y mis apellidos son " + last_name + " " + "y tengo" + " " + age + "."
print("V1", template1)

template2 = "Hola, mi nombre es {} y mis apellidos son {}, y tengo {}." .format(name, last_name, age)
print("V2", template2)

template3 = f"Hola, mi nombre es {name}, mis apellidos son {last_name} y tengo {age}."
print("V3", template3)