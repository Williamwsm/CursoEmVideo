from random import randint
from time import sleep
from  operator import itemgetter
maiorValor = 0
jogador ={'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
ranking = list()
print('VALORES SORTEADOS')
for k, v in jogador.items():
    print(f'{k} tirou {v} no dado ')
    sleep(0.5)
print('RANKING DOS JOGADORES')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i , v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(0.5)