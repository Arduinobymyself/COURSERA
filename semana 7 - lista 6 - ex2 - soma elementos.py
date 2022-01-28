# Escreva a função soma_elementos que recebe como parâmetro uma lista
# com números inteiros e devolve um número inteiro correspondente à
# soma dos elementos da lista recebida.

def soma_elementos(lista):
    soma = 0
    for s in lista:
      soma = soma + s
    return soma


#testes
l = [1, 3, 5, 7, 9]
soma = soma_elementos(l)
print(soma)