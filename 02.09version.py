import random
 
def numero_perfeito(n):
    soma_divisores = 0  
    for i in range(1, n):
        if n % i ==0:
            soma_divisores += i
    return soma_divisores == n
 
numero = int(input("Digite um numero : "))
if numero_perfeito(numero):
    print(f"{numero} é um numero perfeito! ")
else:
    print(f"{numero} não é um numero perfeito! ")28
    