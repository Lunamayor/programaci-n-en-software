#2. calcula el mayor de dos numeros ingresados
n1=int(input("ingrese el  primer num: "))
n2=int(input("ingrese el segundo numero: "))
if n1>n2:
    print(f"el mayor es {n1}")
elif n2>n1:
    print(f"el mayor es el {n2}")


#-------------------------------------------TALLER 10 PREGUNTAS-----------------------------------------------


# 1. Verifica si un número es positivo, negativo o cero
num = int(input("Ingresa un número: "))
if num > 0:
    print(f"El número {num} es positivo.")
elif num < 0:
    print(f"El número {num} es negativo.")
else:
    print(f"El número {num} es cero.")

# 2. Calcula el mayor de dos números ingresados
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 > num2:
    print(f"El número mayor es {num1}.")
elif num2 > num1:
    print(f"El número mayor es {num2}.")
else:
    print("Los números son iguales.")

    
#3. Determina si un número es par o impar
num = int(input("Ingresa un número: "))
if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")

# 4. Dado un número, verifica si está entre 10 y 20
num = int(input("Ingresa un número: "))
if 10 <= num <= 20:
    print(f"El número {num} está entre 10 y 20.")
else:
    print(f"El número {num} no está entre 10 y 20.")

# 5. Dados tres números, encuentra el mayor usando condicionales
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print(f"El número mayor es {mayor}.")

# 6. Calcula el precio final con un 10% de descuento si el total es mayor a $100
precio = float(input("Ingresa el precio: "))
if precio > 100:
    precio_final = precio * 0.9
    print(f"El precio final con 10% de descuento es ${precio_final:.2f}.")
else:
    print(f"El precio final es ${precio:.2f}.")

# 7. Verifica si una persona puede votar (mayor o igual a 18 años)
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Puedes votar.")
else:
    print("No puedes votar.")

# 8. Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP
precio = float(input("Ingresa el precio: "))
tipo_cliente = input("Ingresa el tipo de cliente (VIP o normal): ")
if tipo_cliente.lower() == "vip":
    precio_final = precio * 0.8
    print(f"El precio final con 20% de descuento es ${precio_final:.2f}.")
else:
    print(f"El precio final es ${precio:.2f}.")

# 9. Determina si un número es múltiplo de 5 y de 3 al mismo tiempo
num = int(input("Ingresa un número: "))
if num % 5 == 0 and num % 3 == 0:
    print(f"El número {num} es múltiplo de 5 y de 3 al mismo tiempo.")
else:
    print(f"El número {num} no es múltiplo de 5 y de 3 al mismo tiempo.")

# 10. Dado un número, verifica si es divisible entre dos números dados
num = int(input("Ingresa un número: "))
div1 = int(input("Ingresa el primer divisor: "))
div2 = int(input("Ingresa el segundo divisor: "))
if num % div1 == 0 and num % div2 == 0:
    print(f"El número {num} es divisible entre {div1} y {div2}.")
else:
    print(f"El número {num} no es divisible entre {div1} y {div2}.")






