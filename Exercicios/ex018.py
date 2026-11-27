from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do angulo: '))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'Os valor do seno é de : {seno:.2f}')
print(f'O Valor do coseno é de {coseno:.2f}')
print(f'O Valor da tangente é de {tangente:.2f}')
