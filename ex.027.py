primeiro = int(input(print('Informe o Termo')))
razao = int(input(print('Informe a razao')))
cont = 0
extra = 1
termo =0
while cont < 10:
    termo = primeiro
    primeiro += razao
    cont+= 1
    print('{} → '.format(termo), end='')
print('PAUSA')

while extra != 0:
    extra = int(input(print(' Deseja adcionar mais quantos termos? ')))
    for c in range(extra, 0, -1):
        termo+=razao
        cont+=1
        print('{} → '.format(termo), end='')
    print('PAUSA')
print('A progressao finalizada do termo foi de: {} vezes '.format(cont))