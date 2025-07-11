#---------------------------------------DESARROLLO DEL TALLER 20 PREGUNTAS------------------------------------------------
# #PRIMERA Pide tu edad y muestra si eres menor de edad, mayor de edad o adulto mayor (65+).
# dato1=input("ingresa tu nombre: ")
# d2=int(input("ingresa tu edad: "))
# if d2<=18:
#     print("eres un menor de edad")
# elif d2 >18:
#     print("eres un adulto, mayor de edad")
# else:
#     print("eres un adulto mayor")


# #SEGUNDO Solicita tu estatura en metros. Si mide menos de 1.5 m, eres considerado bajo entre 1.5 y 1.8 m, estatura media; más de 1.8 m, alto.

# d1=input("ingresa tu nombre: ")
# d2=d2=float(input("ingresa tu estatura en metros: "))
# if d2 <1.5:
#     print("eres un enano, na mentiras, eres bajito")
# elif d2 >=1.5 and d2 <1.8:
#     print("tienes una estatura media")
# else:
#     print("eres un adulto mayor")

# #TERCERO Ingresa un número y muestra si es múltiplo de 2, de 3, o de ninguno.
# numero = int(input("Ingresa un número: "))
# if numero % 2 == 0:
#     print("Es múltiplo de 2.")
# elif numero % 3 == 0:
#     print("Es múltiplo de 3.")
# else:
#     print("No es múltiplo de 2 ni de 3.")

# # CUARTO Pide un número decimal y determina si tiene 1, 2 o más de 2 decimales (usa str() y split()).
# decimal = input("Ingresa un número decimal: ")
# partes = decimal.split(".")
# if len(partes) == 1:
#     print("No tiene decimales.")
# elif len(partes[1]) == 1:
#     print("Tiene 1 decimal.")
# elif len(partes[1]) == 2:
#     print("Tiene 2 decimales.")
# else:
#     print("Tiene más de 2 decimales.")

# #QUINTO Solicita un país y muestra si está en la siguiente tupla: ("Colombia", "Perú", "Argentina", "México").
# D1=input("ingresa tu nombre pq si: ")
# P1=input("ingresa cualquier pais:")
# paises = ("Colombia", "Perú", "Argentina", "México")
# if P1 in paises:
#     print("El país está en la lista.")
# else:
#     print("El país no está en la lista.")

# #SEXTO Pide tu tipo de sangre (A, B, AB, O) y muestra tu compatibilidad según un diccionario predefinido.
# compatibilidad = {
#     'A': ['A', 'AB'],
#     'B': ['B', 'AB'],
#     'AB': ['AB'],
#     'O': ['A', 'B', 'AB', 'O']
# }
# tipo_sangre = input("Ingresa tu tipo de sangre (A, B, AB, O): ").upper()
# if tipo_sangre in compatibilidad:
#     print("Compatibilidad:", compatibilidad[tipo_sangre])
# else:
#     print("Tipo de sangre no válido.")

# # SETIMO Ingresa una temperatura en °C. Si es menor de 10, hace frío. Si está entre 10 y 25, templado. Más de 25, hace calor.
# temperatura = float(input("Ingresa una temperatura en °C: "))
# if temperatura < 10:
#     print("Hace frío.")
# elif 10 <= temperatura <= 25:
#     print("Templado.")
# else:
#     print("Hace calor.")

# OCTAVO Crea un menú con opciones 1. Sumar, 2. Restar, 3. Multiplicar. Pide dos números y ejecuta la operación seleccionada.
# print("Menú:")
# print("1. Sumar")
# print("2. Restar")
# print("3. Multiplicar")
# opcion = int(input("Selecciona una opción: "))
# num1 = int(input("Ingresa el primer número: "))
# num2 = int(input("Ingresa el segundo número: "))

# if opcion == 1:
#     print("Resultado:", num1 + num2)
# elif opcion == 2:
#     print("Resultado:", num1 - num2)
# elif opcion == 3:
#     print("Resultado:", num1 * num2)
# else:
#     print("Opción no válida.")

# # NOVENO Pide un número entre 1 y 12 y muestra el mes correspondiente usando un diccionario.
# meses = {
#     1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
#     5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
#     9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
# }
# numero_mes = int(input("Ingresa un número entre 1 y 12: "))
# if numero_mes in meses:
#     print("Mes:", meses[numero_mes])
# else:
#     print("Número no válido.")

# #DECIMO Solicita un número de 4 dígitos y determina si comienza con 1, 2 o cualquier otro.
# numero = input("Ingresa cualquier  número de 4 dígitos: ")
# if len(numero) == 4:
#     if numero.startswith('1'):
#         print("Comienza con 1.")
#     elif numero.startswith('2'):
#         print("Comienza con 2.")
#     else:
#         print("Comienza con otro número baby.")
# else:
#     print("baby, ese número no tiene 4 dígitos mor.")

