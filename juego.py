#Juego Tic Tac Toe
#Autora: Carla Gonzalez Mina

import random

def dibujarTablero(tablero):
    #imprimo el tablero que se le pasa. "tablero" es una lista de 10 cadenas representando el tablero
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   |')

def eligeLetraJugador():
    #jugador elegir su letra
    #devuelvo una lista con la letra del jugador como primer elemento y la letra de la computadora como segundo
    letra = ""
    while not (letra == "X" or letra == "O"):
        print("¿Quieres ser X o O?")
        letra = input().upper()
    #primera letra en la lista es la del jugador, la segunda es la de la computadora
    if letra == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

def quienComienza():
    # azar que jugador comienza
    if random.randint(0, 1) == 0:
        return "computadora"
    else:
        return "jugador"
    
def jugarDeNuevo():
    #devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra
    def esGanador(ta, le):
        #un tablero y la letra de un jugador, esta funcion devuelve True si ese jugador ha ganado
        return ((ta[7] == le and ta[8] == le and ta[9] == le) or  # fila superior
                (ta[4] == le and ta[5] == le and ta[6] == le) or  # fila del medio
                (ta[1] == le and ta[2] == le and ta[3] == le) or  # fila inferior
                (ta[7] == le and ta[4] == le and ta[1] == le) or  # columna izquierda
                (ta[8] == le and ta[5] == le and ta[2] == le) or  # columna del medio
                (ta[9] == le and ta[6] == le and ta[3] == le) or  # columna derecha
                (ta[7] == le and ta[5] == le and ta[3] == le) or  # diagonal
                (ta[9] == le and ta[5] == le and ta[1] == le))    # diagonal

    #verifiico si la jugada actual hace que el jugador gane
    if esGanador(tablero, letra):
        return True
    else:
        return False

def obtenerCopiaTablero(tablero):
    #hace una copia del tablero y la devuelve
    copiaTablero = []
    for i in tablero:
        copiaTablero.append(i)
    return copiaTablero

def hayEspacioLibre(tablero, jugada):
    #devuelve True si la jugada esta libre en el tablero
    return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero):
    #permite al jugador escribir su jugada
    jugada = ' '
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('¿Cuál es tu próxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elegirJugada(tablero, listaJugadas):
    #devuelve una jugada valida de la lista de jugadas dada en el tablero
    #devuelve None si no hay jugadas validas
    jugadaPosibles = []
    for i in listaJugadas:
        if hayEspacioLibre(tablero, i):
            jugadaPosibles.append(i)

    if len(jugadaPosibles) != 0:
        return random.choice(jugadaPosibles)
    else:
        return None
    
def obtenerJugadaComputadora(tablero, letraComputadora):
    #dado un tablero y la letra de la computadora, determina donde jugar y devuelve esa jugada
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'

    #algoritmo para la computadora
    #primero, verifica si puede ganar en la siguiente jugada
    for i in range(1, 10):
        copia = obtenerCopiaTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)
            if hacerJugada(copia, letraComputadora, i):
                return i

    #verifica si el jugador puede ganar en la siguiente jugada y lo bloquea
    for i in range(1, 10):
        copia = obtenerCopiaTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraJugador, i)
            if hacerJugada(copia, letraJugador, i):
                return i

    #intenta ocupar una de las esquinas si esta libre
    jugada = elegirJugada(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada

    #intenta ocupar el centro si esta libre
    if hayEspacioLibre(tablero, 5):
        return 5

    #intenta ocupar uno de los lados
    return elegirJugada(tablero, [2, 4, 6, 8])

def tableroCompleto(tablero):
    #devuelve True si cada espacio del tablero esta ocupado, de lo contrario devuelve False
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True

print('¡Bienvenido al juego de Carla!')
while True:
    #reseteo el tablero
    elTablero = [' '] * 10
    letraJugador, letraComputadora = eligeLetraJugador()
    turno = quienComienza()
    print('El ' + turno + ' irá primero.')
    juegoEnCurso = True

    while juegoEnCurso:
        if turno == 'jugador':
            #turno del jugador
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)

            if hacerJugada(elTablero, letraJugador, jugada):
                dibujarTablero(elTablero)
                print('¡Felicidades! ¡Has ganado!')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'computadora'

        else:
            #turno de la computadora
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            hacerJugada(elTablero, letraComputadora, jugada)

            if hacerJugada(elTablero, letraComputadora, jugada):
                dibujarTablero(elTablero)
                print('¡La computadora te ha vencido! ¡Perdiste!')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'jugador'

    if not jugarDeNuevo():
        break

if __name__ == "__main__":
    pass