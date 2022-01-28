
"""
Verifica se um número recebido possui ao menos
um dígito com dígito adjacente igual a ele.
"""



n = int(input("Digite o valor de n: "))

aux = 0
adjacente = 0

anterior = n % 10
n = n // 10

while n > 0:
    aux = n % 10
    if anterior == aux:
        adjacente = 1
    anterior = aux
    n = n // 10
if adjacente:
    print("sim")
else:
    print("não")
