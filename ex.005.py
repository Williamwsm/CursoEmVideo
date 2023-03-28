import math
angulo = int(input(print('Digite o valor do angulo: ')))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O angulo que voce escolheu foi {}, seu seno é: {:.2f}\nO coseno é : {:.2f} e sua tangente é {:.2f}'.format(angulo,seno,cos,tang))