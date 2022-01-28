

soma = 0
valor = 0
n = 0

n = int(input('Digite quantos valores devem ser somados: '))

while n != 0:
    valor = int(input('Digite um valor: '))
    soma = soma + valor
    n -= 1
print('A soma dos valores digitados é {}'.format(soma))
