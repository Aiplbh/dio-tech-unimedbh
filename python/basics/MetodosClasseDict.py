# 22:38 12/10/2022
# Módulo: Aprendendo a usar dicionario em Python
# Instrutor: Guilherme Arthur de Carvalho

# 01. Definição de dicionario

# Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário.
# Em um dicionario, para ser chave o elemento deve ser imutável.

# 02. Criação de Dicionario
# Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas.

print("Criação de um dicionario")
print("========================\n")

print("Criando o dicionario usando chaves | pessoa = {'nome': 'Guilherme', 'idade': 28}\n")
pessoa = {'nome': 'Guilherme', 'idade': 28}
print(f"pessoa = {pessoa}")
print()


print("Criando o dicionario usando o construtor dict() | pessoa = dict(nome='Guilherme', idade=28)\n")
pessoa = dict(nome="Guilherme", idade=28)
print(f"pessoa = {pessoa}")
print()


print("Adicionando uma nova chave ao  dicionario | pessoa['telefone'] = '3333-1234')\n")
pessoa["telefone"] = "3333-1234"   # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(f"pessoa = {pessoa}")
print()


print("Acessando os dados de um dicionario")
print("===================================\n")


dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(f"Considere o dicionário dados = {dados}\n")

print("Obtendo o nome de dados usando dados['nome']:")
print(f"dados['nome'] ==> {dados['nome']}\n") 

print("Obtendo o nome de dados usando dados['nome']:")
print(f"dados['telefone'] ==> {dados['telefone']}\n") 


print("Alterando o nome em dados usando dados['nome'] = 'Maria':")
dados['nome'] = 'Maria'
print(f"dados['nome'] ==> {dados['nome']}\n") 


print("Alterando a idade em dados usando dados['idade'] = '18':")
dados["idade"] = 18
print(f"dados['idade'] ==> {dados['idade']}\n") 

print("Alterando o telefone em dados usando dados['telefone'] = '9988-1781':")
dados["telefone"] = "9988-1781"
print(f"dados['telefone'] ==> {dados['telefone']}\n") 

print("Mostrando o dicionario após alterações: ")
print(f"dados = {dados}\n")

# Dicionarios aninhados

# Dicionários podem armazenar qualquer tipo de objeto Python com o valor, desde que a chave para esse valor se ja um objeto imutável como (stringsenúmeros).

print("Dicionários aninhados")
print("======================\n")

# contatos = {
 #   "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
  #  "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
   # "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    #"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},}
    
