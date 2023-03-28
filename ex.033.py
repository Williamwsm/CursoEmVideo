from random import randint

vitorias =0

while True:
    n = int(input(print('Escolha um numero')))
    pc = randint(0,10)
    resultado = n + pc
    opcao = str(input(print('Par ou Impar? [P] - [I]'))).upper().strip()
    if opcao == 'P' and resultado%2 == 0 or opcao == 'I' and resultado%2 != 0:
        vitorias += 1
        print(f'O seu numero escolhido foi {n} e o numero escolhido pelo pc foi {pc}')
        print('Parabens pela sua vitoria')
    else:
        print(f'O seu numero escolhido foi {n} e o numero escolhido pelo pc foi {pc}')
        print(' Voce acabou perdendo, boa sorte na proxima ')
        break
print(f'O total de vitorias foi {vitorias}')