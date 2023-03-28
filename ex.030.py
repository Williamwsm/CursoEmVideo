opcao = str(input(print('Para continua digite [S]\nSe deseja encerrar digite [N]'))).upper()
maior =  media = cont = soma = 0
n = int(input(print('Informe um numero: ')))
menor = n
while opcao == 'S':
    cont += 1
    soma += n
    if maior < n:
        maior = n

    if menor > n:
        menor = n
    media = (soma/cont)
    opcao = str(input(print('Para continua digite [S]\nSe deseja encerrar digite [N]'))).upper()
    if opcao == "S":
        n = int(input(print('Informe um numero: ')))
print('A media total foi de: {:.2f}, o maior numero foi {}, o menor numero foi {} '.format(media, maior, menor))