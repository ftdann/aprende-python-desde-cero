### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error ")
except:
#   se ejecuta si se produce una excepción
    print("Se ha producido un error")
    
# try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error ")
except:
    print("Se ha producido un error")
else:# Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:# Opcional
    # Se ejecuta Siempre
    print("la ejecución continua")
    
# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error ")
except ValueError:
#   se ejecuta si se produce una excepción
    print("Se ha producido un error")

