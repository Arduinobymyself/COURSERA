"""
Ler uma sequencia de números digitados pelo usuário e,
para cada número digitado informar seu fatorial.
"""


n = int(input('Digite um número inteiro: '))
while n >= 0:

    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n -= 1
    print(fatorial)
    n = int(input('Digite um número inteiro: '))


