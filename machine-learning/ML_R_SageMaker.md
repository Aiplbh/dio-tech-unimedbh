# ***Programação em R***


### ***Defnição***

R é uma linguagem de programação multi-paradigma orientada a objetos, programação funcional, dinâmica, voltada à manipulação, análise e visualização de dados.


A versão base do R possui uma coleção enorme de funções:

- Modelos estatisticos
- Algoritimos computacionais
- Metodos matematicos
- Visualização de dados


### ***Pacotes (ou módulos)***

Podem ser escritos em Fortran, C, R e C++

As funcionalidades do R podem ser ampliadas através do carregamento dos pacotes, tornand-o capaz de realizar inúmeras tarefas como:

- Análise multivariada
- Análise Bayesiana
- Manipulação de dados
- Gráficos para publicação
- Big Data, Deep Learning
- Processamento de imagens

Pacotes muito usados:

- ***maptools***: funções para leitura, exportação e manipulação de estruturas espaciais

- ***cluster***: funções para análise de clusters

- ***ggplot2***: criação de gráficos elegantes

- ***rmarkdown***: criação de documentos dinâmicos em PDF, Word, HTML

- ***nlme***: modelos lineares e não-lineares de efeitos mistos


## ***R para Machine Learning***

Usaremos o ambiente de programação Replit


Exemplo de funções:


## ***Resolvendo o primeiro problema em R***


Create a repl> escolher a linguagem R > nomear o projeto: FirstProject


- A linguagem R é complilada

- Tudo o que for gerado em R é identifiacado como objeto

- O sinal de atribuição é  <-   Ex: objeto1 <- 3*3

- R é case sensitive


- '#' é o caracter indicativo de comentários inline


## ***Operadores lógicos em R***

== igual

!= diferente

>= maior ou igual a 

<= menor ou igual a

>  maior que

<  menor que


## ***Manipulação de vetores e matrizes***


Definindo um ***vetor***:


print (Estatística Básica com R    # o c significa concatenar


lenght(primeiro.vetor)


***Matrizes***

Matriz_A <- matrix(c(2,4,3,1,5,7), nrow = 2, ncol = 3, byrow = TRUE)

Print (Matriz_A)


## ***Estatística Básica com R***


Alguns exemplos:

```
vetor <- c(2,2,3,3,3,4,4,5,4,3)

# Média
print(mean(vetor) 
[1] 3.3


# Mediana
print (median(vetor)
[1] 3


# Desvio padrão 
print (sd (vetor)
[1] 0.9486833
```



## ***Entendendo ML com Amazon SageMaker***

Notas da apresentação do Prof. Dr. Diego Renan na Plataforma DIO

```
Prof. Dr. Diego Bruno - Education Tech Lead na DIO
Doutor em Robótica e Machine Learning pelo ICMC USP
```

### ***Objetivo***

Neste curso, você aprenderá as habilidades necessárias para criar, treinar e implantar modelos de machine learning no Amazon SageMaker incluindo implementações em Python e suas bibliotecas para integrá las aos seus aplicativos para resolver problemas do mundo real.

Primeiro, você aprenderá o básico e como configurar o SageMaker Em seguida, você descobrirá como criar, treinar e implementar modelos aplicados à Classificação de problemas.


### ***Roteiro***

- Aula 01 Introdução para o SageMaker
- Aula 02 Ferramentas aplicadas no SageMaker
- Aula 03 Criando uma conta na AWS
- Aula 04 Modelos de Machine Learning
- Aula 05 Biblioteca Pandas e suas funções
- Aula 06 AWS SageMaker x Google Colab
- Aula 07 Desenvolvendo seu Primeiro Sistema no SageMaker


### ***Introdução para o SageMaker***


O Amazon SageMaker é uma plataforma de aprendizado de máquina na nuvem lançada em novembro de 2017. O SageMaker permite que os desenvolvedores criem, treinem e implantem modelos de aprendizado de máquina na nuvem.

![Topologia SageMaker](https://drive.google.com/uc?id=1xWOO3TNh3jR-mcQESaHAOLAy1HrjTNkF "SageMaker Topology")


O SageMaker permite que os desenvolvedores operem em vários níveis de abstração ao treinar e implantar modelos de aprendizado de máquina. Em seu nível mais alto de abstração, o SageMaker fornece modelos de ML pré treinados que podem ser implantados como estão.

Além disso, o SageMaker fornece vários algoritmos de ML integrados que os desenvolvedores podem treinar em seus próprios dados. Além disso, o SageMaker fornece instâncias gerenciadas do TensorFlow e do Pytorch , onde os desenvolvedores podem criar seus próprios algoritmos de ML do zero.

Independentemente do nível de abstração usado, um desenvolvedor pode conectar seus modelos de ML habilitados para SageMaker a outros serviços da AWS , como o Amazon Dynamo DBbanco de dados para armazenamento de dados estruturados, AWS Batch para processamento offline em lote, ou Amazon Kinesis para processamento em tempo real.



Várias interfaces estão disponíveis para os desenvolvedores interagirem com o SageMaker. Primeiro, há uma API da Web que controla remotamente uma instância do servidor SageMaker.


Embora a API da Web seja independente da linguagem de programação usada pelo desenvolvedor, a Amazon fornece associações de API do SageMaker para várias linguagens, incluindo Python, JavaScript, Ruby, Java e Go.

***SageMaker Portal***

![SageMaker Portal](https://drive.google.com/uc?id=1VbhJyWQV4e4321W1-q2sMC1lkVUcjZhb "SageMaker Portal")



***Sage Maker Studio***

![SageMaker Portal](https://drive.google.com/uc?id=1OO-2uRAGvRTLTjbKIEZmh2U1JpnPaSzx "Sage Maker Studio")


### ***Ferramentas do SageMaker***

O conjunto de ferramentas do SageMaker envolve recursos que são ferramentas de outras empresas como:

- Tensorflow
- PyTorch
- Apache MXNet
- XGBoost

Assim você pode construir um modelo de Machine Learning com o framework de sua escolha.

Use o Amazon SageMaker para treinar e ajustar o modelo, escolha a plataforma alvo e através do Amazon SageMaker Neo, otimize o modelo treinado para a plataforma alvo escolhida.

![](https://drive.google.com/uc?id=1lN_C0dXNhaZ_pmpkhAzu_5wPSFzn9Nkr "SageMaker Working Method")

A integração do modelo criado com as bases de dados pode ser feita com o SageMaker Data Wrangler. Com essa plataforma é possível:

- Selecionar, analisar e transformar os dados facilmente agilizando a preparação da etapa de ML.

- Rapidamente estimar a acurácia do modelo ML e diagnosticar seus problemas antes de colocá-lo em produção.

- Automatizar os fluxos de trabalho de adequação dos dados desde a preparação até a produção.

Funcionamento do Data Wrangler

![](https://drive.google.com/uc?id=19UCqEuBfJXomdN5QL0svRqX2eX46YspD "Data Wrangler: How it works")

Arquitetura de funcionamento do SageMaker

![](https://drive.google.com/uc?id=1pcpfYOlNx-VjNDlIBLWTdRjjiMb9eLe- "SageMaker Architecture")





[Workshop sobre SageMaker](https://workshop-amazon-sagemaker.readthedocs.io/pt/latest/intro_sagemaker.html)


























































































































































