def potencia(e : int )-> int:
  if e == 0: 
    return 1
  else:
    return base*potencia(e-1)

if __name__ == "__main__":
  base = int(input("Ingrese base: "))
  exp = int(input("Ingrese exponente: "))
  resultado = potencia(exp)
  
  print(f"La potencia de {base}^{exp} es {resultado}")