from math import sqrt



def delta(a, b, c):
    return (b**2 - 4 * a * c)

def main():
    #calcula as raizes de uma equação de segundo grau
    a = float(input('Entre com o índice "a": '))
    b = float(input('Entre com o índice "b": '))
    c = float(input('Entre com o índice "c": '))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print('\nNão existe solução real possível \nas raizes são imaginárias.')
    if d == 0:
        r = -b/(2*a)
        print("""Existe uma única raiz \ne vale:
        r = {:.3f}""".format(r))
    if d > 0:
        r1 = (-b + sqrt(d))/(2*a)
        r2 = (-b - sqrt(d))/(2*a)
        print("""As raizes são Reais \ne valem:
        r1 = {:.3f}
        r2 = {:.3f}""".format(r1, r2))