# # ONCE Ingresa una palabra. Muestra si su primera letra es vocal, consonante o un número.
# palabra = input("Ingresa cualquier palabra mor, pliss: ")
# if palabra:
#     primera_letra = palabra[0]
#     if primera_letra.isdigit():
#         print("La primera letra es un número.")
#     elif primera_letra in 'aeiouAEIOU':
#         print("La primera letra es una vocal.")
#     else:
#         print("La primera letra es una consonante.")
# else:
#     print("No se ingresó ninguna palabra.")

#DOCE Pide una fruta. Si está en la lista ["manzana", "pera", "piña"], muestra su precio. Si no, indica que no está disponible.
fruta = input("Ingresa una fruta: ")
precios = {
    "manzana": 1000,
    "pera": 1500,
    "piña": 2000
}
if fruta in precios:
    print("El precio de la", fruta, "es", precios[fruta], "pesos.")
else:
    print("Fruta no disponible.")

# TRECE Pide tu calificación (0 a 5). Si es menor que 3, reprobado. Entre 3 y 4, aprobado. Mayor a 4, excelente.
# calificacion = float(input("Ingresa tu calificación (0 a 5): "))
# if calificacion < 3:
#     print("Reprobado.")
# elif 3 <= calificacion < 4:
#     print("Aprobado.")
# else:
#     print("Excelente.")

# # CATORCE Pide un número y muestra si es divisible entre 4, entre 6, o no lo es.
# numero = int(input("Ingresa un número: "))
# if numero % 4 == 0:
#     print("Es divisible entre 4.")
# elif numero % 6 == 0:
#     print("Es divisible entre 6.")
# else:
#     print("No es divisible entre 4 ni entre 6.")



#QUINCE . Crea un sistema de autenticación básico. Pide usuario y clave. Usa un diccionario para validar.
usuarioss={
    "usuario1":"clave1",
    "usuario2":"clave2"
}
usuario=input("Ingresa tu usuario: ")
clave=input("Ingresa tu clave: ")

if usuario in usuarioss and usuarioss[usuario] == clave:
    print("Acceso concedido")
else:
    print("Acceso denegado")
# 16. Grupo de edad
Nombre=input("Ingresa tu nombre baby:" ) 
edad = int(input("Ingresa tu edad: "))
if 0 <= edad <= 12:
    print("Eres un niño, que ternura ")
elif 13 <= edad <= 17:
    print("Eres un adolescente jsjs")
elif 18 <= edad <= 64:
    print("Eres mayor de edad, o sea un adulto baby")
else:
    print("Eres un adulto mayor.")

# DIECISIETE Pide el nombre de una ciudad. Si está en una tupla, muestra que es capital; si no, muestra “ciudad secundaria”.
ciudad = input("Ingresa el nombre de una ciudad: ")
capitales = ("Bogotá", "Lima", "Buenos Aires", "Ciudad de México")
if ciudad in capitales:
    print("Es una capital.")
else:
    print("Es una ciudad secundaria.")

# DIECIOCHO Ingresa el valor de una compra. Si es mayor de $200.000 aplica un 15% de descuento. Entre $100.000 y $200.000 aplica 10%. Si es menor, no hay descuento.

nombre=input("baby, primero q este proceso Ingresa tu nombre:") 
valor_compra = float(input("Ingresa el valor de la compra: "))
if valor_compra > 200000:
    descuento = valor_compra * 0.15
elif 100000 < valor_compra <= 200000:
    descuento = valor_compra * 0.10
else:
    descuento = 0

valor_final = valor_compra - descuento
print("El valor final de la compra es:", valor_final)

# DIECINUEVE Pide el nombre y el número de horas trabajadas. Calcula el salario con tarifa de $10.000/hora. Si trabajó más de 40 horas, aplica un bono del 20%.
nombre = input("Ingresa tu nombre: ")
horas_trabajadas = float(input("Ingresa el número de horas trabajadas: "))
tarifa_hora = 10000
salario = horas_trabajadas * tarifa_hora

if horas_trabajadas > 40:
    salario *= 1.2  # Aplica bono del 20%

print("El salario de", nombre, "es:", salario)

# VEINTE Ingresa tu puntaje en una prueba (0 a 100). Si es menor a 50, insuficiente. De 50 a 79, aceptable. 80 a 100, sobresaliente.
puntaje = int(input("Ingresa tu puntaje en la prueba (0 a 100): "))
if puntaje < 50:
    print("Insuficiente.")
elif 50 <= puntaje < 80:
    print("Aceptable.")
else:
    print("Sobresaliente.")