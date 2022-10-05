import numpy as np
import funciones as fn
import clases as cl

print("Bienvenido a Battleship")

tab_player = cl.tablero("tab_player")
tab_player_riv = cl.tablero("tab_player_riv")
tab_ia = cl.tablero("tab_ia")
tab_ia_riv = cl.tablero("tab_ia_riv")
barcos = fn.generar_barcos()
barcos_player = [cl.navio(barco[0], barco[1]) for barco in barcos[0]]
barcos_ia = [cl.navio(barco[0], barco[1]) for barco in barcos[1]]

for barco in barcos_player:
    colocacion_barco = fn.coloca_barco(tab_player.forma, barco.tamano)
    tab_player.forma = colocacion_barco[0]
    barco.ubicacion = colocacion_barco[1]
    tab_player.barcos += 1

for barco in barcos_ia:
    colocacion_barco = fn.coloca_barco(tab_ia.forma, barco.tamano)
    tab_ia.forma = colocacion_barco[0]
    barco.ubicacion = colocacion_barco[1]
    tab_ia.barcos += 1

while True:
    print(tab_player.forma)
    print()
    print(tab_player_riv.forma)
    if not "O" in tab_player.forma:
        ganador = "Gana la máquina, más suerte la próxima vez"
        break
    
    if not "O" in tab_ia.forma:
        ganador = "Gana el jugador, enhorabuena"
        break

    resultado_disp = fn.disparo_player(tab_ia.forma, tab_player_riv.forma, barcos_ia)
    tab_ia.forma = resultado_disp[0]
    tab_player_riv.forma = resultado_disp[1]
    barcos_ia = resultado_disp[2]

    resultado_disp = fn.disparo_ia(tab_player.forma, tab_ia_riv.forma, barcos_player)
    tab_player.forma = resultado_disp[0]
    tab_ia_riv.forma = resultado_disp[1]
    barcos_player = resultado_disp[2]

print(ganador)