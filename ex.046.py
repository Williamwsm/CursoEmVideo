n = []
cont = 0
while True:
    n.append( int(input('Digite um numero: ')))
    cont += 1
    opcao = str(input('Deseja continuar? [S/N] '))
    if opcao.upper() == 'N':
        break
if 5 in n:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 nao esta na lista')
n.sort(reverse= True)
print(f'Voce digitou {cont} elementos ')
print(f'Os numeros que voce desligou foram {n}')