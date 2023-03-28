pessoas = list()
dados = dict()
mulheres = list()
soma =0
while True:
    dados.clear()
    dados['nome'] = str(input('Informe o seu nome: ')).title()
    dados['sexo'] = str(input('Informe o seu sexo: [M/F] ')).upper()
    if dados['sexo'] in "F":
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Informe a sua idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    opcao = str(input('Deseja continuar? [S/N] ')).upper()
    if opcao == 'N':
        print('Finalizando...')
        break
media = float((soma / len(pessoas)))
print(f'O numero total de pessoas é:{len(pessoas)} ')
print(f'A media de idades é: {media}')
print(f'As mulheres cadastradas fora: {mulheres}')
for p in (pessoas):
    if p['idade'] >= media:
        for k, v in p.items():
            print(f' {k} = {v}: ',end=" ")