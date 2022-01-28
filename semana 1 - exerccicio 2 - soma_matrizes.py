def soma_matrizes(m1, m2):

  def dimensoes(A):
      lin = len(A)
      col = len(A[0])

      return ((lin, col))

  if dimensoes(m1) != dimensoes(m2):
      return False
  else:
      matriz = []
      for i in range(len(m1)): # percorre as linhas
          linha = []
          for j in range(len(m1[0])): # percorre as colunas
              linha.append(m1[i][j] + m2[i][j])
          matriz.append(linha)
      return matriz

# testes
if __name__ == '__main__':
  m1 = [[1, 2, 3], [4, 5, 6]]
  m2 = [[2, 3, 4], [5, 6, 7]]
  print(soma_matrizes(m1, m2))

  m1 = [[1], [2], [3]]
  m2 = [[2, 3, 4], [5, 6, 7]]
  print(soma_matrizes(m1, m2))