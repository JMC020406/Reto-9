#Area y perimetro de dos circulos y un rectangulo:

import math

def perimetro_figura (*a_los_patos_no_les_gusta_el_pan)->float:
    for pan in a_los_patos_no_les_gusta_el_pan:
        calculo_perimetro = ((2*a + 2*b) + (2*(2*math.pi*r)))
    return calculo_perimetro

def area_figura (*a_los_patos_no_les_gusta_el_pan)->float:
    for pan in a_los_patos_no_les_gusta_el_pan:
        calculo_area = ((a*b)+(2*(math.pi*r**2)))
    return calculo_area

if __name__ == "__main__":
    a=float(input("Ingrese la altura del rectangulo: "))
    b=float(input("ingrese el ancho del rectanguro: "))
    r=float(input("Ingrese el radio de los circulos: "))

    print(f"El area de la figura con un rectangulo de {a} de altura, {b} de ancho y dos circulos de {r} de radio, es de {area_figura(a, b, r)} y su perimetro es de {perimetro_figura(a, b,r)}")
    
