### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional 
    print("Mi condición es mayor o igual que 10")

print("la ejecucion continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene la ejecución")
        break
    print(my_condition)
    
print("La ejecución continúa")

# For

my_list = [20, 12, 12, 22, 32, 42, 52, 62]

for element in my_list:
    print(element)
    
'''etc for imprime una linea por cada elemento que tengas
asi como las List, tuplas, diccionarios y sets'''

my_tuple = (35, 1.77, "Danner", "Herbas", "Mejia")

for element in my_tuple:
    print(element)

my_set = {"Danner", "Herbas", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Danner", "Apellido": "Herbas", "Edad": 20, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")    
