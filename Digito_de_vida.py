fecha = (input("Ingresa tu fecha de nacimiento en el formato AAAAMMDD: "))

def lista_numeros(num):
    num_string = str(num)
    num_list = []
    for n in num_string:
        num_list.append(int(n))
    return num_list

def sumar_numeros(lista):
    suma = 0
    for l in lista:
        suma += l
    if suma > 9:
        suma = sumar_numeros(lista_numeros(suma))
    return suma

number_list = lista_numeros(fecha)
print(sumar_numeros(number_list))

