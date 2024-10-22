def read_int(prompt, min, max):
        try:
            prompt = int(prompt)
            if prompt < min or prompt > max:
                print("El valor no está dentro del rango permitido (-10, 10)")
                pass
            else:
                return prompt 
        except ValueError:
            print("Entrada incorrecta")
            read_int(input("Ingresa un número entre -10 a 10: "), -10, 10)



while True:
    v = read_int(input("Ingresa un número entre -10 a 10: "), -10, 10)
    if v != None:
        print("El número es:", v)
