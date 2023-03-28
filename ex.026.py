primeiro = int(input (print('Informe o primeiro termo')))
razao = int(input(print('Informe a razao')))
cont = 0
while cont < 10:
     termo = primeiro
     primeiro += razao
     cont += 1
     print('{} → '.format(termo), end='')
print('Fim')