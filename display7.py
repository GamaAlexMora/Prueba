digit =[[
'###',
'# #',
'# #',
'# #',
'###',
],
[
'  #',
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
        for i in range(5):
            renglon = ""
            renglon = (digit[n][i])
            print(renglon)


if numero > 9:
    imprimir_varios_numeros(cadena_con_varios_numeros(numero))

else:
    for i in range(5):
            renglon = ""
            renglon = (digit[numero][i])
            print(renglon)