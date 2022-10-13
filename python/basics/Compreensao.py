# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Listas - Compreensao de lista

# Usado como filtro de uma lista original

# Recurso que oferece uma sintaxe mais curta quando você deseja:

# - criar uma nova lista com base nos valores de uma lista existente (filtro)
# - gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

# Ex.: Extrair os numeros pares da lista numeros[] abaixo e colocá-los na lista pares []

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)

print("\nSem usar comprehension\n")
print (pares)

# Embora o método acima funcione ele necessida da criação de duas listas e várias linhas de código

# O mesmo resultado pode ser obtido com o metodo comprehension como abaixo exemplificado:

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2== 0]

# 'Coloque na lista pares[] o numero iterado durante a varredura da lista numeros[] caso ele seja par (%2 == 0) '

print("\nUsando comprehension\n")
print (pares)


# Outro exemplo sem if:
# criar uma nova lista quadrado[] com os números da lista numeros[] elevados a 2

# tradicional:

numeros = [1, 30, 21, 2, 9, 65, 34]

quadrado = []

for numero in numeros:
    quadrado.append(numero**2)

print("\nSem usar comprehension\n")
print (quadrado)


quadrado = [numero **2 for numero in numeros]

print("\nUsando comprehension\n")
print (quadrado)

