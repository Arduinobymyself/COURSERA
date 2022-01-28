
def imprime_matriz(A):
  lin = len(A)
  col = len(A[0])

  for i in range(lin):
    for j in range(col):
      if j == col - 1:
        print(A[i][j])
      else:
        print(A[i][j], end=' ')


if __name__ == '__main__':
  minha_matriz = [[1], [2], [3]]
  imprime_matriz(minha_matriz)
  print()
  minha_matriz = [[1, 2, 3], [4, 5, 6]]
  imprime_matriz(minha_matriz)
  print()
  minha_matriz = ([[1, 2, 7], [3, 4, 8], [1, 2, 3]])
  imprime_matriz(minha_matriz)