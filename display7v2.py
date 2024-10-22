digit =[[
'###',
'# #',
'# #',
'# #',
'###',
],
[
' ##',
'  #',
'  #',
'  #',
'  #',
],
[
'###',
'  #',
'###',
'#  ',
'###',
],
[
'###',
'  #',
'###',
'  #',
'###',
],
[
'# #',
'# #',
'###',
'  #',
'  #',
],
[
'###',
'#  ',
'###',
'  #',
'###',
],
[
'###',
'#  ',
'###',
'# #',
'###',
],
[
'###',
'  #',
'  #',
'  #',
'  #',
],
[
'###',
'# #',
'###',
'# #',
'###',
],
[
'###',
'# #',
'###',
'  #',
'###',
]]
numero = int(input("ingresa un numero:"))

def cadena_con_varios_numeros(num):
    num_string = str(num)
    num_list = []
    for n in num_string:
        num_list.append(n)
    #print(num_list)
    return num_list

def imprimir_varios_numeros(lista):
    for n in lista:
        n = int(n)
        renglon = ""
        renglon = (digit[n][0])
        print(renglon, end=" ")
    print("")
    for n in lista:
        n = int(n)
        renglon = ""
        renglon = (digit[n][1])
        print(renglon, end=" ")
    print("")    
    for n in lista:
        n = int(n)
        renglon = ""
        renglon = (digit[n][2])
        print(renglon, end=" ")
    print("")
    for n in lista:
        n = int(n)
        renglon = ""
        renglon = (digit[n][3])
        print(renglon, end=" ")
    print("")
    for n in lista:
        n = int(n)
        renglon = ""
        renglon = (digit[n][4])
        print(renglon, end=" ")


if numero > 9:
    imprimir_varios_numeros(cadena_con_varios_numeros(numero))

else:
    for i in range(5):
            renglon = ""
            renglon = (digit[numero][i])
            print(renglon)