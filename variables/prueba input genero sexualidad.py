# 1. Definimos las opciones que consideramos válidas y serias
generos_validos = ["Masculino", "Femenino", "No binario"]
orientaciones_validas = ["Heterosexual", "Homosexual", "Bisexual", "Asexual"]

# 2. Pedimos los datos al usuario
genero = input("¿Cuál es tu género? (Masculino/Femenino/No binario): ")
orientacion = input("¿Cuál es tu orientación? (Heterosexual/Homosexual/Bisexual/Asexual): ")

# 3. Validamos el género
if genero in generos_validos:
    print("Tu género es:", genero)
else:
    print("❌ Error: El género ingresado no es válido o no es serio.")

# 4. Validamos la orientación sexual
if orientacion in orientaciones_validas:
    print("Tu orientación es:", orientacion)
else:
    print("❌ Error: La orientación ingresada no es válida o no es serio.")
