def dimensoes(matriz):
  linha = 0
  coluna = 0
  for i in matriz:
    mat = matriz[linha]
    linha += 1
  for j in mat:
    coluna +=1
  print(f'{linha}x{coluna}')



minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)
minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)
minha_matriz = [[1], [2]]
dimensoes(minha_matriz)
minha_matriz = [1, 2, 3], [4, 5, 6], [7, 8, 9]
dimensoes(minha_matriz)
