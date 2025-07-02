# #---------------------------------desarrollo del taller------------------------------------------------------------------
# #PRIMER EJERCICIO
# califiacion1=float(input("ingresa la primera calificacion: "))
# califiacion2=float(input("ingresa la segunda calificacion: "))
# califiacion3=float(input("ingresa la tercera calificacion: "))
# suma=(califiacion1+califiacion2+califiacion3)/3
# print(f"el promedio del usuario es {suma}")


# #SEGUNDO EJERCICIO
# PRECIOS = {
#     "producto1" : "1.500",
#     "producto2" : "2.600",
#     "producto3" : "500"
# }
# print(PRECIOS)

# porcentaje_de_aumento=float(input("ingresa el aumento de porcentaje para los productos: "))
# PRECIOS["producto1"]*(porcentaje_de_aumento/100)
# PRECIOS["producto2"]+=PRECIOS["producto2"]*(porcentaje_de_aumento/100)
# PRECIOS["producto3"]+=PRECIOS["producto3"]*(porcentaje_de_aumento/100)


# print(F"el nuevo precio de los productos seria {PRECIOS}")


# #TERCER EJERICIO
# mi_tupla=(20,10,30)



# c1=float(input("dame la primera temperatura: "))
# c2=float(input("dame la segunda temperatura: "))
# c3= float(input("dame la tercera temperatura: "))
# c4=float(input("dame la cuarta temperatura: "))
# c5=float(input("dame la quinta temperatura: "))

# f1=c1*9/5+32
# f2=c2*9/5+32
# f3=c3*9/5+32
# f4=c4*9/5+32
# f5=c5*9/5+32

# Fahrenheit=(f1,f2,f3,f4,f5)
# print(mi_tupla)
# print(Fahrenheit)

# #CUARTO EJERCICIO

# E1 = int(input("Ingresa la primera edad: "))
# E2 = int(input("Ingresa la segunda edad: "))
# E3 = int(input("Ingresa la tercera edad: "))
# E4 = int(input("Ingresa la cuarta edad: "))
# E5 = int(input("Ingresa la quinta edad: "))

# edades = [E1, E2, E3, E4, E5]

# promedio = sum(edades) / len(edades)

# edad_mayor = max(edades)
# edad_menor = min(edades)

# print(f"Promedio de edades: {promedio}")
# print(f"Mayor: {edad_mayor}, Menor: {edad_menor}")

# #QUINTO EJERCICIO
frutas = {
    "pera": 4.800,
    "manzana": 5.000,
    "durazno": 6.000
}

print("Precios por kilo:")
print(frutas)

cantidad_pera = float(input("Cantidad de peras en kilos: "))
cantidad_manzana = float(input("Cantidad de manzanas en kilos: "))
cantidad_durazno = float(input("Cantidad de duraznos en kilos: "))

total_pera = frutas["pera"] * cantidad_pera
total_manzana = frutas["manzana"] * cantidad_manzana
total_durazno = frutas["durazno"] * cantidad_durazno

total_a_pagar = total_pera + total_manzana + total_durazno

print(f"Total a pagar  peras: {total_pera}")
print(f"Total a pagar  manzanas: {total_manzana}")
print(f"Total a pagar  duraznos: {total_durazno}")
print(f"Total a pagar: ${total_a_pagar}")

# #SEXTO EJERCICIO
mi_tupla = (
    int(input("Ingresa el primer número: ")),
    int(input("Ingresa el segundo número: ")),
    int(input("Ingresa el tercer número: ")),
    int(input("Ingresa el cuarto número: ")),
    int(input("Ingresa el quinto número: "))
)

suma_total = sum(mi_tupla)

print(f"La tupla es: {mi_tupla}")
print(f"La suma total es: {suma_total}")

#SEPTIMO EJERCICIO

