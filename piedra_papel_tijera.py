# Ejercicio del juego piedra,papel,tijera

import random

print("1 ---> papel")
print("2 ---> piedra")
print("3 ---> tijera")


maquina= random.randint(1,3)

opcion = int(input("selecione la opcion: "))

if maquina == 1 and opcion== 1:
   rta= "empate , la maquina saco papel el jugador saco papel" 

elif maquina ==2 and opcion ==2:
   rta= "empate, la maquina saco piedra el jugador saco piedra"

elif maquina ==3 and opcion ==3:
   rta= "empate, la maquina saco tijera el jugador saco tijera" 

elif maquina ==1 and opcion ==2:
   rta= "gana jugador, la maquina saco papel el jugador saco piedra"

elif maquina ==1 and opcion ==3:
   rta= "gana jugador, la maquina saco papel el jugador saco tijera"

elif maquina ==2 and opcion ==1:
   rta= "gana jugador, la maquina saco piedra el jugador saco papel"

elif maquina ==2 and opcion ==3:
   rta= "gana maquina, la maquina saco piedra el jugador saco tijera"

elif maquina ==3 and opcion ==1:
   rta= "gana maquina, la maquina saco tijera el jugador saco papel"

elif maquina ==3 and opcion ==2:
   rta= "gana jugador, la maquina saco tijera el jugador saco piedra"


else: 
   rta= "entrada invalida"

print(rta) 