contatos = {
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
  "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
  "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
  "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},}

print(contatos)

print("Para acessar o telefone do usuario 'giovanna@gmail.com deve-se enviar o seguinte comando")
print("contatos['giovanna@gmail.com']['telefone']")
print(contatos['giovanna@gmail.com']['telefone'])

print("\nIterando um dicionário com for")
print("==============================\n")

for chave in contatos:
    print(chave, contatos[chave])


print("\nIterando um dicionário com for..items()")
print("========================================\n")

for chave, valor in contatos.items():
    print(chave, valor)

print()

print("Copiando um dicionario com copy()")
print("=================================\n")

copia_de_contatos = contatos.copy()
print (f"Cópia de contatos: copia_de_contatos = {copia_de_contatos}")


print("\nLimpando um dicionário com clear()")
print("==============================\n")


print ("Conteudo antes do clear(): ")
print(contatos)

contatos.clear()
print (f"Dicionario contatos limpo com contatos.clear()\n")
print ("Conteudo depois do clear(): ")
print(contatos)
print()


print("\nMetodo fromkeys() - Cria chaves")
print("==================================\n")

print("\n1) Criando um dicionario apenas com as chaves (campo valor = none):")

print("\ndict.fromkeys(['nome', 'telefone'])")

print(f"\nResultado ===> {dict.fromkeys (['nome','telefone'])}")

print("\n2) Criando um dicionario apenas com as chaves (campo valor definido pelo metodo):")

print("\ndict.fromkeys(['nome', 'telefone'],'vazio')")

print(f"\nResultado ===> {dict.fromkeys (['nome','telefone'],'vazio')}")

print()


# Metodo get()
# Esse método permite obter os valores a partir de uma chave fornecida.
# Sem usar get o Python pode retornar uma excessão 'Key error' caso a chave não exista
# Com get() o retorno será 'none' ou um dicionario vazio caso isso seja especificado

print("\nMetodo get() - Acessar dados do dicionario")
print("============================================\n")

print("Considerando o dicionário abaixo: \n")
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(f"contatos = {contatos}")
print ("\nAo tentar obter uma chave inexistente com contatos['chave'] tem-se um erro: KeyError: 'chave'\n")
#print (contatos['chave'])

print(f"Usando o get() não há erro: contatos.get('chave') ===> {contatos.get('chave')}")

print("\nRetornando um dicionario vazio, caso a chave de pesquisa não exista: \n")

print(f"contatos.get('chave', '{'{}'}') ===> {contatos.get('chave',{})}")

print("\nRetornando o resultado de uma pesquisa com chave existente:\n")

print(f"contatos.get('guilherme@gmail.com', '{'{}'}') ===> {contatos.get('guilherme@gmail.com',{})}")

print()

# Metodo item() retorna uma lista de tuplas

print("\nMetodo items() - retorna os itens do dicionario")
print("=================================================")

print("\nImprimindo itens do dicionário contatos com contatos.items():\n")

print(contatos.items())

print("\nMetodo keys() - retorna soment as chaves do dicionario")
print("=========================================================")

print("\nImprimindo itens do dicionário contatos com contatos.keys():\n")

print(contatos.keys())


print("\nMetodo pop() - remove as chaves do dicionario")
print("===============================================\n")

print(f"contato = {contatos}")

print("\nRemovendo a chave do dicionário 'contatos' com contatos.pop(''guilherme@gmail.com''):\n")

print(f"contatos = {contatos.pop('guilherme@gmail.com')}")

print("\nCaso a chave não seja encontrada retornar mensagem: 'Chave não encontrada'") 

print("\nRemovendo novamente chave do dicionário 'contatos' com contatos.pop('guilherme@gmail.com','Chave não encontrada'):\n")

print(f"contatos = {contatos.pop('guilherme@gmail.com','Chave não encontrada')}")

print()


print("\nMetodo popitem() - remove as chaves uma a uma do dicionario")
print("=============================================================\n")

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

print(f"contato = {contatos}")

print("\nRemovendo a chave do dicionário 'contatos' com contatos.popitem():\n")

print(f"contatos = {contatos.popitem()}\n")

print(f"contato = {contatos}")

print("\nRemovendo novamente chave do dicionário 'contatos' com contatos.pop() gera-se um erro:\n")

#print(f"contatos = {contatos.popitem ()}")

print()
# Metodo setdefault('chave','valor')
# Esse método permite definir uma valor default de uma chave:valor
# Caso a chave fornecida como parâmetro exista nenhuma alteração será feita
# Caso a chave não exista ela será inserida no dicionario


print("\nMetodo setdefault('chave', 'valor') insere uma chave:valor")
print("=============================================================\n")

contatos = {"nome": "Guilherme", "telefone": "3333-2221"}

print(f"contato = {contatos}")

print("\nInserindo uma chave já existente com setdefault() NADA será alterado\n")

print("Alterando a chave 'nome' existente: contatos.setdefaul('nome','Giovana')\n")
contatos.setdefault("nome", "Giovanna") # "Guilherme"
print(f"contato = {contatos}  SEM ALTERAÇÃO")



print("\nAlterando a chave 'idade' inexistente: contatos.setdefaul('idade', 28)\n")
contatos.setdefault("idade", 28) 
print(f"contato = {contatos}")
print('\nNova chave inserida por default!\n')


# Metodo update('dicionario')
# Esse método permite atualizar os valores de um dicionario fornecendo uma chave existente
# Caso a chave fornecida como parâmetro exista o valor passado será atualizado
# Caso a chave não exista ela será inserida no dicionario

print("\nMetodo update (dicionario) atualiza uma chave ou insere nova ")
print("================================================================\n")


contatos.clear()
contatos = {"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}}
print(f"contato = {contatos}")

print("Atualizando contatos 'guilherme@gmail.com' com a chave nome = Gui\n")
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(f"contato = {contatos}")

print("\nAtualizando contatos 'giovanna@gmail.com' com novas chaves\n")
print("contatos.update({'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}")
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(f"contato = {contatos}")


print()


# Método values() retorna todos os valores descritos no dicionario
print("\nMetodo values()")
print("================\n")

contatos.clear()
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print(f"contato = {contatos}")


print("\nMostrando apenas os valores presentes no dicionario com contatos.values()\n")
print(f"contato.values = {contatos.values()}")

print()

# dict_values([
# {'nome': 'Guilherme', 'telefone': '3333-2221'}, 
# {'nome': 'Giovanna', 'telefone': '3443-2121'}, 
# {'nome': 'Chappie', 'telefone': '3344-9871'}, 
# {'nome': 'Melaine', 'telefone': '3333-7766'}])

# Método 'in' retorna True ou False para a chave fornecida como pesquisa

print("\nMetodo 'in'")
print("=============\n")

print(f"contatos = {contatos}")

print("\n1) Pesquisando se a chave 'guilherme@gmail.com' existe no dicionario:\n")
print(f"guilherme@gmail.com in contatos ===> {'guilherme@gmail.com' in contatos}" )

print("\n2) Pesquisando se a chave 'megui@gmail.com' existe no dicionario:\n")
print(f"megui@gmail.com in contatos ===> {'megui@gmail.com' in contatos}" )

print("\n3) Pesquisando se a chave idade in contatos['guilherme@gmail.com'] existe no dicionario:\n")
print(f"'idade' in contatos['guilherme@gmail.com'] ===> {'idade' in contatos['guilherme@gmail.com']}" )

print("\n4)Pesquisando se a chave telefone in contatos['giovanna@gmail.com'] existe no dicionario:\n")
print(f"'telefone' in ['giovanna@gmail.com'] ===> {'telefone' in contatos['giovanna@gmail.com']}" )


print()