velocidade = int(input('digite a velocidade do carro: '))

multa = (velocidade - 80) * 7
if velocidade > 80:
   print('você foi multado em {}'.format(multa))


