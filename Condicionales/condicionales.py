### Conditionals ###

my_condition = False 

if my_condition: # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")   # si es verdadero se ejecuta el print
    
my_condition = 25

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")
    
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 25 ")

print("La ejecución continúa")

my_string = ""      # si una variable str texto esta vacio es false
                                    # por ende no imprime
if not my_string:        # pero si pones not funciona y es true
    print("My cadena de texto no es vacía ")
    
if my_string == "Mi cadena de textooooo":
    print("Estas cadenas de texto coinciden")


