#calcula as raizes de uma equação de segundo grau
a = float(input('Entre com o índice "a": '))
b = float(input('Entre com o índice "b": '))
c = float(input('Entre com o índice "c": '))

delta = (b**2 - 4 * a * c)

if delta < 0:
    print('Não existe solução real possível \nas raizes são imaginárias')
if delta == 0:
    r = -b/(2*a)
    print('Existe uma única raiz \ne vale: r = {:.3f}'.format(r))
if delta > 0:
    r1 = (-b + delta**(1/2))/(2*a)
    r2 = (-b - delta**(1/2))/(2*a)
    print('As raizes são Reais \ne valem: r1 = {:.3f} e r2 = {:.3f}'.format(r1, r2))
