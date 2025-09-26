distancia = int(input("¿Que distancia se va a recorrer?"))
paradas = distancia // 150000


for i in range(paradas):
    print("Parada en el kilometro:",150000 * i)

print("Total de paradas: ",i)