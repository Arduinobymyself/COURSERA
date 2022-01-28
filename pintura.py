# recebendo as informações do usuário
l = float(input('Qual a largura da parede em metros? '))
a = float(input('Qual a altura da parede em metros? '))

# calculando a area a ser pintada
area = a * l

# acescentando 10% de folga
area = area*1.1

# arredondando a área
excesso = area - int(area)
area = int(area)
if excesso > 0:
    area = area + 1
print('A área a ser pintada é de {} m^2.'.format(area))

# calculando o número de litros necessários
litros = area // 6
if area % 6 > 0:
    litros = litros + 1
print('Litros necessários: {} litros.'.format(litros))

# apenas latas de 18 litros
latas = litros // 18
if litros % 18 > 0:
    latas = latas + 1
print('\nOpção 1) comprar apenas latas de 18 litros.')
print('Serão necessárias {} latas.'.format(latas))
print('Obteremos {} litros.'.format(latas*18))
print('Total: R$ {}'.format(latas*80))

# apenas latas de 4 litros
galoes = litros // 4
if galoes % 4 > 0:
    galoes = galoes + 1
print('\nOpção 2) comprar apenas galões de 4 litros.')
print('Serão necessárias {} latas.'.format(galoes))
print('Obteremos {} litros.'.format(galoes*4))
print('Total: R$ {}'.format(galoes*25))

# mesclando latas de 18 litros e galões de 4 litros

#Vamos pensar, o preço total por litro pago nas latas é 80/18 ~ 4.44 R$/L
#enquanto que para o galão é 25/4 ~ 6.25 R$/L
#portanto é sempre mais vantajoso comprar o máximo de latas possíveis
#e o mínimo de galões, desde que o preço desses galões não ultrapasse o preço
#de uma lata, isto é, o numero de galões seja menor ou igual a 3 (R$ 75)

latas = litros // 18
galoes = 0
litros_restantes = litros % 18
if litros_restantes <= 3 * 4:
    #Ou seja o numero de galões necessários seja menor do que três
    galoes = litros_restantes // 4
    if litros_restantes % 4 > 0:
        galoes = galoes + 1
else:
    latas = latas + 1
print('\nOpção 2) mesclando latas e galoes.')
print('Serão necessárias {} latas.'.format(latas))
print('Serão necessárias {} galões.'.format(galoes))
print('Obteremos {} litros.'.format(latas*18 + galoes*4))
print('Total: R$ {}'.format(latas*80 + galoes*25))



