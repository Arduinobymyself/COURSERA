"""
Faça um programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas, unidade do mesmo.
Observando os termos no plural a colocação do "e", da virgula
entre outros.
Exemplo:
326 = "3 centenas, 2 dezenas e 6 unidades."
12 = "1 dezena e 2 unidades."
Testar com: 326, 300, 100, 320, 310, 305, 301,
101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

n = int(input('Digite um número entre 0 e 999: '))

if n>999:
    print('Número Inválido')
else:
    u = n // 1 % 10
    d = n // 10 % 10
    c = n // 100 % 10


if c==0:
    aux = ' '
elif c>1:
    aux = str(c) + ' Centenas, '
else:
    aux = str(c) + ' Centena, '
if d==0:
    print('')
elif d>1:
    aux = aux + str(d) + ' Dezenas e '
else:
    aux = aux + str(d) + ' Dezena e '
if u==0:
    print('')
elif u>1:
    aux = aux + str(u) + ' Unidades.'
else:
    aux = aux + str(u) + ' Unidade.'

print(aux) 
