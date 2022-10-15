# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Métodos da Classe Set


# Metodos da classe Set()

# union {}

print("Método Union ")
print("=============")

conjunto_a = {1,2,3}
conjunto_b = {3,4,6}

print("A união do conjunto_a = "'{1,2,3}' " e o conjunto_b = "'{3,4,6}'" será\n")

print("conjunto_a.union(conjunto_b)")
print (conjunto_a.union(conjunto_b))

print()

# intersection {}

print("Método Intersection")
print("===================")

conjunto_a = {1,2,3}
conjunto_b = {3,4,6}

print("A interseção do conjunto_a = "'{1,2,3}' " e o conjunto_b = "'{3,4,6}'" será\n")

print("conjunto_a.intersection(conjunto_b)")
print (conjunto_a.intersection(conjunto_b))

print()

print("Método difference")
print("=================")

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print("A diferença do conjunto_a = "'{1,2,3}' " e o conjunto_b = "'{2,3,4}'" será\n")

print("conjunto_a.difference(conjunto_b)") # Tudo que está no conjunto_a que não está no conjunto_b
print (conjunto_a.difference(conjunto_b))

print("\nA diferença do conjunto_b = "'{2,3,4}' " e o conjunto_a = "'{1,2,3}'" será\n")

print("\nconjunto_b.difference(conjunto_a)") # Tudo que está no conjunto_b que não está no conjunto_a
print (conjunto_b.difference(conjunto_a))

print()


print("Método symmetric_difference")
print("===========================")

# União de A e B menos a intersecção A e B


conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print("A diferença do conjunto_a = "'{1,2,3}' " e o conjunto_b = "'{2,3,4}'" será\n")

print("conjunto_a.difference(conjunto_b)") # Tudo que está no conjunto_a menos o que está no conjunto_b: sobrou {1}
print (conjunto_a.difference(conjunto_b))

print("\nA diferença do conjunto_b = "'{2,3,4}' " e o conjunto_a = "'{1,2,3}'" será\n")

print("\nconjunto_b.difference(conjunto_a)") # Tudo que está no conjunto_b menos o que está no conjunto_a: sobrou {4}
print (conjunto_b.difference(conjunto_a))

print()



# A diferença simétrica é a união menos a interseção de dois conjuntos

conjunto_a = {1, 2, 3}
print("conjunto_a")

conjunto_b = {2, 3, 4}
print("conjunto_b")

print("conjunto_a.symmetric_difference(conjunto_b)")
print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}


# Contem e está contido

# Essa operação é obtida por dois métodos cujo retorno é um boolean

# Está contido ---> issubset()

print("\nMétodo issubset() ou está contido")
print("==================================")

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(f"conjunto_a = {conjunto_a}")
print(f"conjunto_b = {conjunto_b}")


conjunto_aEstaContidoEmConjunto_b = conjunto_a.issubset(conjunto_b) # True: A está contido em B ?
conjunto_bEstaContidoEmConjunto_a = conjunto_b.issubset(conjunto_a) # False B não está contido em A ?

print("\nConjunto A está contido no conjunto B ? ")
print(conjunto_aEstaContidoEmConjunto_b)

print("\nConjunto B está contido no conjunto A ? ")
print (conjunto_bEstaContidoEmConjunto_a)

# Contém ----> issuperset()

print("\nMétodo issuperset() ou contem")
print("==================================")

#conjunto_a.issuperset(conjunto_b) # False: A contém B
#conjunto_b.issuperset(conjunto_a) # True : B contem A

conjunto_aContemConjunto_b = conjunto_a.issuperset(conjunto_b) # False: A contém B ?
conjunto_bContemConjunto_a = conjunto_b.issuperset(conjunto_a) # True : B contem A ?

print("\nConjunto A contem conjunto B ? ")
print(conjunto_aContemConjunto_b)

print("\nConjunto B contem conjunto A ? ")
print (conjunto_bContemConjunto_a)


# Método para verificar se dois conjuntos são disjuntos (retorna bolean)

print("\nMétodo isdisjoint()")
print( "====================")

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(f"\nSejam os conjuntos a = {conjunto_a} , b = {conjunto_b} e c = {conjunto_c}\n")

