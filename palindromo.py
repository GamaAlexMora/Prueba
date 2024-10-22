sentence = input("Ingrese una oracion o palabra: ")

def ordenar_palabras(palabra):
    letras = ""
    letras_inversas = ""
    for i in range(len(palabra)):
        if palabra[i].isspace():
            pass
        elif palabra[i].isalpha():
            letras = letras + palabra[i]
    for letter in reversed(letras):
        letras_inversas = letras_inversas + letter
    if letras_inversas.upper() == letras.upper():
        return True
    else:
        return False

if ordenar_palabras(sentence) == True:
    print("Es un palindromo")
else:
    print("No es un palindromo")