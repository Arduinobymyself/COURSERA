#Semana 3 - atividade adicional 1
#Distância entre dois pontos

from math import sqrt #Importando somente "sqrt" do módulo "math"

x1 = int(input('Digite a coordenada x1: '))
y1 = int(input('Digite a coordenada y1: '))
x2 = int(input('Digite a coordenada x2: '))
y2 = int(input('Digite a coordenada y2: '))

#Calculando a distância entre 2 pontos
dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#Saída com as informações solicitadas
if (dist >= 10):
    print('longe')
else:
    print('perto')

