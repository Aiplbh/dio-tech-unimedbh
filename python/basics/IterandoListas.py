# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Listas - Iterando Listas


# 06. Iterando listas
# A forma mais comum de iterar uma lista é usando o for

carros = ["gol", "celta", "palio"]

for carro in carros:
    print (carro)

# ou

for i in carros:
    print (i)



# Função enumerate 
# Retorna o indice do elemento e permite iniciá-lo com valor diferente de [0]

print ("\nMostrando o indice com enumerate\n")
for indice , carro in enumerate(carros):
    print(f"{indice}, {carro}")




seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print (seasons)
print (list(enumerate(seasons)))



