#Semana 3 exercício adicional 2
#Calculando as raizes de uma equação de segundo grau

#Importando "sqrt" do módulo "math"
from math import sqrt

#Entrada de dados
a = float(input('Entre com o parâmetro "a": '))
b = float(input('Entre com o parâmetro "b": '))
c = float(input('Entre com o parâmetro "c": '))

#Calculando o Delta
delta = (b**2 - 4 * a * c)

if (delta < 0):
    print('esta equação não possui raízes reais')
if (delta == 0):
    r = -b/(2*a)
    print('a raiz desta equação é {:.1f}'.format(r))
if (delta > 0):
    r1 = (-b + sqrt(delta))/(2*a)
    r2 = (-b - sqrt(delta))/(2*a)
    if (r1 > r2):
        print('as raízes da equação são {:.1f} e {:.1f}'.format(r2, r1))
    else:
        print('as raízes da equação são {:.1f} e {:.1f}'.format(r1, r2))
