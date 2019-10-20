
import random
import time
import numpy as np
import os

l_len = 15
c_len = l_len * 3
maze = [['' for x in range(c_len+2)] for y in range(l_len+2)]
FIRST_PASS = 'º'



def imprima(timer):
    for row in maze:
        print(''.join([str(ele) for ele in row]))
    time.sleep(timer)
    # print('\n' * 2)
    os.system('clear')


def geraLabirinto():
    # Preparação para modelagem do labirinto
    for c in range(0, c_len):
        for l in range(0, l_len):
            if c % 2 != 0 and l % 2 != 0 : maze[l][c] = '*'
            else : maze[l][c] = '@'
    maze[1][1] = 'p'
    l = c = 1
    # "Escavação" do labirinto
    while True:
        way = '*'
        rastro = FIRST_PASS
        betweenWay = '@'
        side = [0] * 8
        seq = [0, 0, -2, 2]
        # Checagem de possibilidades de caminhos
        for i in range(2):
            for mv in range(4):
                if maze[l + seq[mv]][c + seq[3 - mv]] == way and maze[l + round(seq[mv] / 2)][ c + round(seq[3 - mv] / 2)] == betweenWay:
                    side[mv] = seq[mv]
                    side[7 - mv] = seq[3 - mv]
            if side.count(0) == 8:
                way = betweenWay = FIRST_PASS
                rastro = ' '
            else:
                break
        # Se não há mais possibilidades de caminho ->
        if side.count(0) == 8:
            maze[l][c] = ' '
            break  # -> Finaliza-se o processo
        while True:
            choic = random.randint(0, 3)  # Escolha aleatória dos caminhos posiveis em linha ou coluna a tomar
            if (abs(side[choic]) + abs(side[7 - choic])) > 0:
                maze[l + side[choic]][c + side[7 - choic]] = 'p'  # local destino recebe 'p'
                maze[l + round(side[choic] / 2)][c + round(side[7 - choic] / 2)] = rastro
                break
        maze[l][c] = rastro
        l += side[choic]
        c += side[7 - choic]
        imprima(0.04)


def movimenta():
    mud = np.array([[0 for x in range(c_len + 2)] for y in range(l_len + 2)])
    maze[1][1] = 'p' # ponto de saída
    for x in range(l_len):
        for y in range(c_len):
            if maze[x][y] == ' ' : mud[x][y] = 0  # caminho recebe 0
            elif maze[x][y] == 'p' : mud[x][y] = 1
            else : mud[x][y] = 3  # parede recebe 3
    maze[l_len - 2][c_len - 2] = '#'
    l = c = 1
    sequence = [0, 0, -1, 1]
    while maze[l_len - 2][c_len - 2] != 'p':  # ponto de chegada
        maze[l][c] = ' '
        move_l = move_c = 0
        lessPosition = mud[l][c]
        for rang in range(0, 4):
            if mud[l + sequence[rang]][c + sequence[3 - rang]] < lessPosition:  # Se mud menor que menor valor, será guardado essa escolha para ->
                lessPosition = mud[l + sequence[rang]][c + sequence[3 - rang]]
                move_l = sequence[rang]
                move_c = sequence[3 - rang]
        maze[l + move_l][c + move_c] = 'p'  # -> assim que feito todas as verificações, movimentar 'p'
        mud[l + move_l][c + move_c] = mud[l][c] + 1
        c += move_c
        l += move_l
        mud = np.where(mud >  mud[l][c], mud[l][c] + 3, mud)  # atualização do valor das paredes
        imprima(0.08)


while True:
    geraLabirinto()
    movimenta()
