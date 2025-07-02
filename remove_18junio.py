# frutas=['manzana','banana','naranja','banana']

# frutas.remove("banana")
# print(frutas)
# #------------------------------------------------------------------

# frutas=['manzana', 'banana', 'naranja', 'banana']
# frutas.clear( )
# print(frutas)

# #------- ejercicioooooooooooooooooooooooooossssssssssssssssssssssssss------------------------------------------
# #append

# lista1=['3']
# ejercicio1=int(input("ingrese el primer numero: "))
# lista1.append(ejercicio1)
# print(lista1)

# lista2=["ana", "luis"]
# ejercicio2=input("ingrese el nombre: ")
# lista2.append(ejercicio2)
# print(lista2)

# #insert(i, x)
# lista3=['1','2','3']
# ejercicio3=int(input("ingrese el numero: "))
# lista3.insert(0,ejercicio3)
# print(lista3)

# lista4=["azul","verde"]
# ejercicio4=input("ingrese el color: ")
# lista4.insert(1,ejercicio4)
# print(lista4)

#extend
lista5=[4,5,6]
lista6=[1,2,3]

lista=lista5.extend(lista6)
print(lista)

lista_q_me_salte=["a","b"]
lista_q_me_salte2=("ok")
asi_queda=lista_q_me_salte.extend(lista_q_me_salte2)
print(asi_queda)

#remove(x)
frutas6=['manzana', 'uva', 'pera']

frutas6.remove('uva')
print(frutas6)

nuemero6=['1','2','3','2']

nuemero6.remove('2')
print(nuemero6)

#pop([i])

lista7=[1,2,3,4]
lista7.pop()
print(lista7)

lista8=["uno","dos","tres"]
lista8.pop(0)
print(lista8)

#clear()
lista9=[1,2,3]
lista9.clear()
print(lista9)

lista10=["negro","lila","blanco"]
lista10.clear()
print(lista10)

#index (x)
lista11=["manzana","pera","uva"]
lista11.index("pera")
print(lista11)

lista12=[4,5,6,7]
lista12.index(6)
print(lista12)

#count (x)
lista13=[3,1,3,5,3]
lista13.count(3)
print(lista13)

lista14=["a","b","a","c","a"]
lista14.count("a")
print(lista14)

#sort ()
lista15=[5,1,4,2,3]
lista15.sort()
print(lista15)

lista16=["z","a","m","b"]
lista16.sort()
print(lista16)

#reverse ()
lista17=[1,2,3,4,5]
lista17.reverse()
print(lista17)

lista18=["inicio","medio","fin"]
lista18.reverse()
print(lista18)

#copy ()
lista19=[1,2,3]
nueva=lista19.copy()
print(lista19)

lista20=["a","b","c"]
nueva=lista20.copy
print(lista20)


#####----------------------------ACTIVIDAD  DE  LISTAS---------------------------------------------------------------

LISTA1=["hello","que tal","adioss"]
LISTA1.append(int(100))
LISTA1.append("hola mundo")
print(LISTA1)


LISTA2=["hola y adios","HOLA","bay"]
LISTA2.append(300)
print(LISTA2)

LISTA3 = LISTA1.copy()
print(LISTA3)


LISTA4 = LISTA2.copy()
print(LISTA4)

LISTA5= [LISTA4, LISTA3]
print(LISTA5)





