numero1 = int(input())
numero2 = input()

def cadena_con_varios_numeros(num):
    # Convierte la cadena a una lista de enteros
    return [int(n) for n in num.split()]

def numero_en_lista(num, conjunto):
    # Verifica si el número está en el conjunto
    return num in conjunto

# Convertir la cadena de números una vez y almacenar en un conjunto
numeros_conjunto = set(cadena_con_varios_numeros(numero2))

missingNumber = None
for i in range(numero1):
    if not numero_en_lista(i, numeros_conjunto):
        missingNumber = i

print(missingNumber)
