
"""
mostra o digito das dezenas
"""

n = int(input('Digite um número inteiro:'))
n = n % 100
n = n // 10
print('O dígito das dezenas é', n)
