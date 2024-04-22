#Cuentas en el supermercado:

def cuentas_del_mercado (*quiero_paz_quiero_amor_quiero_dulces_por_favor)->int:
    for dulces in quiero_paz_quiero_amor_quiero_dulces_por_favor:
        vueltas_pago = b - (p*300 + m*3300 + h*350)
    return vueltas_pago

if __name__ == "__main__":
    p= int(input("¿Cuantos panes vas a comprar?: "))
    m= int(input("¿Cuantas bolsas de leche vas a comprar?: "))
    h= int(input("¿Cuantos huevos vas a comprar?: "))
    b= int(input("¿Cuanta plata te dio mamá?: "))

    if cuentas_del_mercado(p,m,h,b) < 0:
        print(f"O rayos, el dinero no es suficiente, te faltaron {-1*cuentas_del_mercado(p,m,h,b)} pesos, ve y busca a mamá para que te de más dinero.")

    elif cuentas_del_mercado(p,m,h,b) > 0:
        print(f"Wow, te sobraron {cuentas_del_mercado(p,m,h,b)} pesos, deberias comprarte un dulce como compensación de tu trabajo.")

    else:
        print(f"Te sobraron {cuentas_del_mercado(p,m,h,b)} pesos, regresa a casa.")    