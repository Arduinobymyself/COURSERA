"""
Dada uma sequência de números inteiros não nulos,
seguida por 0, imprimir seus quadrados.
"""

flag = 1
while flag == 1:
    n = int(input("Digite um número: "))
    if n != 0:
        print("{} ao quadrado = {}".format(n, n**2))
    else:
        flag = 0
print("Fim do programa!")
    
          
