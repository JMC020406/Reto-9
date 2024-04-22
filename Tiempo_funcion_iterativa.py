import time

def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo


if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  inicio_tiempo = time.time()
  serieFibo = fibo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
  fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print(f"El tiempo que se demoro la funcion iterativa fue de {tiempo_total}")