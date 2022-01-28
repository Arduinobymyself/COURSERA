"""
Saque permitido de R$10 a R$600
Notas do caixa: R$100, R$50, R$10,R$5 e R$1
Pergunte ao usuário a quantia a ser sacada.
Mostre quantas notas de cada ele vai receber
"""


saque = int(input("Digite o valor do saque: "))

if 10 <= saque <= 600:
    notas_cem = saque // 100
    saque = saque % 100
    notas_cinquenta = saque // 50
    saque = saque % 50
    notas_dez = saque // 10
    saque = saque % 10
    notas_cinco = saque // 5
    saque = saque % 5
    notas_um = saque // 1

    if notas_cem >0:
        print(" {} notas de R$100,00".format(notas_cem))
    if notas_cinquenta >0:
        print(" {} notas de R$50,00".format(notas_cinquenta))
    if notas_dez >0:
        print(" {} notas de R$10,00".format(notas_dez))
    if notas_cinco >0:
        print(" {} notas de R$5,00".format(notas_cinco))
    if notas_um >0:
        print(" {} notas de R$1,00".format(notas_um))
else:
    print("Não é possível fazer o saque")
        
    
    
    
