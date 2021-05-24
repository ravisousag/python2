numero = int(input('Insira um numero: '))

op = int(input('Escolha a base de conversão \n'
               '1- Binário \n'
               '2- octal \n'
               '3- Hexadecimal'))
if op == 1:
    conv=bin(numero)
    print('O número {} convertido em hexadecimal é igual a: {}'.format(numero, conv))

elif op == 2:
    conv=oct(numero)
    print('O número {} convertido em hexadecimal é igual a: {}'.format(numero, conv))

elif op == 3:
    conv=hex(numero)
    print('O número {} convertido em hexadecimal é igual a: {}'.format(numero, conv))
else:
    print('Você escolheu opção inválida')