"""
Informar, para cada valor digitado pelo usuário,
se ele é primo ou não
"""

def primo(n):
    fator = 2
    if n == 2:
        return True
    while (n % fator != 0) and (fator <= n / 2):
        fator += 1
    if n % fator == 0:
        return False
    else:
        return True




n = int(input('Digite um número: '))
while n > 0:
    if primo(n):
        print('{} é primo!'.format(n))
    else:
        print('{} não é primo!'.format(n))
    n = int(input('Digite um número: '))