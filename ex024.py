frase = str(input('digite uma frase: ')).upper()
frase = frase.replace(' ', '')
print('a letra a aparece {} vezes na frase'.format(frase.count('A')))
print('a letra a aparece na posição {} pela primeira vez'.format(frase.find('A') + 1))
print('a letra a aparece na posição {} pela ultima vez'.format(frase.rfind('A') + 1))


