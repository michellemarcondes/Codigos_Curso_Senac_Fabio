numero = input("Digite um número de dois dígitos: ")


digito1 = int(numero[0])
digito2 = int(numero[1])
soma = digito1 + digito2
print("A soma dos dígitos é:", soma)

numero_int = int(numero)

if numero_int % soma == 0:
    print(f"O numero {numero} está na sequencia de HARSHAD")
else:
    print(f"O numero {numero} não faz parte da seuquencia de HARSHAD")