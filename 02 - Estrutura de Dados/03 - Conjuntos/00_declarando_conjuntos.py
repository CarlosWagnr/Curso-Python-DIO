# Sets são uma coleção que não possui objetos repetidos, 
# usamos sets para representar os conjuntos matemáticos ou eliminar itens duplicados de um iterável
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}
