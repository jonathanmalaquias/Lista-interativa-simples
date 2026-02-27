lista = ["arroz" , "feijão" , "macarrão" , "ovo" , "leite" , "batatas" , "nescau" , "cenouras", "frango"]
Comprados = []
faltaram = []
for n in lista:
    print(f"O item {n} tem no mercado?")
    validar = input("s / n")
    if validar == "s":
        Comprados.append(n)
    elif validar == "n":
        faltaram.append(n)
    else :
        print("eu num tindi uque ele falooou")
print(Comprados)
print(faltaram)
                
