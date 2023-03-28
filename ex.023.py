from random import randint
contTentativas = 0
jogador = 100
numero = randint(0,10)
print('Iniciando o jogo.... ')
while numero != jogador:
    jogador = int(input(print('Descobra o numero escolhido de 1 a 10 ')))
    contTentativas += 1

    if jogador == numero:
        print('Parabens voce conseguiu em {}, tentativas'.format(contTentativas))
    elif jogador < numero:
        print('Mais....')
    else:
        print('Menos...')