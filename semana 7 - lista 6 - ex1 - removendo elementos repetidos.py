# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros,
# verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma
# lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida
# deve estar ordenada.

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

#testes
lista = [1, 2, 3, 3, 3, 4]

lista = remove_repetidos(lista)
print (lista)