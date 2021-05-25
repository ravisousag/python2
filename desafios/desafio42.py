r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar triângulos')
    if r1 == r2 == r3:
        print('Triângulo equilatero')
    elif r1 != r2 != r3 != r1:
        print('Triângulo escaleno')
    else:
        print('Triângulo isóceles')
else:
    print('Os segmentos não podem formar triângulo')