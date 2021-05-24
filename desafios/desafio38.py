a = int(input('Insira primeiro número: '))
b = int(input('Insira segundo número: '))

if a>b:
    print('O número A({}) é maior que o número B({})'.format(a,b))
elif b>a:
    print('O número B({}) é maior que o número A({})'.format(b,a))
else:
    print('Os números são iguais')