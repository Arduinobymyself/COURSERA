

#definindo a função fatorial
def fatorial(n):
    contador = n-1
    produto = n
    if n == 0:
        print("1")
    else:
        while contador > 1:
            produto = produto * contador
            contador = contador - 1
        return produto



#solicitando entrada do usuário
n = int(input("digite o valor n: "))
k = int(input("digite o valor k: "))

#calculando o coeficiente binomial
b = fatorial(n)//(fatorial(k)*fatorial(n-k))

#imprimindo a resposta ao usuário
print("binomial ({}/{}) = {}".format(n, k, b))
