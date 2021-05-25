peso = float(input('Insira seu peso: '))
alt = float(input('Insira sua altura: '))
imc = peso/(alt*alt)

if imc<18.5:
    print('Seu imc é {} e está abaixo do peso'.format(imc))
elif imc>=18.5 and imc<25:
    print('Seu imc é {} e está no peso ideal'.format(imc))
elif imc>=25 and imc<30:
    print('Seu imc é {} e está com sobrepeso'.format(imc))
elif imc>=30 and imc<40:
    print('Seu imc é {} e tu é um obeso'.format(imc))
else:
    print('Seu imc é {} e tu é um obeso fudido e vai morrer'.format(imc))