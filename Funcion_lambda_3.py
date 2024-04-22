#Contagios en Nuncalandia:

if __name__ == "__main__":
    c=int(input("Ingrese la cantidad de contagiados iniciales: "))
    d=int(input("Ingrese el numero de dias que quiere que transcurran: "))
    contagiados=(lambda x, y: x*2**y)(c, d)
    print(f"Si tenemos {c} contagiados en el dia 0 y transcurren {d} días, entonces, la cantidad final de enfermos va a ser de {contagiados}")