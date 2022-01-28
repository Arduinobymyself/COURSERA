'''
Escreva a função maiusculas(frase) que recebe uma frase (uma string) como
parâmetro e devolve uma string com as letras maiúsculas que existem nesta
frase, na ordem em que elas aparecem.
'''


def maiusculas(frase):
    i = 0
    while i < len(frase):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            print(frase[i], end='')
        else:
            pass
        i += 1


# testes
if __name__ == '__main__':
    maiusculas('Programamos em python 2?')
    print()
    maiusculas('Programamos em Python 3.')
    print()
    maiusculas('PrOgRaMaMoS em python!')
    print()
    maiusculas('PYT;.,:><]~ç}^Ç[´{`)(*&¨%$#@!/?HON')
    print()
