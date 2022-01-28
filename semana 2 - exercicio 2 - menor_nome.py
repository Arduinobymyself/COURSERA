'''
Escreva uma função menor_nome(nomes) que recebe uma lista de strings
com nome de pessoas como parâmetro e devolve o nome mais curto
presente na lista.
'''

def menor_nome(nomes):
  item = nomes[0].capitalize().strip()
  for c in nomes:
    if len(c.capitalize().strip()) < len(item):
      item = c.strip().capitalize()
  print(f'{item}')


# testes
if __name__ == '__main__':
    menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
    print()
    menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
    print()
    menor_nome(['LU   ', ' josé ', 'PAULO', 'Catarina'])
    print()
    menor_nome(['zé', ' lu', 'fê'])
    print()
    menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
    print()
