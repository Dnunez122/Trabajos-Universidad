#Busqueda lineal, Si x esta en lista devuelve su posicin en la lista, de lo contrario devuelve -1
x = 0
#Funcion del algoritmo, se recorren todos los elementos en la lista
def busqueda_lineal(list,x):
    i = 0
    

#El ciclo recorre todos los elementos en la lista   
    for z in list:

#Si z es igual a x, devuelve el valor de i 
        if z == x:
            return i 
        i = i+1
#Si salio del ciclo sin haber encontrado el valor, devuelve -1
    return -1 

print(busqueda_lineal([1,4,54,3,0,-1],44))
print(busqueda_lineal([1,4,54,3,0,-1],54))
print(busqueda_lineal([],44))