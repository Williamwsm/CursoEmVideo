aluno = {}
aluno['nome'] = str(input('Informe o seu nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno ['media'] < 7:
    aluno['situacao'] = str('Reprovado! ')
else:
    aluno['situacao'] = str('Aprovado! ')
for k, v in aluno.items():
    print(f'{k} é igual a {v}')