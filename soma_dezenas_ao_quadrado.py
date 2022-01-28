"""
Qualquer número natural de quatro algarismo pode ser dividido
em duas dezenas formadas pelos seus dois primeiros e dois
últimos digitos.
Exemplos:
1297: 12 e 97
5314: 53 e 14

Escreva um programa que imprime todos os milhares (4 algarismos)
1000 <= n < 10000
cuja raiz quadrada seja a soma das dezenas formadas pela
divisão acima.
Exemplo:
raiz de 9801 = 99 => 98 + 01 = 99
portanto 9801 é um número a se impresso.
"""

#1000 --> 10 00 --> 10 + 0 = 10 --> 10**2 = 100 --> 100 != 1000
#1001 --> 10 01 --> 10 + 1 = 11 --> 11**2 = 121 --> 121 != 1001
#  .
#  .
#9801 --> 98 01 --> 98 + 1 = 99 --> 99**2 = 9801 --> 9801 == 9801 -> IMPRIME

num = 1000
while num < 10000:
    aux = num
    dois_ult = aux % 100
    aux //= 100
    dois_prim = aux % 100
    if (dois_ult + dois_prim) ** 2 == num:
        print(num)
    num += 1





