resultado = 1
numero = int(input("Coloque o valor de um número: "))
i = 1

while i <= numero:
    fatorial = 1
    j = 1
    while j <= i:
        fatorial *= j
        j += 1

    div = 1 / fatorial
    resultado += div    
    i += 1
print(f"{resultado}")