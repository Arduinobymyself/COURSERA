"""
Escreva a função n_primos que recebe como argumento um número inteiro
maior ou igual a 2 como parâmetro e devolve a quantidade de números
primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
"""


div = 2
aux = 0
flag = False
soma = 0
cont = 0

def primo(n):
    div = 2
    aux = 0
    if n <= 1:
        #print('é primo')
        return False
    else:
        while div < n:
            if n % div == 0:
                if aux == 0:
                    #print("não primo")
                    aux += 1
                    div += 1
                    return False
                else:
                    aux += 1
                    div += 1
            else:
                div += 1
        if aux == 0:
            return True
            #print("primo")




n = int(input('Digite um número: '))
print('Os números primos são:', end = ' ')

while n >= 2:
    flag = primo(n)
    if flag == True:
        print('{},'.format(n), end=' ')
        soma = soma + n
        cont += 1
    n -= 1
print('\nSão {} números primos.'.format(cont))
print('A soma entre eles vale {}.'.format(soma))
