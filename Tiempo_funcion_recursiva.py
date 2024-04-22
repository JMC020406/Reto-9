import time

def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)  

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  inicio_tiempo = time.time()
  serieFibo = fiboRecursivo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
  fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print(f"El tiempo que se demoro la funcion recursiva fue de {tiempo_total}")