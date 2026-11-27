km = float(input('Quantos km foram percorridos: '))
dia = int(input('Quantos dias foram utilizados: '))
valork = km * 0.15
valord = dia * 60
total = valork + valord
print(f'O valor em km são de R${valork:.2f} de dias é de R${valord:.2f}, o total a pagar é de R${total:.2f}')
