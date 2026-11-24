#este es un comentario

my_file = "My code"
print(my_file)

my_int_variable = 5
print(my_int_variable)
#funcion de str
""""
str en numeros le quita el valor de numero y se convierte
en un caracter

str en caracteres en para advertencia
"""
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

print(my_file,str(my_int_variable), my_bool_variable) #Concatenaciones de variable en un print

#funciones del sistema


my_bool_variable = False

my_file = "My litle Ponny"
print(my_file)

#len cuenta los caracteres
print(len(my_file))

print("este es el valor de:", my_bool_variable)

#variables en una sola linea
#          cuidado con poner muchas variables
name, lastname, alias, age = "Danner", "Herbas", "Darko", 20
print("Me llamo", name, "Y me apellido", lastname, "Me conocen como", alias, "y mi edad es", age)

#sistemas de input
""""
name = input('Cual es tu nombre: ')
age = input('Edad: ')

print(name)
print(age)
"""
#cambiamos su tipo
name = 20
age =  "Danner"
print(name)
print(age)

#Forzamos el tipo? rt: no se puede
address: str = "Mi dirrección"
address = 32
print(type(address))

name, lastname, alias, age = "Danner", "Herbas", "Darko", 20
print("Me llamo", name, "Y me apellido", lastname, "Me conocen como", alias, "y mi edad es", age)

