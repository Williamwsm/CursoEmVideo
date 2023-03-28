maiorIdade = 0
pMaisVelha = ''
contTotal = 0
contF = 0
somaIdade = 0
for x in range(0, 4):
    nome = str(input(print('Informe o seu nome:'))).strip().title()
    idade = int(input(print('Informe a sua idade: ')))
    contTotal += 1
    somaIdade += idade
    sexo = str(input(print('Informe o seu sexo: [M] ou [F] '))).upper().strip()
    if x == 0:
        maiorIdade = idade
    if idade >= maiorIdade and sexo == 'M':
        pMaisVelha = nome

    if sexo == 'F' and idade < 20:
        contF += 1
media = somaIdade / contTotal
print('O homem mais velho foi: {}\nO numero de mulheres que tinha menos de 20 anos era: {}'.format(pMaisVelha, contF))
print('A idade media dessas pessoas é de: {} '.format(media))