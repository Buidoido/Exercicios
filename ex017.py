from math import hypot
cat = float(input('Digite o cateto oposto : '))
cat2 = float(input('Digite o cateto adjacente: '))
valor = hypot(cat, cat2)
print(f'O valor da hipotenusa do triandgulo retangulo {valor:.2f}')

