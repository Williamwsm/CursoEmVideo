
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for x in range(0, 3):
    for j in range(0, 3):
        matriz[x][j] = (int(input(f'Digite um numero para a posicao [{x}, {j}]: ')))

for x in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[x][j]}] ', end='')
    print()
