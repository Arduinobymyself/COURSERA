# Escreva uma função soma_hipotenusas que receba como parâmetro
# um número inteiro positivo n e devolva a soma de todos os
# inteiros entre 1 e n que são comprimento da hipotenusa de
# algum triângulo retângulo com catetos inteiros.


from math import sqrt


def hipotenusa(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            a = i
            b = j
            c = int(sqrt((a ** 2) + (b ** 2)))
            if (c > a) and (c > b) and (c < (a + b)):
                if (a ** 2) + (b ** 2) == c ** 2:
                    if c == n:
                        return c
            j = j + 1
        i = i + 1

    return 0


def soma_hipotenusas(n):
    soma = 0
    old = 0
    for i in range(1, n+1):
        result = hipotenusa(i)
        if result > old:
            old = result
            soma = soma + result

    return soma

#just for testing purpposes
n = soma_hipotenusas(25)
print(n)