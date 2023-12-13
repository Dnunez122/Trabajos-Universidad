#Programa para encontrar el factoriasl del numero dado 

def factorial(n):
    #Ver si el numero 
    #Si es 1 o 0 encontes 
    #retornar 1 
    #mientras tanto return 
    #facotiarl
    if (n==1 or n==0):
        return 1
    else:
        return (n*factorial(n-1))
    
#Driver code
num = 5;
print("number: ", num)
print("Factorial : ",factorial(num))  