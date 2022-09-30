# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Operadores Aritméticos
# Calculo da frequencia de ressonância dados os valores de C e L

from cmath import sqrt
from pickletools import float8

print ("\n------------------------------------")
print ("Cálculo da frequência de ressonância")
print ("------------------------------------\n\n")

capacitancia = 0.0
indutancia   = 0.0
PI = 3.1416


capacitancia = float(input ("Informe o valor da Capacitância em uF: "))*(10**-6)
indutancia   = float(input ("Informe o valor da Indutãncia em mH: "))*(10**-3)

frequencia_ressonante = 1 / (2*PI*((capacitancia*indutancia)**0.5))

print (f"Para os valores fornecidos de C e L a frequência de ressonância será de {frequencia_ressonante:2.2f} Hz\n\n")