time = []
jogador={}
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Informe o seu nome: '))
    partidas = int(input('Quantas partidas voce jogou?: '))
    gols.clear()
    for x in range(0,partidas):
        gols.append(int(input(f'Quantos gols vc marcou na partida {x}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    opcao = str(input('Deseja continuar? [S/N]')).upper()
    if opcao == "N":
        break
print()
print('Cod ',end='')
for i in jogador.keys():
    print(f'{i:<15} ',end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str (d):<15} ', end='')
    print()
while True:
    busca = int(input('Qual o ID do jogador que voce deseja encontrar? (999 para parar)'))
    if busca == 999:
        break
    if busca>= len(time):
        print(f'Erro nao existe nenhum jogador com o ID {busca} ')
    else:
        print(f'Lwvantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i} fez {g} gols')