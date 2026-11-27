from random import randrange
maquina = randrange(0, 6)
valor = int(input('Adivinhe o valor: '))
if valor == maquina:
    print(f'PARABENS!! A maquina pensou {maquina}')
else:
    print(f'A MAQUINA GANHOU!! Ela pensou {maquina}!')