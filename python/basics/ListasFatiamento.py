# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Listas - Fatiamento

# Numa lista podemos extrair um conjunto de valores de uma sequência. Isso chama-se fatiamento.

# lista = [indice_inicial : indice_final : salto]

lista = ["p", "y", "t",  "h",  "o",  "n"]

print (lista [2:])    #>>> ["t",  "h",  "o",  "n"]

print (lista [:2])    #>>> ["p", "y"]

print (lista [1:3])   #>>> ["y", "t"]

print (lista [::])    #>>> ["p", "y", "t",  "h",  "o",  "n"]

print (lista [0:3:2]) #>>> ["p", "t"]

print (lista [::-1])  #>>> ["n", "o", "h",  "t",  "y",  "p"]

