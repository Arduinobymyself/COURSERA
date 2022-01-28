"""
Faça um programa que peça dois números,
calcule e mostre o primeiro número (base) elevado ao
segundo número (expoente).
Não utilize a função de potenciação da linguagem.
"""

base = int(input("digite o valor da base: "))
expoente = int(input("digite o valor do Expoente: "))
potencia = 1
contador = 0 
while contador < expoente:
    potencia = potencia*base
    contador = contador + 1
print(" {} elevado a {} potência = {}".format(base, expoente, potencia) )

