def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="VolksWagen", modelo="Fox", ano=2015, placa="HYB-1991")
salvar_carro(**{"marca": "BMW", "modelo": "BZ 400", "ano": 2018, "placa": "ICD-9938"})
