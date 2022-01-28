largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

l = 1
a = 1

while a <= altura:
    while l <= largura:
        print('#', end=' ')
        l += 1
    print()
    a += 1
    l = 1
