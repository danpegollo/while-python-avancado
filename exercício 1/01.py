numero = int(input("Coloque um número inteiro natural entre 0 e 15: "))
i = numero
resultado = 1

if numero > 15 or numero < 0:
    print("Coloque um número válido")
elif numero == 0:
    resultado = 1
    print(f"O fatorial de {numero}, é de {resultado}")
else:
    while i > 0:
        resultado = i * resultado
        i = i - 1
    print(f"O fatorial de {numero}, é de {resultado}")