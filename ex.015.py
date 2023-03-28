import random
n1= 'Pedra'
n2= 'Papel'
n3= 'Tesoura'
pc = [n1,n2,n3]
pc = random.choice(pc)
print('Inicaiando o jogo......\nPor favor escolha uma opçao para jogar: ')
jogador= int(input(print('[1] - Pedra\n[2] - Papel\n[3] - Tesoura')))
if jogador == 1:
    jogador = n1

elif jogador ==2:
    jogador = n2

elif jogador==3:
    jogador= n3

else:
    print('Opcao invalida tente novamente')

print('O jogador escolheu {}'.format(jogador))
print('O computador escolheu {}'.format(pc))
if jogador == n1 and pc == n2 or jogador == n2 and pc == n3 or jogador == n3 and pc == n1:
    print('O computador venceu!, boa sorte na proxima')

elif jogador == n2 and pc == n1 or jogador == n3 and pc == n2 or jogador == n1 and pc == n3:
    print('Parabens voce venceu!!')

elif jogador == pc:
    print('Empate')
