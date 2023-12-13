#Definimos la funcion torres hanoi, con los parametros n,origen,auxiliar y destino
def torres_hanoi(n, origen, auxiliar, destino):
    
    if n == 1:
        print(f"Mover disco 1 desde {origen} hacia {destino}")
        return
    torres_hanoi(n-1, origen, destino, auxiliar)
    print(f"Mover disco {n} desde {origen} hacia {destino}")
    torres_hanoi(n-1, auxiliar, origen, destino)

# Para probar la función con 3 discos en el primer poste ('A'), el segundo poste ('B') como auxiliar y el tercer poste ('C') como destino:
n=int(input("¿Cuantos discos hay? "))
torres_hanoi(n, 'A', 'B', 'C')

