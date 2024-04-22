#Volumen y area superficial de una esfera y un cono:

import math

def volumen_figuras (*los_unicornios_deberian_existir_xd)->float:
    for cuerno in los_unicornios_deberian_existir_xd:
        calculo_volumen = (((3/4)*math.pi*re**3)+((h/3)*math.pi*rc**2))
    return calculo_volumen

def area_figuras (*los_unicornios_deberian_existir_xd)->float:
    for cuerno in los_unicornios_deberian_existir_xd:
        calculo_area_superficial = ((4*math.pi*re**2)+(((math.pi)*rc*(rc**2+h**2))+(math.pi*rc**2)))
    return calculo_area_superficial

if __name__ == "__main__":
    re = float(input("Ingrese el radio de la esfera: "))
    rc = float(input("Ingrese el radio del cono: "))
    h = float(input("Ingrese la altura del cono: "))

    print(f"La esfera de radio {re} junto al cono de radio {rc} y altura {h} tienen un volumen de {volumen_figuras(re, rc, h)} y un area superficial de {area_figuras(re, rc, h)}.")
    