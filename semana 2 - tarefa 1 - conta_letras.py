'''
Escreva a função conta_letras(frase, contar="vogais"),
que recebe como primeiro parâmetro uma string contendo uma frase e como
segundo parâmetro uma outra string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais",
a função deve devolver o numero de vogais presentes na frase.
Quando ele for definido como "consoantes", a função deve devolver
o número de consoantes presentes na frase.
Se este parâmetro não for passado para a função, deve-se assumir
o valor "vogais" para o parâmetro.
'''

def conta_letras(frase, contar='vogais'):
    frase = retira_espacos(frase) # chama a função para retirar espaços no string

    conta_vogal = 0
    conta_consoante = 0

    for c in frase:
        if c in 'aeiouAEIOU':
            conta_vogal +=1
        else:
            conta_consoante += 1
    if contar == 'vogais':
        print(conta_vogal)
    else:
        print(conta_consoante)


def retira_espacos(frase):
    pos = 0
    frase_aux = ""
    while pos < len(frase):
        if frase[pos] != " ":
            frase_aux = frase_aux + frase[pos]
        pos = pos + 1
        frase_aux = frase_aux.capitalize()
    return frase_aux



# testes
if __name__ == '__main__':
    conta_letras('programamos em python')
    # deve devolver 6

    conta_letras('programamos em python', 'vogais')
    # deve devolver 6

    conta_letras('programamos em python', 'consoantes')
    # deve devolver 13

    conta_letras('oi', 'consoantes')
    # deve devolver 0