inventario = [
    {"nombre": input("Ingresa el nombre del producto 1: "), "cantidad": int(input("Ingresa la cantidad del producto 1: ")), "precio": float(input("Ingresa el precio del producto 1: "))},
    {"nombre": input("Ingresa el nombre del producto 2: "), "cantidad": int(input("Ingresa la cantidad del producto 2: ")), "precio": float(input("Ingresa el precio del producto 2: "))},
    {"nombre": input("Ingresa el nombre del producto 3: "), "cantidad": int(input("Ingresa la cantidad del producto 3: ")), "precio": float(input("Ingresa el precio del producto 3: "))}
]

total_inventario = inventario[0]["cantidad"] * inventario[0]["precio"] + inventario[1]["cantidad"] * inventario[1]["precio"] + inventario[2]["cantidad"] * inventario[2]["precio"]

print("Inventario:")
print(inventario)
print(f"Total del inventario: {total_inventario}")

# #OCTAVO EJERCICIO

precios = [float(input("Ingresa el precio 1: ")), float(input("Ingresa el precio 2: ")), float(input("Ingresa el precio 3: ")), float(input("Ingresa el precio 4: ")), float(input("Ingresa el precio 5: "))]
descuento = float(input("Ingresa el descuento en porcentaje: "))

precios_con_descuento = [precios[0] * (1 - descuento / 100), precios[1] * (1 - descuento / 100), precios[2] * (1 - descuento / 100), precios[3] * (1 - descuento / 100), precios[4] * (1 - descuento / 100)]

print("Precios originales:")
print(precios)
print("Precios con descuento:")
print(precios_con_descuento)

# #EJERCICIO NOVENO

notas = (float(input("Ingresa la primera nota: ")), float(input("Ingresa la segunda nota: ")), float(input("Ingresa la tercera nota: ")), float(input("Ingresa la cuarta nota: ")))

nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

print(f"Nota más alta: {nota_mas_alta}")
print(f"Nota más baja: {nota_mas_baja}")

#DECIMO EJERCICIO 

conversiones = {"km": 1000, "m": 1, "cm": 0.01}

unidad = input("Ingresa la unidad (km, m, cm): ")
cantidad = float(input("Ingresa la cantidad: "))

metros = cantidad * conversiones[unidad]

print(f"{cantidad} {unidad} son {metros} metros")

#EJERCICIO ONCE

precios = [float(input("Ingresa el precio 1: ")), float(input("Ingresa el precio 2: ")), float(input("Ingresa el precio 3: ")), float(input("Ingresa el precio 4: ")), float(input("Ingresa el precio 5: "))]

precios_con_iva = [precios[0] * 1.19, precios[1] * 1.19, precios[2] * 1.19, precios[3] * 1.19, precios[4] * 1.19]

print("Precios sin IVA:")
print(precios)
print("Precios con IVA:")
print(precios_con_iva)

# #EJRCICIO DOCE

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

operaciones = (num1 + num2, num1 - num2, num1 * num2, num1 / num2)

print("Operaciones:")
print(f"Suma: {operaciones[0]}")
print(f"Resta: {operaciones[1]}")
print(f"Multiplicación: {operaciones[2]}")
print(f"División: {operaciones[3]}")

#EJERCICIO TRECE
nota1 = float(input("Ingresa la nota del estudiante 1: "))
nota2 = float(input("Ingresa la nota del estudiante 2: "))
nota3 = float(input("Ingresa la nota del estudiante 3: "))

promedio = (nota1 + nota2 + nota3) / 3

# print(f"Promedio general: {promedio}")

#EJERCICIO CATORCE 
salarios = [float(input("Ingresa el salario 1: ")), float(input("Ingresa el salario 2: ")), float(input("Ingresa el salario 3: ")), float(input("Ingresa el salario 4: ")), float(input("Ingresa el salario 5: "))]
salarios_con_aumento = [salarios[0] * 1.10, salarios[1] * 1.10, salarios[2] * 1.10, salarios[3] * 1.10, salarios[4] * 1.10]

print("Salarios originales:")
print(salarios)
print("Salarios con aumento:")
print(salarios_con_aumento)

#EJERCICIO QUINCE

productos = {"Producto 1": float(input("Ingresa el precio del producto 1: ")),
              "Producto 2": float(input("Ingresa el precio del producto 2: ")), 
              "Producto 3": float(input("Ingresa el precio del producto 3: "))
              }


