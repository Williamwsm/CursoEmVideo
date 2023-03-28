matriz = [[0,0,0],[0,0,0],[0,0,0]]
smTotalPares = smColuna3 = maiorValorLn2 = 0
for x in range(0,3):
    for j in range(0,3):
        matriz[x][j] = int(input('Digite um numero: '))
        if matriz[x][j] %2 ==0:
            smTotalPares += matriz[x][j]
        #A soma dos valores da coluna 3
        if matriz[x][j] == matriz[x][2]:
            smColuna3 += matriz[x][2]
        #maior valor da linha 2
        if matriz[x][j] == matriz [1][j] and matriz[1][j] > maiorValorLn2:
            maiorValorLn2 = matriz[1][j]
for x in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[x][j]}] ', end='')
    print()
print(f'A soma de todos valores pares da matrizes sao: {smTotalPares}')
print(f'A soma dos valores da coluna 3 é: {smColuna3} ')
print(f'O maior valor da linha 2 foi: {maiorValorLn2} ')