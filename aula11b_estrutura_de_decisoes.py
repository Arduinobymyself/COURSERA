a = int(input('Digite um valor a: '))
b = int(input('Digite um valor b: '))
c = int(input('Digite um valor c: '))


if a>b>c:
    print('a > b > c')
elif a>c>b:
    print('a > c > b')
elif b>a>c:
    print('b > a > c')
elif b>c>a:
    print('b > c > a')
elif c>a>b:
    print('c > a > b')
else:
    print('c > b > a')






