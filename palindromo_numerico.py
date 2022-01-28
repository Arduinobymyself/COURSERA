"""
Dizemos que um número natural n é palíndromo se
o 1º algarismo de n é igual ao seu último algarismo,
o 2º algarismo de n é igual ao penúltimo algarismo,
e assim sucessivamente.

exemplos:
567765 e 32423 são palíndromos.

Exercício: Dado um número natural n > 10, verificar se n
é palíndromo.
"""
#   aux         dig         reverso         n
#   567765      0               0          567765
# ----------------------------------------------------
#   567765      5               5
#   56776       6               50 + 6 -> 56
#   5677        7               560 + 7 -> 567
#   567         7               5670 + 7 -> 5677
#   56          6               56770 + 6 -> 56776
#   5           5               567760 + 5 -> 567765
#   0

#   aux//10     aux%10          reverso*10+dig

n = int(input('Digite um número maior que 10: '))

aux, reverso = n, 0

while aux != 0:
    reverso = reverso * 10 + aux % 10
    aux //= 10
if reverso == n:
    print(f'{n} é palíndromo')
else:
    print(f'{n} não é palíndromo')
