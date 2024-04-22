#Prestamos con intereses

if __name__ == "__main__":
    c=int(input("¿Cuanta plata tiene en su prestamo?: "))
    i=int(input("¿Que porcentaje de intereses se le esta aplicando a su prestamo?: "))
    t=int(input("Cuantos meses van a trancurrir?: "))
    total_final_plata = (lambda x, y, z : x*(1 + y/100)**z)(c, i, t)
    print(f"Tu prestamo de {c} pesos con un interes del {i}%, terminara siendo {total_final_plata} pesos, si transcuren {t} meses.")