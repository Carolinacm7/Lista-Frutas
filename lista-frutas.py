frutas=["Manzana","Pera","mango","papaya","uvas","granadilla"]
#añadir informacion a la lista
frutas= frutas +["nizpero"]
#para eliminar toda la informacion de la lista
#frutas=clear()
#para copiar una lista
lista2=frutas.copy()
#para contar las frutas frutas.count()para buscar cuantas veces retorna un numero ejm uvas 

print(frutas)
print(cant)
print("lista2")
#cambiar a mayuscula la primera letra
for indice in range(len(frutas)):
    fruta=frutas[indice]
    frutas[indice]= fruta.capitalize()#upper(apple)->APPLE Lower(APPLE)->apple Capitalize(APPLE)->Apple
cant = frutas.count("Uvas")
#insertar una fruta en una posicion diferente
frutas.insert(3,"Uchuva")
frutas.append("Sandia")
#buscar y agregar info 
busco=frutas.idex("granadilla")
fruta[busco]="Aguacate"
fruta.insert(busco,"uchuva")
#para remover o quitar una fruta 

#para organizar alfabeticamnete
frutas.sort()

