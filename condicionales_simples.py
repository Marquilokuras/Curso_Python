'''
Primer ejemplo:
Crear un programa que reciba el numero de años que tiene nuestra computadora
Imprimir en consola si es nuevo o es viejo
Condiciones: Si es menor o igual a 2 años, entonces es nuevo
Pero, si es mayor a 2 años,, entonces es viejo
'''

anios = int(input("¿Cuantos años tiene tu computadora?"))

if anios >= 0 and anios <= 2:
    print("Tu computador es nuevo")
else:
    print("Tu computador es viejo")

edad = int(input("¿Cuantos años tienes?"))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

print("Hasta la proxima")