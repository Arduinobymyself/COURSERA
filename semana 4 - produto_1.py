

produto = 1
valor = 0
n = 0

n = int(input('Digite quantos valores devem ser multiplicados: '))

while n != 0:
    valor = int(input('Digite um valor: '))
    produto = produto * valor
    n -= 1
print('O produto dos valores digitados é {}'.format(produto))
