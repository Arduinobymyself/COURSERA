'''
Escreva a função primeiro_lex(lista) que recebe uma lista de strings
como parâmetro e devolve o primeiro string na ordem lexicográfica.
Neste exercício, considere letras maiúsculas e minúsculas.
'''

def primeiro_lex(meu_string):
  item = meu_string[0].strip()
  for c in meu_string:
    if c.strip() < item:
      item = c.strip()
  print(f'{item}')



if __name__ == '__main__':
  primeiro_lex(['oĺá', 'A', 'a', 'casa'])
  # deve devolver 'A'
  print()
  primeiro_lex(['AAAAAA', 'b'])
  # deve devolver 'AAAAAA'
  print()
  primeiro_lex(['maria', 'josé', 'PAULO', 'Catarina'])
  print()
  primeiro_lex(['zé', 'lu', 'fê'])
  print()

