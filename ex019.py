nome = input('Digite o seu nome completo: ')
print('Seu nome em letra maiuscula é: {}'.format(nome.upper()))
print('Seu nome em letra minuscula é: {}'.format(nome.lower()))
nomelen = nome.replace(' ', '')
print('Seu nome possui {} letras'.format(len(nomelen)))
nomelista = nome.split()
print('Seu primeiro nome possui {} letras'.format(len(nomelista[0])))

