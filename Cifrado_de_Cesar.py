# Cifrado César.
text = input("Ingresa tu mensaje: ")
numero_de_cifrado = input("Ingresa el numero de cifrado: ")
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    if char == "Z":
        char = "A"
        code = ord(char) + int(numero_de_cifrado) - 1
        cipher += chr(code)
    elif char == "z":
        char = "a"
        code = ord(char) + int(numero_de_cifrado) - 1
        cipher += chr(code)
    else:
        code = ord(char) + int(numero_de_cifrado)
        cipher += chr(code)

print(cipher)