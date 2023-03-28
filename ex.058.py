jogador={}
gols = []
jogador['nome'] = str(input('Informe o seu nome: '))
partidas = int(input('Quantas partidas voce jogou?: '))
for x in range(0,partidas):
    gols.append(int(input(f'Quantos gols vc marcou na partida {x}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print(jogador)
print()
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print()
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas ')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')