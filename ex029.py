from calendar import isleap

ano = int(input("digite um ano: "))

if isleap(ano):
    print('Esse ano é bissesto')
else:
    print('Esse ano não é bissesto')

