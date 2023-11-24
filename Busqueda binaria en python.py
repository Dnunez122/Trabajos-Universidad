#Este es el vector que el algoritmo usara para la busqueda
vector = [3,5,8,9,10,22,45,500,900,4253]

#La variable puntero sera el inicio del vector que es 0
puntero = 0

#VercorLen es el longitud del vector 
vectorLen = len(vector)

#la variable "encontrado" cambiara su valor, asi el algoritmo sabra que hacer
encontrado = False

#Le pedimos al usuario una entrada de un numero entero 
numero = int(input("Ingrese el dato que desea buscar: "))

#Creamos un bucle que no se detenga hasta que encontrado sea diferente de false y que puntero sea menor o igual que vectorlens

while not(encontrado) and puntero <= vectorLen:
    mitad = int((puntero+vectorLen)/2) #creamos variable mitad
    print("EL dato se encuentra en la posicion ",str(mitad+1)) #mostrasmo mensaje con la posicion del dato
    print(vector)
    break
else:
    print("El dato no se encontró ")
