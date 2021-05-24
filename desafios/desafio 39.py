nasc = int(input('Insira seu ano de nascimento: '))
idade = 2021-nasc

if idade<17:
    valid = 18-idade
    print('Você ainda não tem idade para se alistar, faltam {} anos para se alistar'.format(valid))

elif idade==17:
    valid = 18 - idade
    print('Você ainda não tem idade para se alistar, falta {} ano para se alistar'.format(valid))

elif idade==18:
    print('Você precisa se alistar, você tem {} anos'.format(idade))
else:
    valid = (idade-18)
    print('Você já se alistou há {} anos'.format(valid))