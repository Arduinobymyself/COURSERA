
n = int(input("Digite um número inteiro: "))

div = 2
aux = 0


if n <= 1:
    print("não primo")
else:
    while div < n:
        if n % div == 0:
            if aux == 0:
                print("não primo")
                aux = aux + 1
                div = div + 1
            else:
                aux = aux + 1
                div = div + 1
        else:
            div = div + 1
    if aux == 0:
        print("primo")


