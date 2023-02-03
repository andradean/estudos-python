import random

numAle = random.randint(0, 5)

resposta = int(input('Digite o numero que o computador pensou: '))
if resposta == numAle:
    print('você GANHOU!!!')
else:
    print('você perdeu :/')
