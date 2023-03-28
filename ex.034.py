contHomens = contMaiorIdade = contFMenor = 0
while True:
    sexo = str(input(print('Informe o seu sexo: [M/F] '))).strip().upper()
    idade = int(input(print('Informe a sua idade: ')))
    if idade > 18:
        contMaiorIdade+=1
    if sexo == 'M':
        contHomens+=1
    if sexo== 'F' and idade <20:
        contFMenor+=1
    opcao= str(input(print('deseja continuar? [S/N]'))).upper()
    if opcao == 'N':
        break
print(f'O numero de mulheres com menos de 20 anos foi {contFMenor} mulheres\nO numero de pessoas  maiores de 18 anos foi {contMaiorIdade} pessoas')
print(f'O numero de homens cadastrado foi {contHomens}')