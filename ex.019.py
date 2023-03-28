import datetime
anoAtual = datetime.date.today().year
contMaiorIdade = 0
contMenorIdade = 0
for x in range (0,7):
  anoNasci = int(input(print('Digite seu ano de nascimento')))
  if anoAtual - anoNasci < 21:
      contMenorIdade += 1
  else:
      contMaiorIdade +=1
print("O numero total de pessoas que atingiram a maior idade é de {}".format(contMaiorIdade))
print("O numero total de pessoas que estam na menor idade é de {}".format(contMenorIdade))