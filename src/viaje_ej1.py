distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")


#Tardarías 3.203333333333333 días en llegar.
#Tardarías 3.0 días en llegar.
#Tardarías 3 días en llegar.

# Redondea para abajo, como tiempo en horas es float, el tiempo en dias con la doble // sera
# float, cuando es un entero se produce un entero con un redondeo hacía abajo
#floor division