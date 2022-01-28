n1 = int(input('Digite um número'))
n2 = int(input('Digite um número'))
n3 = int(input('Digite um número'))
n4 = int(input('Digite um número'))
n5 = int(input('Digite um número'))
n6 = int(input('Digite um número'))
n7 = int(input('Digite um número'))

impar = 0
par = 0

if (n1%2>0):
    impar = impar + 1
else:
    par = par + 1

if (n2%2>0):
    impar = impar + 1
else:
    par = par + 1

if (n3%2>0):
    impar = impar + 1
else:
    par = par + 1

if (n4%2>0):
    impar = impar + 1
else:
    par = par + 1

if (n5%2>0):
    impar = impar + 1
else:
    par = par + 1

if (n6%2>0):
    impar = impar + 1
else:
    par = par + 1

if (n7%2>0):
    impar = impar + 1
else:
    par = par + 1

print('Impares ', impar)
print(' Pares ', par)
