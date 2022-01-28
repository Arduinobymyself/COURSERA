
"""
Quantas vezes o digito d ocorre no número n
"""
n = int(input('Digite o valor de n (n>0): '))
d = int(input('Digite o valor de d (0<=d<=9): '))

aux = n
aux2 = len(str(aux))


teste = aux % 10
result = 0


if (teste == d and teste != 0):
    result = result + 1
aux = aux // 10
teste = aux % 10

if (teste == d and teste != 0):
    result = result + 1
aux = aux // 10
teste = aux % 10    

if (teste == d and teste != 0):
    result = result + 1
aux = aux // 10
teste = aux % 10

if (teste == d and teste != 0):
    result = result + 1
aux = aux // 10
teste = aux % 10

if (teste == d and teste != 0):
    result = result + 1
aux = aux // 10
teste = aux % 10

print('O digito {} ocorre {} vezes em {}'.format(d, result, n))
