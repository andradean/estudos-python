import random

aluno1 = input('digite o primeiro aluno: ')
aluno2 = input('digite o segundo aluno: ')
aluno3 = input('digite o terceiro aluno: ')
aluno4 = input('digite o quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
ale = random.choice(alunos)

print('o aluno escolhido foi o aluno {}'.format(ale))

