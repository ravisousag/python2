nota1 = float(input('Insira primeira nota: '))
nota2 = float(input('Insira segunda nota: '))
media = (nota1+nota2)/2

if media<5:
    print('Sua média é {} e foi reprovado'.format(media))
elif media >= 5 and media<7:
    print('Sua média é {} e você está em recuperação'.format(media))
else:
    print('Sua média é {} e você foi aprovado'.format(media))