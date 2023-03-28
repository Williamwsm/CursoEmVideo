numeroEscolhido = ['zero','um','dois', 'tres','quatro','cinco','seis', 'sete','oito', 'nove','dez', 'onze', 'doze' ,'treze', 'catoze', 'quinze'
                   , 'dezesseis', ' dezessete', ' dezoito', 'dezenove', 'vinte']
while True:
    n = int(input(print('Digite um numero entre 0 a 20')))
    if n < 0 or n >20:
        print('Tente novamente')
    else:
        print(f'O numero que voce digitou foi {numeroEscolhido[n]}')
        break