import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor seno do Angulo {} vale {:.2f}'. format(angulo, seno))
print('O valor cosseno do Angulo {} vale {:.2f}'. format(angulo, cosseno))
print('O valor tangente do Angulo {} vale {:.2f}'. format(angulo, tangente))
