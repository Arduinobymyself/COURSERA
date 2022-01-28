"""
Refaça o exercício 1 imprimindo os retângulos sem preenchimento,
de forma que os caracteres que não
estiverem na borda do retângulo sejam espaços.
"""


#recebe valores do usuário
largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

#auxiliares
a = 1
l = 1

#loop principal
while a <= altura:
    while l <= largura:
        if l <= largura and a <= altura:
            # verifica se estamos na primeira linha  ou primeira coluna (nas bordas)
            if l == 1 or l == largura or a == 1 or a == altura:
                print('#', end='')
            # verifica se estamos numa linha e coluna interna
            if l != 1 and l != largura and a != 1 and a != altura:
                print(' ', end='')
            l += 1
    print('')
    a += 1
    l = 1