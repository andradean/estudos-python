import random

n1 = input('nome 1: ')
n2 = input('nome 2: ')
n3 = input('nome 3: ')
n4 = input('nome 4: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem da apresentação será: {}'.format(lista))

