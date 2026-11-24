### Tuples ###
#formas de definir una tupla
my_tuple = tuple()
my_other_tuple = ()
#

my_tuple = (20, 1.71, "Danner", "Herbas", "Danner")


print(my_tuple)
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[6]) IndexError

print(my_tuple.count("Danner")) #encontró dos danner y lo escribe
print(my_tuple.index("Herbas"))
print(my_tuple.index("Danner")) #.index() se utiliza para localizar la posición (el índice) de un elemento específico dentro de una estructura de datos

#my_tuple[5] = 1.80

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

