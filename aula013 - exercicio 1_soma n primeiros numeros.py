"""
Dado um número inteiro positivo n,
Calcular a soma dos n primeiros números inteiros positivos.
"""


flag = 1
soma = 0
contador = 0
while flag > 0:
    n = int(input("Digite um número: "))
    if n <= 0:#se n = 0, usuário deseja terminar; se n < 0 não é positivo
        flag = 0
    soma = soma + n
    contador = contador + 1
if contador > 1:#se contador é 1 significa que usuário entrou somente um número 0 e deseja terminar
    print("a soma dos {} primeiros números vale: {}".format(contador-1, soma))

