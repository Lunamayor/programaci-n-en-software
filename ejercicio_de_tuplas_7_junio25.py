#--------------ejercicios practicos de tuplas, 25 de junio------------------------------------------------
mi_tupla1=("1","2","3","4","5")
print(mi_tupla1)

print(mi_tupla1[1])

longitud=len(mi_tupla1)
print(longitud)
print(len(mi_tupla1))


posicion=mi_tupla1.index("4")
print(posicion)

veces=mi_tupla1.count("2")
print(veces)

mi_tupla2=("hola como estas","6","4.3")
print(mi_tupla2)

mi_tupla3=(mi_tupla1,mi_tupla2,(1,3,4,5,6,7))

mi_lista=list(mi_tupla3)
mi_listaa=int(input(3))
mi_lista.append(mi_listaa)

print(mi_listaa[0][3])

print(f"el valor al acceder el primer valor de la tupla externa es {mi_listaa [0][3]}")