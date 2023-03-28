salario = float(input(print('Informe o seu salario: ')))
valorCasa= float(input(print('Informe o valor da casa: ')))
tempoPagamento = float(input(print('Informe o tempo que pretende pagar o imovel: ')))
prestacaoMensal = valorCasa/(tempoPagamento*12)
if prestacaoMensal > (salario*30)/100:
    print('Emprestimo negado!')
else:
    print('Emprestimo concedido!')