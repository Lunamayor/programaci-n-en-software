# #-----------------------------TALLER, PRIMERA PARTE ES DE CONDICIONALES Y OPERACIONE MATEMÁTICAS-----------------------

# 1. Verifica si un número es positivo, negativo o cero
num = float(input("Ingresa un número: "))
if num > 0:
    print(f"{num} es positivo")
elif num < 0:
    print(f"{num} es negativo")
else:
    print(f"{num} es cero")

# 2. Calcula el mayor de dos números ingresados
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
if num1 > num2:
    print(f"El mayor de los dos números es {num1}")
else:
    print(f"El mayor de los dos números es {num2}")

# 3. Determina si un número es par o impar
num = int(input("Ingresa un número: "))
if num % 2 == 0:
    print(f"{num} es un número par")
else:
    print(f"{num} es un número impar")

# 4. Dado un número, verifica si está entre 10 y 20
num = float(input("Ingresa un número: "))
if 10 <= num <= 20:
    print(f"{num} está entre 10 y 20")
else:
    print(f"{num} no está entre 10 y 20")

# 5. Dados tres números, encuentra el mayor usando condicionales
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
if num1 >= num2 and num1 >= num3:
    print(f"El mayor de los tres números es {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El mayor de los tres números es {num2}")
else:
    print(f"El mayor de los tres números es {num3}")

# 6. Calcula el precio final con un 10% de descuento si el total es mayor a $100
precio = float(input("Ingresa el precio: "))
if precio > 100:
    precio_final = precio * 0.9
    print(f"El precio final con el 10% de descuento es ${precio_final:.2f}")
else:
    print(f"El precio final es ${precio:.2f}")

# 7. Verifica si una persona puede votar (mayor o igual a 18 años)
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")

# 8. Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP
precio = float(input("Ingresa el precio: "))
tipo_cliente = input("Ingresa el tipo de cliente (VIP o normal): ")
if tipo_cliente.upper() == "VIP":
    precio_final = precio * 0.8
    print(f"El precio final con el 20% de descuento es ${precio_final:.2f}")
else:
    print(f"El precio final es ${precio:.2f}")

# 9. Determina si un número es múltiplo de 5 y de 3 al mismo tiempo
num = int(input("Ingresa un número: "))
if num % 5 == 0 and num % 3 == 0:
    print(f"{num} es múltiplo de 5 y de 3 al mismo tiempo")
else:
    print(f"{num} no es múltiplo de 5 y de 3 al mismo tiempo")

# 10. Dado un número, verifica si es divisible entre dos números dados
num = int(input("Ingresa un número: "))
div1 = int(input("Ingresa el primer divisor: "))
div2 = int(input("Ingresa el segundo divisor: "))
if num % div1 == 0 and num % div2 == 0:
    print(f"{num} es divisible entre {div1} y {div2}")
else:
    print(f"{num} no es divisible entre {div1} y {div2}")


#-----------------------------TALLER, PRIMERA PARTE ES DE CONDICIONALES Y OPERACIONE MATEMÁTICAS-----------------------
#11









