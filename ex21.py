cidade = input('Digite o nome da sua cidade: ')
cidadeSplit = cidade.split()
cidadeNomeUm = cidadeSplit[0]
verify = 'santo'
if cidadeNomeUm == verify:
    print('Sua cidade começa com santo')
else:
    print('Sua cidade não começa com santo')
