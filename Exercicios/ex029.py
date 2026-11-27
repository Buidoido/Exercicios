velocidade = float(input('Qual a velocidade atual do carro: '))
excedeu = (velocidade - 80)
if velocidade > 80:
    print(f'MULTADO!. Você excedeu a velocidade limite de 80KM/H em {excedeu}KM/H!')
    print(f'Total a pagar {excedeu * 7.0:.2f}R$, 7.0R$ por KM/H excedido.')
else:
    print(f'OBRIGADO!. Sua velocidade {velocidade} está dentro do limite.')
