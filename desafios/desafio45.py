from random import randint
itens = ('Pedra','papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções são
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua jogada? '))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador ganhou')
    elif jogador == 2:
        print('Jogador perdeu')
    else:
        print('Opção inválida')

elif computador == 1:
    if jogador == 0:
        print('Computador ganhou')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador ganhou')
    else:
        print('Opção inválida')

elif computador == 2:
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('Empate')
    else:
        print('Opção inválida')
else:
    print('Opção inválida')