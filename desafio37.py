valor=float(input('Insira o valor da casa: '))
salario=float(input('Insira seu salario: '))
anos=int(input('tempo de emprestimo: '))

meses=anos*12
valorPrest=(valor/(meses))

if valorPrest > salario*0.3:
    print('O valor de prestação mensal excede 30% do seu salário')
else:
    print('Seu empréstimo de {} terá o valor mensal de {} por {} meses foi aprovado'.format(valor,valorPrest,meses))