impuesto = float(input("Ingresa el porcentaje de impuesto: "))

precio_final1 = productos["Producto 1"] * (1 + impuesto / 100)
precio_final2 = productos["Producto 2"] * (1 + impuesto / 100)
precio_final3 = productos["Producto 3"] * (1 + impuesto / 100)

print(f"Precio final del producto 1: {precio_final1}")
print(f"Precio final del producto 2: {precio_final2}")
print(f"Precio final del producto 3: {precio_final3}")

#EJERCICIO DIESISEIS

edad1 = int(input("Ingresa la edad 1: "))
edad2 = int(input("Ingresa la edad 2: "))
edad3 = int(input("Ingresa la edad 3: "))
edad4 = int(input("Ingresa la edad 4: "))
edad5 = int(input("Ingresa la edad 5: "))

mayores = (edad1 >= 18) + (edad2 >= 18) + (edad3 >= 18) + (edad4 >= 18) + (edad5 >= 18)
menores = 5 - mayores

print(f"Mayores de edad: {mayores}")
print(f"Menores de edad: {menores}")

#EJERCICIO DIESISIETE

cantidad_dolares = float(input("Ingresa la cantidad en dólares: "))
tasa_euro = 0.88
euros = cantidad_dolares * tasa_euro

tasa_peso = 3800
pesos = cantidad_dolares * tasa_peso

tasa_yen = 110
yenes = cantidad_dolares * tasa_yen

print(f"{cantidad_dolares} dólares son {euros} euros")
print(f"{cantidad_dolares} dólares son {pesos} pesos")
print(f"{cantidad_dolares} dólares son {yenes} yenes")



#EJERCICIO DIESIOCHO

venta1 = int(input("Ingresa la cantidad vendida del producto 1: "))
venta2 = int(input("Ingresa la cantidad vendida del producto 2: "))
venta3 = int(input("Ingresa la cantidad vendida del producto 3: "))

total_unidades = venta1 + venta2 + venta3

print(f"Total de unidades vendidas: {total_unidades}")

#EJERCICIO DIESINUEVE

temp1 = float(input("Ingresa la temperatura 1: "))
temp2 = float(input("Ingresa la temperatura 2: "))
temp3 = float(input("Ingresa la temperatura 3: "))
temp4 = float(input("Ingresa la temperatura 4: "))
temp5 = float(input("Ingresa la temperatura 5: "))
temp6 = float(input("Ingresa la temperatura 6: "))
temp7 = float(input("Ingresa la temperatura 7: "))
temp8 = float(input("Ingresa la temperatura 8: "))
temp9 = float(input("Ingresa la temperatura 9: "))
temp10 = float(input("Ingresa la temperatura 10: "))

superiores_30 = (temp1 > 30) + (temp2 > 30) + (temp3 > 30) + (temp4 > 30) + (temp5 > 30) + (temp6 > 30) + (temp7 > 30) + (temp8 > 30) + (temp9 > 30) + (temp10 > 30)
inferiores_10 = (temp1 < 10) + (temp2 < 10) + (temp3 < 10) + (temp4 < 10) + (temp5 < 10) + (temp6 < 10) + (temp7 < 10) + (temp8 < 10) + (temp9 < 10) + (temp10 < 10)

print(f"Temperaturas superiores a 30: {superiores_30}")
print(f"Temperaturas inferiores a 10: {inferiores_10}")


#EJERCICIO VEINTE

precios = [float(input("Ingresa el precio 1: ")), float(input("Ingresa el precio 2: ")), float(input("Ingresa el precio 3: ")), float(input("Ingresa el precio 4: ")), float(input("Ingresa el precio 5: "))]
eliminar = int(input("Ingresa el índice del precio a eliminar (0-4): "))
precios.pop(eliminar)
nuevo_precio = float(input("Ingresa el nuevo precio: "))
precios.append(nuevo_precio)
precios.sort()

print(f"el acual precio seria {precios}")


