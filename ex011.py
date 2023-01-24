m1 = float(input('digite a largura da sua parede: '))
m2 = float(input('digite o comprimento de sua parede: '))
mq = m1 * m2
print(f'A dimensão de sua parede é de {m1} x {m2} e a área é de: {mq}m2')
tinta = mq / 2
print('para pintar essa parede voce precisa de {} litros de tinta'.format(tinta))
