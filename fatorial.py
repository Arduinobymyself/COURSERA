"""
Dado um número inteiro não negativo n, determinar n!
5! = 5*4*3*2*1 = 120
3! = 3*2*1 = 6
"""


def fatorial(n):
    cont = n
    while cont >= 0:
        fatorial = 1
        while cont > 1:
            fatorial = fatorial * cont
            cont = cont - 1
        return fatorial


def main():
    n = 1
    
    while n >= 0:
        if n < 0:
            print('End!')
            quit()
        n = int(input("digite um número inteiro positivo: "))
        print("{}! = {}".format(n, fatorial(n)))
        print()
