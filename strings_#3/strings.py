### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)
  
my_new_line_string = "Este es un String \n con salto de linea"
print(my_new_line_string)

my_tab_line_string = "\tEste es un String con tabulacion"
print(my_tab_line_string)

my_scape_line_string = "\\tEste es un String \\n escapado"
print(my_scape_line_string)

# Formateo  ##lo aprenderé más adelante cuando formatee datos

name, surname, age = "Danner", "Fernando", 20

print("Mi nombre es {} {} y mi edad es {}". format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))


# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) #pone la primera letra en mayuscula
print(language.upper())      #pone todo en mayuscula
print(language.count("t"))   #cuenta las letra en especifico las "t" ejem
print("1".isnumeric())       #Es un numero "1" True. Es un numero "Python" False.
print(language.lower())      #pone todo en minuscula
print(language.upper().isupper())
print(language.startswith("py")) #busca la palabra


