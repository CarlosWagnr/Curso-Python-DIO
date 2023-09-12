# A String é uma cadeia de caracteres.
nome = "Carlos Wagner"
print(nome.upper())
print(nome.lower())
print(nome.title())

#
print("\n#### Stript -  Eliminando espaços ####")
texto = "  Hello World   "
print(texto)
print(texto.strip() + "!") # Remove todos os espaços
print(texto.lstrip() + "!") # Remove os espaços da esquerda
print(texto.rstrip() + "!") # Remove os espaços da direita

#
print()
menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "-"))

#
print("\n#### JOIN ####")
print("-".join(menu))

# Fazendo for
for letra in menu:
    print(letra, end='-')
    