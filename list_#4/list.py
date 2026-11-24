### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35,24,52,45,30,30,34,34]   ###forma de agrupar datos

print(my_list)
print(len(my_list))           ##"len" contar datos en list

my_other_list = [20, 1.71, "Danner", "Herbas"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_list.count(30))  ##"count" cuenta elementos dentro de la propia lista

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)
#print(my_list - my_other_list)
print(type(my_list))

my_other_list.append("Darko") ##con operacion ".append" se va al final
print(my_other_list)

my_other_list.insert(1, "Negro") #con 'insert' a introducido un dato donde seleccioné
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_other_list.remove("Rojo") # remueve
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop()       #borra el ultimo dato de la lista
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)    ##elimina el dato de la lista pero lo guarda en otra variable
print(my_list)

del my_list[1]          ##del elimina por indice
print(my_list)

my_new_list = my_list.copy()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)


my_list = "Hola Python"
print(my_list)
print(type(my_list))




