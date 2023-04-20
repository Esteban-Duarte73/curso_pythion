# operadores logicos and y or
print("AND")
print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)
print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)
#En AND las dos operaciones tienen que ser True para que el resultado sea True, de lo contrario será False

# operador or
print("or")
print("True or True =>", True or True)
print("True or False =>", True or False)
print("False or True =>", False or True)
print("False or False =>", False or False)
print(10 > 5 or 5 < 10)
print(10 > 5 or 5 > 10)
print(10 < 5 or 5 > 10)
#En or, solo da falso cuando los dos elemntos comparados sean falsos, pero si al menos un es True, dará True