
n = int(input("Digite o valor de n: "))

contador = n-1
produto = n
if n == 0:
    print("1")
else:
    while contador > 1:
        produto = produto * contador
        contador = contador - 1
    print(produto)



