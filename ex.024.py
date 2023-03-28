opcao = 0
n1 = int(input(print('Digite um numero: ')))
n2 = int(input(print('Digite mais um numero: ')))
while opcao !=5:

    opcao = int(input(print('[ 1 ]- Somar\n[ 2 ]- Multiplicaçao\n[ 3 ]- Maior\n[ 4 ]- Novos numeros\n[ 5 ]- Sair do programa'))) # usar case mas nao sei como
    if opcao == 1:
        soma = n1+n2
        print('A soma entre {} e {} é: {}'.format(n1,n2,soma))

    elif opcao == 2:
        multiplicacao = n1*n2
        print('A maultiplicaçao entre {}  e {} é {}'.format(n1,n2,multiplicacao))

    elif opcao == 3:
        if n1 >= n2:
            maiorN =n1
        else:
            maiorN = n2
        print('O maior numero entre {} e {} é: {} '.format(n1,n2,maiorN))

    elif opcao == 4:
        n1= int(input(print('Digite um numero:')))
        n2 = int(input(print('digite um numero: ')))

    elif opcao == 5:
        print('Fim do programa')

    else:
        print('Opcao invalida')
