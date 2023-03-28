import math
cttOp = float(input(print('Informe o tamanho do cateto oposto: ')))
cttAd =float(input(print('Informe o tamanho do cateto adjacente:')))
hipotenusa = math.hypot(cttOp,cttAd)
print(' O tamanho da hipotenusa é igual a {:.2f}'.format(hipotenusa))