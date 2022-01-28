"""
Dado um número inteiro positivo n,
impirmir os n primeiros naturais ímpares.
n = 4 -> 1, 3, 5, 7
n = 3 -> 1, 3, 5
n = 7 -> 1, 3, 5, 7, 9, 11, 13.
.
.
"""


soma = 1
contador = 0

n = int(input("Digite um número: "))

while contador < n:
    print(soma)
    soma = soma + 2
    contador = contador + 1

