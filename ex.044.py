opcao = ''
listaNum = []
while True:
    n = int(input('Digite um numero: '))
    if n not in listaNum:
        listaNum.append(n)
        print('Numero cadastrado com sucesso...')
    else:
        print('Esse numero ja foi digitado... o numero nao pode ser cadastrado ')
    opcao = str(input('Deseja continuar ? [S/N] '))
    if opcao.upper() == 'N':
        break
    listaNum.sort()
print(f'Os numeros que voce digitou os numeros {listaNum}')