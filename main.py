print("Hola mundo Eva")
"""
# variables
texto= "repaso de sintaxis"
nombre = "eva"
altura= "171cm"
year= 2021

print(f"{texto}-{nombre}-{altura}-{str(year)}")

#  Entrada
nom = input("cual es tu nombre perra: ")
edad = input("tu edad es: ")

# Salida
print(f"mi nombre es: {nom} ")
print(f"mi nombre es: {int(edad)+5} ")
"""
"""year= 1995
if year != 1995:
    print("no 1995")
else:
    print("introdujiste 1995")

dia =int(input("Introduce el numero del dia: "))
if dia==1:
    print("es lunes")
elif dia ==2:
        print("es martes")
elif dia ==3:
        print("es miercoles")
else:
    print("es fin de semana")
#ejemplo

edad=int(input("introduce tu edad"))

if edad >= 18 and edad <= 65:
    print( "tienes edad para trabajar")
else:
    print("no tienes edad")"""
"""
#bucle for
for var in elemento interable (lista, rango,etc)

con=0
resul=0
for con in range (1,6):
    print("voy por el"+ str(con))
    
    resul += con
print(f"el resultado es: {resul}")"""

import random
from random import sample
ahorro = 4
for x in range(11):
    
   mano= sample(lista,k=10)
print(f"cuenta de ahorro: {mano}")
#print(f"cuenta de ahorro: {ahorro}+{list}")