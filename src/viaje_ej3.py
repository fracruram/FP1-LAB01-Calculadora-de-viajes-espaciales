edad = int(input("¿Cual es su edad?: "))

if edad < 18:
    print("Debe ser mayor de edad")
else:
    niveL_fisico = int(input("¿Cual es su nivel físico?: "))

    if niveL_fisico < 1 or niveL_fisico > 10:  
        print("Rango no permitido de nivel físico")
    elif niveL_fisico < 5:
        print("Debes estar en mejor forma")
    else:
        print("Listos para despegar")