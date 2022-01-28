"""
Imprime a soma dos dígitos de um número inteiro
"""

n = int(input("Digite um número inteiro: "))

soma = 0
aux = n
i = len(str(n))#Lê o comprimento do número digitado
while not i == 0:
    aux = n % 10
    soma = soma + aux
    n = n // 10
    i = i - 1
print(soma)
