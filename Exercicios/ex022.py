nome = str(input('Digite o seu nome completo: '))
primeiro = nome.split()[0]
print(f'O nome completo em maiusculo é {nome.upper()}')
print(f'O nome completo em minusculo é {nome.lower()}')
print(f'O total de letras sem espaços: {len(nome.replace(' ',''))}')
print(f'Seu primeiro nome é {primeiro} e ele contem: {len(primeiro)}')
