numero = int(input('Insira um numero: '))
print ('''Escolha a base de conversão'
               1- Binário
               2- octal
               3- Hexadecimal''')
op = int(input('Sua opção: '))
if op == 1:
    print('O número {} convertido em binániro é igual a: {}'.format(numero, bin(numero)[2:]))

elif op == 2:
    print('O número {} convertido em octal é igual a: {}'.format(numero, oct(numero)[2:]))

elif op == 3:
    print('O número {} convertido em hexadecimal é igual a: {}'.format(numero, hex(numero)[2:]))
else:
    print('Você escolheu opção inválida')