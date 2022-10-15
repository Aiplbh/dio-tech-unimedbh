# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Conjuntos (Dados set)


# Usamos set() para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

print("\n01. Conceito de conjunto da dados - set")
print(  "=======================================\n")

# Exemplo 1
numeros = [1,2,3,4,1,1,3,5,2]

print(f"Para a lista numeros = {numeros} ao aplicar set(numeros) teremos:\n")

print(set(numeros))

# Exemplo 2
fruta = ["abacaxi"]

print ("\nPara a string 'abacaxi' ao se aplicar set('abacaxi') teremos:\n") # {"b", "a", "c", "x", "i"}

print (set('abacaxi'))

print("\nObserve que o metodo set() não garante a ordenação dos elementos\n")

# Exemplo 3
carros = ("palio", "gol", "celta", "palio")

print (f"\nPara a tupla carros = {carros} ao se aplicar set(carros) teremos:\n") # {"gol", "celta", "palio"}

print(set(carros))

print ()

print("Os conjuntos também podem ser criados com {}")

# Ex.:  linguagens = {"python", "java", "python", "javascript"}

# linguagens é um conjunto, assim ao ser impresso só aparecem os elementos
# que não são duplicados.

linguagens = {"python", "java", "python", "javascript"}

print (f"\nPara o conjunto linguagens = {linguagens}, ao se imprimir print(linguagens) teremos:\n")
print (linguagens)

# Conjuntos em Python não suportam indexação e nem fatiamento.
# Caso se queira acessar os seus valores é necessário converter o conjunto para lista.

numeros = {1,2,3,4,6,1,3,4,4,8}

print(f"\nPara acessar o quarto elemento do conjunto" 'numeros = {1,2,3,4,6,1,3,4,4,8}' " devemos primeiro convertê-lo em uma lista\n")

numeros = list(numeros)
print (numeros)
print (numeros[3])




