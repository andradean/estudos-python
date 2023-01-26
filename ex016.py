from math import hypot

co = float(input('digite o cateto oposto '))
ca = float(input('digite o cateto adjascente '))

print('o comprimento da hipotenusa é: {:.2f} '.format(hypot(co, ca)))
