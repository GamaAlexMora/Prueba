palabra_oculta = input("Ingrese la palabra oculta: ")
grupo_de_letras = input("Ingrese el grupo de letras: ")

def dividir_palabra(palabra, grupo):
    palabra = palabra.upper()
    grupo = grupo.upper()
    for i in palabra:
        fnd = grupo.find(i)
        if fnd != -1:
            pass
        else:
            return False
    return True
    

if dividir_palabra(palabra_oculta, grupo_de_letras) == True:
    print("Se encontraron todas las letras")
else: 
    print("No se encontraron todas las letras")