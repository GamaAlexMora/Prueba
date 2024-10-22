numero1 = int(input())
numero2 = input()


def cadena_con_varios_numeros(num):
    num_string = str(num)
    num_list = []
    numero = ""
    for n in num_string:
        if n != " ":
            numero = numero + n
        else:
            num_list.append(int(numero))
            numero = ""
            pass
    return num_list

def numero_en_lista(num, lista):
    return num in lista


for i in range(numero1):
    if numero_en_lista(i, cadena_con_varios_numeros(numero2)) == True:
        pass
    else:
        missingNumber = i

print(missingNumber)