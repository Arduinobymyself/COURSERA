def sao_multiplicaveis(m1, m2):
  matriz_mult = []

  lin1 = len(m1)
  col1 = len(m1[0])
  lin2 = len(m2)
  col2 = len(m2[0])

  if col1 == lin2:
    for i in range(lin1):
      for j in range(col1):
        matriz_mult
    return True
  else:
    return False


# testes
if __name__ == '__main__':
  m1 = [[1, 2, 3], [4, 5, 6]]
  m2 = [[2, 3, 4], [5, 6, 7]]
  print(sao_multiplicaveis(m1, m2))

  m1 = [[1], [2], [3]]
  m2 = [[1, 2, 3]]
  print(sao_multiplicaveis(m1, m2))

  m1 = [[1], [2], [3]]
  m2 = [[1]]
  print(sao_multiplicaveis(m1, m2))

  m1 = [[1], [2], [3]]
  m2 = [[1, 2, 3], [4, 5, 6]]
  print(sao_multiplicaveis(m1, m2))
