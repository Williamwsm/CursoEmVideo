from random import randint
megaSena = []
jogos = []
total = 1
jogadas = int(input('Informe o numero de vezes que voce deseja jogar na mega sena: '))
while total <= jogadas:
    cont = 0
    while True:
     n = randint(0, 60)+1
     if n not in megaSena:
        megaSena.append(n)
        cont += 1
     if cont >= 6:
        break
    megaSena.sort()
    jogos.append(megaSena[:])
    megaSena.clear()
    total +=1
for x, j in enumerate(jogos):
    print(f'Jogos {x+1} : {j}')