conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # Conjunto de A está em B True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # Conjunto de B está em A False
print(resultado)
