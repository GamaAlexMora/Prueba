import random

#precios
menoredad = 35
mayoredad = 40

#Descuento
adultomayor = 35.2
estudiante = 36
profesor = 36

boletosdiahoy = 100
boletosvendidos = random.randint(1,99)

boletosdisponibles = boletosdiahoy - boletosvendidos

comprarboletos = False

boletosapagar = ()



Menus = {
    "Menu_inicio": "Buen día, bienvenidos al museo de Antropología e Historia",
    "Menu_boletos": {
        "opcion_1": "Comprar boletos",
        "opcion_2": "Ver precios",
        "opcion_3": "Horarios de apertura"
    },
    "Menu_precios": {
        "Menor de edad": "$35",
        "Mayor de edad": "$40",
        "Adulto mayor (descuento)": "$35.2",
        "Estudiante (descuento)": "$36",
        "Profesor (descuento)": "$36",
        "Regresar": "Regresar al menú de boletos"
    },
    "Menu_horarios": {
        "Lunes a Viernes": "9:00 AM - 5:00 PM",
        "Sábado": "10:00 AM - 6:00 PM",
        "Domingo": "Cerrado",
        "Regresar": "Regresar al menú de boletos"
    }
}

# Ejemplo de cómo podrías imprimir el menú de inicio
def mostrar_menu(menu):
    for key, value in menu.items():
        print(f"{key}: {value}")


#while comprarboletos == False:
print(Menus["Menu_inicio"])
    