#Establezco el array
num = [2,3,5,1,4,3,6,7,9,5,8]

#Aqui se recorre el codigo y se pregunta si la longitud de la lista es igual al de numeros unicos del array.
#De igual manera se puede usar la funcion set()
repetidos = []
for i in range(len(num)):  #de esta variable se agrega al array, aunque en realidad tmb se puede usar la otra.
    for j in range(len(num)):   
        if i != j:
            if num[i] == num[j] and num[i] not in repetidos:  # Se declara que si i y j son = no se agregada nada a la variable de repetidos.
             repetidos.append(num[i]) #append = adjuntar, entonces se adjunta los numeros de la variable "i" al array de repetidos
            print(repetidos)


#odie este ejericio.