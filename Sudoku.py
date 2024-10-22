sudoku = input("Ingrese los numeros del sudoku: ")

def dividir_lista_sudoku(lista):
    return [lista[n:n+9] for n in range(0, len(lista), 9)]

def creacion_de_sudoku_en_listas(num):
    num_string = str(num)
    num_list = []
    for n in num_string:
        num_list.append(int(n))
    return dividir_lista_sudoku(num_list)

def imprimir_sudoku(sudoku):
    for l in sudoku:
        print(l)

def encontrar_coordenada_grid(val):
    if val <= 2:
        return 0
    if val <= 5:
        return 1
    else: 
        return 2
    
def obtener_grid_para_celda(x, y, sudoku):
    subgrid_col = encontrar_coordenada_grid(x)
    subgrid_fila = encontrar_coordenada_grid(y)

    grid = []
    for fila in sudoku[subgrid_fila * 3: subgrid_fila * 3 + 3]:
        for col in fila[subgrid_col * 3: subgrid_col * 3 + 3]:
            grid.append(col)
    
    return grid 

def es_posible(x, y, v, sudoku):
    # Revisar fila
    if v in sudoku[y]:
        return False
    
    # Revisar columna
    col = [fila[x] for fila in sudoku]
    if v in col:
       return False
    
    # Revisar sub grid 3x3
    grid3x3 = obtener_grid_para_celda(x, y, sudoku)
    if v in grid3x3:
        return False
    
    return True

def verificacion(x, y, valor, sudoku):
    # Revisar fila
    if sudoku[y].count(valor) > 1:
        return False
    
    # Revisar columna
    col = [fila[x] for fila in sudoku]
    if col.count(valor) > 1:
        return False
    
    # Revisar sub grid 3x3
    grid3x3 = obtener_grid_para_celda(x, y, sudoku)
    if grid3x3.count(valor) > 1:
        return False

    return True

def comprobar_sudoku(sudoku):
    for y in range(9):
        for x in range(9):
            valor = sudoku[y][x]
            if not verificacion(x, y, valor, sudoku):
                return False
    return True

# Solo si se tiene sudoku incompleto con valores = 0 
def resolver_sudoku(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for valor in range(1, 10):
                    if es_posible(x, y, valor, sudoku):
                        sudoku[x][y] = valor
                        resolver_sudoku(sudoku)
                        sudoku[y][x] = 0
                return
    imprimir_sudoku(sudoku)
    return       

# Caso correcto = 295743861431865927876192543387459216612387495549216738763524189928671354154938672
# Caso incorrecto = 195743862431865927876192543387459216612387495549216738763524189928671354254938671

sudoku = creacion_de_sudoku_en_listas(sudoku)
imprimir_sudoku(sudoku)
comprobacion_de_sudoku = comprobar_sudoku(sudoku)
if comprobacion_de_sudoku == True:
    print("Esta correcto el sudoku")
else:
    print("Esta incorrecto el sudoku")
