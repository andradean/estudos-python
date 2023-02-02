numero = int(input('Digite um numero de 0 a 9999: '))
numeroU = numero // 1 % 10
numeroD= numero // 10 % 10
numeroC = numero // 100 % 10
numeroM = numero // 1000 % 10

print (f"""
Seu numero é: {numero}
A unidade dele é: {numeroU}
A dezena dele é: {numeroD}
A centena dele é: {numeroC}
O Milhar dele é: {numeroM}
""")