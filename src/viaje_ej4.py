for i in range(0,60000,10000): #stop, start, step
    if i > 0:
        tiempo_horas = 225000000 / i
        tiempo_dias = tiempo_horas / 24
        print("Velocidad:",i,"-> Tiempo:",tiempo_dias)

        tiempo_semanas_unic = tiempo_dias // 7
        tiempo_semanas = tiempo_dias / 7 
        dias_restantes = (tiempo_dias % 7)

        print("Tardara ",tiempo_semanas_unic, "semanas y ", dias_restantes, "días.")
    