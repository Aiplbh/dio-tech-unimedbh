# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Listas - Métodos da Classe List()


# 01. append()
# Adiciona um objeto ao final da lista

lista = []
lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista)  # >>> [1, "Python", [40,30,20]]


# 02. clear()
# Apaga toda a lista

lista = [1, "Python", [40,30,20]]
lista.clear()

print(lista)  # >>> []


# 03. copy()
# Copia os elementos de uma lista preservando os elementos originais

lista1 = [1, "python", [40,30,20]]

lista2 = lista1.copy()

print(id(lista1), id(lista2))

# 04. count()
# Conta quantas vezes um elemento aparece na lista

cores = ["vermelho", "azul", "verde", "azul", "branco", "verde", "verde"]

print(cores.count("vermelho")) # 1
print(cores.count("azul"))     # 2
print(cores.count("verde"))    # 3
print(cores.count("branco"))   # 1
print(cores.count("preto"))    # 

# 05. extend()
# Usada para concatenar listas

linguagens = ["python", "js", "c"]

print(linguagens) # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens) # ["python", "js", "c", "java", "csharp"]

# 06. index()
# Retorna o indice de um elemento. Neste caso é passado o nome do elemento como parâmetro
# No caso de haverem dois elementos iguais apenas o primeiro indice será retornado

linguagens = ["python", "js", "c", "java", "csharp", "js"]

print(linguagens.index("java"))   # 3
print(linguagens.index("python")) # 0
print(linguagens.index("js"))     # 1  (embora haja outro elemento js com indice[5], só or primeiro será retornado )


# 07. pop()
# Retira o último elemento da lista. Em conjunto com append() é possível 
# se implementar uma estrutura de dados como a pilha (LIFO).
# No caso do pop(n) é possível retirar um elemento do meio da pilha

linguagens = ["python", "js", "c", "java", "csharp"]
print (linguagens)

linguagens.pop()  # csharp
print ("\nRetirado o elemento 'csharp'")
print (linguagens)

linguagens.pop()  # java
print ("\nRetirado o elemento 'java'")
print (linguagens)

linguagens.pop()  # c
print ("\nRetirado o elemento 'c'")
print (linguagens)

linguagens.pop(0) # python
print ("\nRetirado o elemento 'linguagens[0]'")
print (linguagens)

# 08. remove()
# Remove um elemento da lista. Diferentemene do pop() que recebe o indice, o 
# remove() recebe o nome do elemento como parametro.
# Caso hajam elementos com mesmo nome, apenas a primeira ocorrência será retornada.

print("\nRemovendo elementos com remove()")
linguagens = ["python", "js", "c", "java", "csharp", "c"]
print(linguagens)
print("\nRemovendo o elemento 'c' com remove('c')")
linguagens.remove("c")
print(linguagens)      # ["python", "js", "java", "csharp", "c"]



# 09. reverse()
# Usado para fazer o espelhamento de uma lista

print("\n09. reverse()\n")
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens)

print("\nAplicando o método linguagens.reverse()\n")

linguagens.reverse()
print(linguagens)        # ["csharp", "java", "c", "js", "python"]
print("")

# 10. sort()
# Implementa um algoritmo de ordenação. Aceita ordenação crescente / decrescente, por ordem alfabética
# ou por ordem de comprimento dos objetos usando a função anonoma lambda

print("\n10. sort()")
linguagens = ["python", "js", "c", "java", "csharp"] 
print(f'\nOrdenar a lista linguagens = {linguagens} com sort()\n')
linguagens.sort()                                      
print (linguagens)


linguagens = ["python", "js", "c", "java", "csharp"]
print(f'\nOrdenar a lista linguagens = {linguagens} com sort(reverse = True)\n')
linguagens.sort(reverse = True)                                      
print (linguagens)


linguagens = ["python", "js", "c", "java", "csharp"]
print(f'\nOrdenar a lista linguagens = {linguagens} com sort(key=lambda x: len(x)) [comprimento]\n')
linguagens.sort(key=lambda x: len(x))                                    
print (linguagens)


linguagens = ["python", "js", "c", "java", "csharp"]
print(f'\nOrdenar a lista linguagens = {linguagens} com sort(key=lambda x: len(x)) [comprimento] e reverse\n')
linguagens.sort(key=lambda x: len(x), reverse=True)                                    
print (linguagens)




# 11. len()
# Retorna o tamanho do elemento ou da lista


print("\n11. len()")
linguagens = ["python", "js", "c", "java", "csharp"] 
print(f'\nMostrar o tamanho da lista linguagens = {linguagens} com len()')
print (len(linguagens))

linguagens = ["python", "js", "c", "java", "csharp"] 
print(f'\nMostrar o tamanho do elemento [0] da lista linguagens = {linguagens} com len(linguagens[0])')
print (len(linguagens[0]))

# 12. sorted()
# Igual ao sort(). No entanto o sort() é um método built-in e o sorted é uma função.