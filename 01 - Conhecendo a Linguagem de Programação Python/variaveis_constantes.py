# Variáveis são utilizadas para armazenar valores que podem sofrer alterações 
# no decorrer da execução do programa. O padrçao de nomes deve ser snake case
nome_usuario = "Wagner"
idade_usuario = 28
print(f"Meu nome é {nome_usuario} e eu tenho {idade_usuario} ano(s) de idade.")

nome_usuario, idade_usuario = "Sinaria", 25
print(f"Meu nome é {nome_usuario} e eu tenho {idade_usuario} ano(s) de idade.")

limite_saque_diario = 1000

print(f"Limite de saque é de R$ {limite_saque_diario:.2f}")

# Constantes são utilizadas para armazenar valores que permanece imutável 
# até o final da execução do programa e são utilizadas em nome em maiuscula.
BRAZILIAN_STATES = ["MA", "PA", "SC"] # constante

print(BRAZILIAN_STATES)