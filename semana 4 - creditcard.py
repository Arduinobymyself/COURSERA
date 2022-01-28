

myCard = int(input('Digite o número do seu cartão de crédito: '))

cardList = 1
foundMyCard = False

while cardList != 0 and not foundMyCard:
    cardList = int(input('Digite o número do próximo cartão de crédito: '))
    if cardList == myCard:
        foundMyCard = True
        
if foundMyCard:
    print('Meu cartão está validado!')
else:
    print('Meu cartão não está validado')

