# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Listas - Criação


# 01. Definição de Listas
# Estruturas que podem armazenar qualquer tipo de objeto demaneira sequencial.
# Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação

# Criação de uma lista com []

pets = ["cachorro", "gato", "papagaio"]
print(pets[0])
print(pets[1])
print(pets[2])

# Criação de uma lista com o construtor list()
# No caso de uma string cada letra da palavra será um elemento da lista

letras = list("python")
print(letras)
print(letras[0])
print(letras[1])
print(letras[2])
print(letras[-3])
print(letras[-2])
print(letras[-1])

# No caso de se criar uma lista com o método construtor list usaremos o range:

numeros = list(range(10))
print(numeros)



