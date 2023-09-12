# Tupla são estruturas de dados muito parecidas com as listas, a principal diferença é que 
# tuplas são imutáveis enquanto as listas são multáveis.
# Podemos criar tuplas através da classe tuple, ou colocando valores separados por virgulas dentro de parenteses.
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)
