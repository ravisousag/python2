from datetime import date
nasc = int(input('Insira seu ano de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print('Sua idade é {} e sua categoria é mirim'.format(idade))
elif idade > 9 and idade<=14:
    print('Sua idade é {} e sua categoria é infantil'.format(idade))
elif idade > 14 and idade <= 19:
    print('Sua idade é {} e sua categoria é junior'.format(idade))
elif idade == 20:
    print('Sua idade é {} e sua categoria é sênior'.format(idade))
else:
    print('Sua idade é {} e sua categoria é master'.format(idade))