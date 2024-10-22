palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

def verificar_anagrama(palabra1, palabra2):
    palabra1 = palabra1.upper()
    palabra2 = palabra2.upper()
    palabra1 = ''.join(sorted(palabra1))
    palabra2 = ''.join(sorted(palabra2))
    if palabra1 == palabra2:
        return True
    else: 
        return False
    
anagrama = verificar_anagrama(palabra1, palabra2)
if anagrama == True:
    print("Es un anagrama")
else:
    print("No es un anagrama")