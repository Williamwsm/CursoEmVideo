dados = []
while True:
    nome = str(input('Informe o seu nome: '))
    nota1 = float(input('Informe a sua primeira nota: '))
    nota2= float (input('Informe a sua segunda nota:'))
    media = (nota2 + nota1)/2
    dados.append([nome, [nota1, nota2], media])
    opcao = str(input('Deseja continuar ? [S/N]')).upper()
    if opcao == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for x , j in enumerate(dados):
    print(f'{x:<4}{j[0]:<10}{j[2]:>8.1f}')
    while True:
        resp = int(input('Mostrar as notas de qual aluno? [digite 999 para encerrar]'))
        if resp == 999:
            print('Finalizando...')
            break
        if resp <= len(dados)-1:
            print(f'Notas de {dados[resp][0]} sao {dados[resp][1]}')