print("Verificando se conjuntos são disjuntos\n")

print("Conjunto A e B são disjuntos ? (conjunto_a.isdisjoint(conjunto_b)")
print(conjunto_a.isdisjoint(conjunto_b))  # True

print("Conjunto A e C são disjuntos ? (conjunto_a.isdisjoint(conjunto_c)")
print(conjunto_a.isdisjoint(conjunto_c)) # False

# Método add()
# Adiciona elementos não repetidos a um conjunto


print("\nMétodo add()")
print( "=============")

sorteio = {1, 23}
print(f"Considere o conjunto sorteio = {sorteio}")

print("\nAdicionando o elemento 25 com sorteio.add(25): ")
sorteio.add(25)
print (f"sorteio = {sorteio}") # {1, 23, 25}

print("\nAdicionando o elemento 42 com sorteio.add(42): ")
sorteio.add(42) 
print (f"sorteio = {sorteio}") # {1, 23, 25, 42}

print("\nAdicionando novamente o elemento 25 com sorteio.add(25): ")
sorteio.add(25)
print (f"sorteio = {sorteio}") # {1, 23, 25, 42}

print("\nObserve que o elemento 25 não foi adicionado duas vezes!\n")
 

print("\nMétodo clear()")
print( "==============\n")

sorteio = {1, 23}
print(f"Considere o conjunto sorteio = {sorteio}")

print("\nLimpando o conjunto com sorteio.clear()")
sorteio.clear()

print (f"\nsorteio = {sorteio}")





print("\nMétodo discard()")
print( "=================\n")

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(f"Considere o conjunto numeros =  {numeros}\n")

print("Removendo o elemento {1} com mumeros.discard(1)")
numeros.discard(1)
print(f"numeros = {numeros}\n")


print("Removendo o elemento  {5} com mumeros.discard(5)")
numeros.discard(5)
print(f"numeros = {numeros}\n")

print("Removendo o elemento inexistente {45} com mumeros.discard(45)")
numeros.discard(45)
print(f"numeros = {numeros}\n")

print("*** Mesmo sendo inexistente o Python não dá erro com discard() ***")



print("\nMétodo pop() - retira um elemento")
print( "=========================================\n")

print("numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}\n")
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print (f"numeros = {numeros}") 

print("\nRemovendo um elemento com numeros.pop()")
numeros.pop() # 0
print (f"numeros = {numeros}") 

print("\nRemovendo outro elemento com numeros.pop()")
numeros.pop() # 0
print (f"numeros = {numeros}") 

print("\nRemovendo outro elemento com numeros.pop()")
numeros.pop() # 0
print (f"numeros = {numeros}") 

print("\nRemovendo outro elemento com numeros.pop()")
numeros.pop() # 0
print (f"numeros = {numeros}\n") 


print("\nMétodo remove() - retira um elemento definido")
print( "==============================================\n")


print("numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}\n")
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print (f"numeros = {numeros}") 

print("\nRemovendo um elemento com numeros.remove(7)")
numeros.remove(7) # 0
print (f"numeros = {numeros}") 

print("\nRemovendo outro elemento com numeros.remove(2)")
numeros.remove(2) # 0
print (f"numeros = {numeros}\n") 

print("ATENÇÃO !!!  se o elemento não existir ocorrerá um ERRO\n")


print("\nMétodo len() - retorna o numero de elementos do conjunto")
print( "=========================================================\n")

print("numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}\n")
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print (f"numeros = {numeros}") 

print(f"\nAplicando o método  len(numeros) obtemos: ", (len(numeros)))

print()


print("\nMétodo in() - verifica a existencia de um elemento no conjunto e retorna um boolean")
print( "===================================================================================\n")

print("numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}\n")
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print (f"numeros = {numeros}") 

print("\nPesquisando se existe o numero 1 no conjunto com '1 in numeros' resulta em: ")
existe_1 = 1 in numeros # True
print (existe_1)

print("\nPesquisando se existe o numero 10 no conjunto com '10 in numeros' resulta em: ")
existe_10 = 10 in numeros # False
print (existe_10)

print()
