import numpy as np
import random

def generar_barcos():
    barcos_player = [("HM Enterprise", 4), ("Santa María", 3), ("HMS Beagle", 3), ("USS Maine", 2),
    ("Santa Clara", 2), ("HMS Suitana", 2), ("Aguila", 1), ("Astrea", 1), ("Perla", 1),
    ("HMS Fortune", 1)]

    barcos_ia = [("Bismarck", 4), ("HMS Odin", 3), ("Queen Anne's Revenge", 3), ("Helen O' Troy", 2),
    ("HMS Diamond", 2), ("Justiniane", 2), ("Acheron", 1), ("Ventura", 1), ("Flecha", 1),
    ("Hades", 1)]

    return barcos_player, barcos_ia

def coloca_barco(tablero, tamano_barco):
    pos_inicial = [np.random.randint(0,10), np.random.randint(0,10)]
    orientacion = random.choice(["N","E","S","O"])
    if orientacion == "N":
        pos_final = [pos_inicial[0]-tamano_barco, pos_inicial[1]]
        if pos_final[0] < 0 or np.any(tablero[pos_inicial[0]:pos_final[0]-1:-1, pos_inicial[1]:pos_inicial[1]] != " "):
            return coloca_barco(tablero, tamano_barco)
        else:
            tablero[pos_inicial[0]:pos_final[0]:-1, pos_inicial[1]] = "O"
            coordenadas = []
            for i in range(pos_inicial[0], pos_final[0], -1):
                coordenadas.append([i, pos_final[1]])
            return tablero, coordenadas
    elif orientacion == "E":
        pos_final = [pos_inicial[0], pos_inicial[1]+tamano_barco]
        if pos_final[1] > 9 or np.any(tablero[pos_inicial[0]:pos_inicial[0], pos_inicial[1]:pos_final[1]+1] != " "):
            return coloca_barco(tablero, tamano_barco)
        else:
            tablero[pos_inicial[0], pos_inicial[1]:pos_final[1]] = "O"
            coordenadas = []
            for i in range(pos_inicial[1], pos_final[1]):
                coordenadas.append([pos_inicial[0], i])
            return tablero, coordenadas
    elif orientacion == "S":
        pos_final = [pos_inicial[0]+tamano_barco, pos_inicial[1]]
        if pos_final[0] > 9 or np.any(tablero[pos_inicial[0]:pos_final[0]+1, pos_inicial[1]:pos_inicial[1]] != " "):
            return coloca_barco(tablero, tamano_barco)
        else:
            tablero[pos_inicial[0]:pos_final[0], pos_inicial[1]] = "O"
            coordenadas = []
            for i in range(pos_inicial[0], pos_final[0]):
                coordenadas.append([i, pos_inicial[1]])
            return tablero, coordenadas
    elif orientacion == "O":
        pos_final = [pos_inicial[0], pos_inicial[1]-tamano_barco]
        if pos_final[1] < 0 or np.any(tablero[pos_inicial[0]:pos_inicial[0], pos_inicial[1]:pos_final[1]-1:-1] != " "):
            return coloca_barco(tablero, tamano_barco)
        else:
            tablero[pos_inicial[0], pos_inicial[1]:pos_final[1]:-1] = "O"
            coordenadas = []
            for i in range(pos_inicial[1], pos_final[1],-1):
                coordenadas.append([pos_inicial[0], i])
            return tablero, coordenadas

def disparo_player(tablero_ia, tab_player_riv, barcos_ia):
    if not "O" in tablero_ia:
        return tablero_ia, tab_player_riv, barcos_ia
    try:
        shoot = [int(input("Indica la fila de disparo: "))-1, int(input("Indica la columna de disparo: "))-1]

        if tablero_ia[shoot[0], shoot[1]] == " ":
            tablero_ia[shoot[0], shoot[1]], tab_player_riv[shoot[0], shoot[1]] = "-", "-"
            return tablero_ia, tab_player_riv, barcos_ia
        
        elif tablero_ia[shoot[0], shoot[1]] == "O":
            tablero_ia[shoot[0], shoot[1]], tab_player_riv[shoot[0], shoot[1]] = "X", "X"
            for barco in barcos_ia:
                if shoot in barco.ubicacion:
                    barco.ubicacion.remove(shoot)
                    print("El barco", barco.nombre, "ha sido tocado")
                    if len(barco.ubicacion) == 0:
                        print("El barco", barco.nombre, "ha sido hundido")
                    break
            print(tab_player_riv)
            return disparo_player(tablero_ia, tab_player_riv, barcos_ia)
        
        else:
            print("Ya has disparado en esa ubicación")
            return disparo_player(tablero_ia, tab_player_riv, barcos_ia)
    
    except:
        print("Esas coordenadas no son correctas, vuelve a intentarlo")
        return disparo_player(tablero_ia, tab_player_riv, barcos_ia)

def disparo_ia(tab_player, tab_ia_riv, barcos_player):
    if not "O" in tab_player:
        return tab_player, tab_ia_riv, barcos_player
    shoot = [np.random.randint(0,10), np.random.randint(0,10)]
    if tab_player[shoot[0], shoot[1]] == " ":
        tab_player[shoot[0], shoot[1]], tab_ia_riv[shoot[0], shoot[1]] = "-", "-"
        return tab_player, tab_ia_riv, barcos_player
    
    elif tab_player[shoot[0], shoot[1]] == "O":
        tab_player[shoot[0], shoot[1]], tab_ia_riv[shoot[0], shoot[1]] = "X", "X"
        for barco in barcos_player:
            if shoot in barco.ubicacion:
                barco.ubicacion.remove(shoot)
                print("El barco", barco.nombre, "ha sido tocado")
                if len(barco.ubicacion) == 0:
                    print("El barco", barco.nombre, "ha sido hundido")
                break
        return disparo_ia(tab_player, tab_ia_riv, barcos_player)
    
    else:
        return disparo_ia(tab_player, tab_ia_riv, barcos_player)