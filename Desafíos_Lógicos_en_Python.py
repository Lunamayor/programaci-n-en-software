#---------------------------------------DESARROLLO DEL TALLER 20 PREGUNTAS------------------------------------------------
#PRIMERA Pide tu edad y muestra si eres menor de edad, mayor de edad o adulto mayor (65+).
dato1=input("ingresa tu nombre: ")
d2=int(input("ingresa tu edad: "))
if d2<=18:
    print("eres un menor de edad")
elif d2 >18:
    print("eres un adulto, mayor de edad")
else:
    print("eres un adulto mayor")

#SEGUNDO Solicita tu estatura en metros. Si mide menos de 1.5 m, eres considerado bajo entre 1.5 y 1.8 m, estatura media; más de 1.8 m, alto.

d1=input("ingresa tu nombre: ")
d2=d2=float(input("ingresa tu estatura en metros: "))
if d2 <1.5:
    print("eres un enano, na mentiras, eres bajito")
elif d2 >=1.5 and d2 <1.8:
    print("tienes una estatura media")
else:
    print("eres un adulto mayor")