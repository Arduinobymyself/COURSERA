
soma = 0

#recebe o valor digitado pelo usuário
n = int(input('digite um número: '))

#calcula o comprimento do número digitado
l = len(str(n))

#repetição para calcular a soma independente de cada dígito
while l != 0:
    soma = soma + (n % 10)
    n = n // 10
    l -= 1

#mostra a resposta final
print('A soma dos digitos do número é {}'.format(soma))

