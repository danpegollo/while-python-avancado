lado = int(input("Coloque o lado do quadrado desejado: "))
linha = lado
while linha > 0:
    if linha == lado: 
        print("*" * lado)
        linha -= 1
    elif linha == 1:
        print("*" * lado)
        linha -= 1
    else:
        print("*" + " " * (lado - 2) + "*")
        linha -=1