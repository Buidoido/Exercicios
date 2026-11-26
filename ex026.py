frase = str(input('Digite uma frase: ')).strip().upper()
QA = frase.count('A')
FP = frase.find('A') + 1
LP = frase.rfind('A') + 1
print(f'A quantidade de palavras [A] na frase: {QA}')
print(f'A primeira aparição do [A] na frase: {FP}')
print(f'A Ultima aparição do [A] na frase: {LP}')