print("Daniel Gallegos NC 1392")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("=========Variables============")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Ejemplo 1 con una variable numerica y una cadena
x = 8
y = "Daniel"
print(x)
print(y)
print("---------------------")
# Ejemplo 2
x = 4       # x es de tipo int ahora
x = "Sally" # x es de tipo str ahora
print(x)
print("---------------------")
# Ejemplo 3 especificando el tipo de variable 
x = str(3)    # x sera '3'
y = int(3)    # y sera 3
z = float(3)  # z sera 3.0

print(x,"-",y,"-",z)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("=========Variables Multiples============")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Ejemplo 1 asignando valores a multiples variables
x, y, z = "Naranja", "Platano", "Cereza"
print(x)
print(y)
print(z)
print("------------------------")
# Ejemplo 2 asignando un unico valor a multiples variables
x = y = z = "Naranja"
print(x)
print(y)
print(z)
print("------------------------")
# Ejemplo 3 desempacando una lista
fruits = ["manzana", "platano", "cereza"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("===========Tipos de Datos===============")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Ejemplo 1 imprimiendo el tipo de dato
x = 5
print(type(x))
# Ejemplo 2 asignando un tipo de dato float()
x = float(20.5)
print(x)
# Ejemplo 3 asignando tipo de dato str()
x = str("Hola profe")
print(x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("=============Operadores=================")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Aritmeticos")
# Ejemplo 1 suma
print(2+3)
print("----------------")
# Ejemplo 2 resta
print(8-3)
print("----------------")
# Ejemplo 3 multiplicacion
print(5*4)
print("----------------")
print("Relacionales")
x = 5
y = 3
print(x,y)
print("Igual que ",x == y) # Igual que
print("Diferente que ",x != y) # Diferente que
print("Mayor que " ,x > y)  # Mayor que
print("Menor que ",x < y)  # Menor que
print("Mayor o igual que ",x >= y) # Mayor o igual que
print("Menor o igual que ",x <= y) # Menor o igual que
print("----------------")
print("Comparacion")
# Ejemplo 1 usando and
x = 5
print(x > 0 and x < 10)
# Ejemplo 2 usando or
x = 5
print(x < 5 or x > 10)
# Ejemplo 3 usando not
x = 5
print(not(x > 3 and x < 10))
print("Daniel Gallegos NC 1392")