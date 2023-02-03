salario = int(input('digite o seu salario: '))

if salario >= 1250:
    aumento = salario * 0.10
    print("Seu Aumento foi de: {}, ou seja, 10% de aumento".format(aumento))
if salario < 1250:
    aumento = salario * 0.15
    print("Seu Aumento foi de: {}, ou seja, 15% de aumento".format(aumento))

