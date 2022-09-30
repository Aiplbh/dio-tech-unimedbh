# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Entrada e saída de dados

from xml.sax.xmlreader import AttributesImpl


nome  = input("Informe seu nome: ")
idade = input("Informe sua idade: ")


# Função print 
print (nome, idade)

# Função print com uso do parâmetro end
print (nome, idade, end = "...\n\n")

# Função print com uso do parâmetro sep (default de sep é espaço)
print (nome, idade, sep = " --> ")

