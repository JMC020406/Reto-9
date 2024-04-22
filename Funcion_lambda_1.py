#Cantidad de carne de aves

if __name__ == "__main__":
    n=int(input("Ingrese la cantidad de gallinas: "))
    m=int(input("Ingrese la cantidad de gallos: "))
    k=int(input("Ingrese la cantidad de pollitos: "))
    carne_total=(lambda x, y, z: x*6 + y*7 + z*1)(n,m,k)
    print(f"si tenemos {n} gallinas, {m} gallos y {k} pollitos, entonces tenemos un total de {carne_total} Kg de carne.")