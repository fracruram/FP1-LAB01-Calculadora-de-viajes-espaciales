

distancia_km = int(input("Dane la distancia Tierra-Luna: ")) #384400  # distancia Tierra - Luna
velocidad_kmh = int(input("Dame la velocidad en kmh: ")) #5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")

tiempo_semanas_unic = tiempo_dias // 7
tiempo_semanas = tiempo_dias / 7 
dias_restantes = (tiempo_dias % 7)

print("Tardara ",tiempo_semanas_unic, "semanas y ", dias_restantes, "días.")