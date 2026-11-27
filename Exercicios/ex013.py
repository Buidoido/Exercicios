func = str(input('Digite o nome do Funcionario: '))
sal = float(input('Digite o salario do funcionario: '))
au = sal * 0.15
print(f'O {func} com um salario de {sal}, recebendo um aumenro de 15% o total fica de {sal + au:.2f}')