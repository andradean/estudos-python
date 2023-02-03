viagem = int(input('qual a distancia da sua viagem: '))

if viagem <= 200:
    preco = viagem * 0.50
    print('O preço da sua viagem é de: {} R$'.format(preco))
else:
    preco = viagem * 0.45
    print('O preço da sua viagem é de: {} R$'.format(preco))
