from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome:'))
anoNasc = int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('Carteira de trabalho: (0 caso nao tenha)'))
trabalhador['idade'] = datetime.now().year - anoNasc
if trabalhador['ctps'] != 0:
    trabalhador['anoContrato'] = int(input('Ano de contrato: '))
    trabalhador['salario'] = float(input('Salario: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + (trabalhador['anoContrato']+35 - datetime.now().year)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')