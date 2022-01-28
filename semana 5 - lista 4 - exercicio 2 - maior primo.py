
"""
VERSÃO 2
def maior_primo(n):
    k = n        
    while k > 1 and primo(k)==False:
        k = k - 1
    return k

def primo(k):
    aux = True    
    div = 2
    while k > div:     
        if k % div == 0:
            aux = False
        div = div + 1
    return aux
"""


"""
VERSÃO 1
"""
def maior_primo(n):
    div = 1
    aux = True   
    cont = 0
    while div <= n and aux:
        if n % div == 0:
            cont = cont + 1  
        if cont >= 3:
            cont = 1
            n = n - 1
            div = 1
        if cont == 2 and n == div:
            aux = False   
        div = div + 1
    return n

n = maior_primo(121)
print(n)