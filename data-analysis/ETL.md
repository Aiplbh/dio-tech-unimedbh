# ***Fundamentos de ETL (Extract, Transform, Load) com Python***

```
Prof. Dr. Diego Renan - Pesquisador Machine Learning
Education Tech Lead na DIO
Notas de aula de Argemiro Leite
```
### ***Agenda***


01. Introdução a ETL com Python

02. Etapas para processos envolvendo ETL

03. Ferramentas aplicadas a ETL

04. Introdução a biblioteca Pandas

05. Biblioteca Pandas e suas funções

06. Introdução à biblioteca Scikit-Learn

07. Manipulando dados com Pandas

08. Framework Luigi para ETL

---

### ***01. Introdução a ETL com Python***

Ferramentas de ETL existentes:

***Pagas***

- IBM Information Server (Data Stage)

- Oracle Data Integrator (ODI)

- Informatica Power Center

- Microsoft Integeration Services (SSIS)


***Open Source***

- Pentaho Data Integrator (PDI)

- Talend ETL




### ***02. Etapas da ETL***


### Extração


O processo de Extração de dados consiste em se comunicar com outros sistemas ou bancos de dados para capturar os dados que serão inseridos no destino, seja uma Staging Area ou outro sistema.

No mapeamento, a extração de origem deve conter a especificação da identidade e seus atributos detalhados, tudo armazenado numa zona temporária. 

Quando forem efetuadas as análises e filtragens dos dados, a nova versão poderá ser comparada com a cópia da versão prévia.

### Transformação

O processo de Transformação de Dados é composto por várias etapas, entre elas: padronização, limpeza, qualidade. 

Dados vindos de sistemas diferentes tem padrões diferentes seja de nomenclatura ou mesmo de tipos de dados ( VARCHAR2 Oracle ou VARCHAR Sql Server.

A transformação inclui limpeza, racionalização e complementação dos registros. 

O processo de limpeza removerá erros e padronizará as informações. 

O processo de complementação implicará no acréscimo de dados.

### Carga

O processo de Load é a etapa final onde os dados são lidos das áreas de staging e preparação de dados, carregados no Data Warehouse ou Data Mart Final.


### Vantagens da ETL


- Garantia significativa da qualidade dos dados (uso de dados consolidados)

- Funcionalidade de execução (aplicação de modelos estatísticos e matemáticos)

- Facilidade no desenvolvimento de uma rotina de carregamento 

- Simplificação das tarefas de manutenção de uma rotina de carregamento

- Geração e Manutenção automática dos metadados evitando problemas de incorreção de dados

- Geralmente o trabalho com grandes volumes de dados utilizam processos de ETL com maior velocidade e consumindo menos recursos

- Facilidade de transferência das ferramentas de ETL entre vários servidores (nuvem)

- Conexão transparente e simplificada com diversas fontes de dados como SAP, VSAM, Mainframes, bastando adquirir o conector.

- Reinicialização do carregamento a partir de onde foi interrompido sem necessidade de programação.

- Segurança e estabilidade 


### ***03. Ferramentas aplicada à ETL***

- Inicialmente foram usadas para projetos de DW e BI.

- Hoje em dia tem sido usado em processo de integração de software e para trabalhar com Big Data

- No caso do Big Data o uso de ferramentas ETL visam expurgar dados irrelevantes no grande volume de dados.


### ETL para Big Data


Como o aumento das plataformas heterogeneas de dados surgem projetos com ferramentas próprias:

- HADOOP: Plataforma em JAva de computação distribuida voltada para cluster, procesamento de grandes volumes, com atenção à tolerânica à falhas. Ferramentas do Hadoop:

	- SQOOP: Movimentar dados entre BD Relacionais e o ambiente Hadoop

	- HIVE : Ambiente SQL sobre um cluster Hadoop

	- PIG  : Script para transformação e processamento de dados

	- SPARK: Framework de processamento em memória


```
Diferente do Data Mart que é uma especialização do Data Warehouse, o Data Lake é um único repositório, com dados brutos e que estejam disponíveis para qualquer pessoa que precise realizar uma análise. 
```


## ***04. Introdução à biblioteca PANDAS***

Essa biblioteca permite trabalhar com:

- Dados tabulares como planilhas Excel / Tabela SQL
- Dados ordenados de modo temporal ou não.
- Matrizes
- Qualquer outro conjunto de dados que não sejam rotulados


***Outras bibliotecas***

- opencv

- pillow

- scikit-image


### ***Estruturas de Dados***

Principais objetos Pandas: Series e DataFrames


***Série***

Matriz unidimensional que contém uma sequência de valores que apresentam
uma indexação (que pode ser numérica, inteira ou rótulos), como uma única 
coluna no Excel.

***DataFrame***

Estrutura tabular, semelhante à planilha Excel onde linhas e colunas tem rótulos



## ***05. Biblioteca Pandas e seus métodos principais***


DATAFRAME

df.head(n=4)
Listar as n primeiras linhas do df

df.shape
Retorna o volume de informação (lin, col)

df.info()
Formato dos dados e quantidade de memória do df


df.columns
(['col1', 'col2', ... 'coln'], dtype = 'object')

df.columns = ['col1', 'col2', ... 'col15')


df.isnull().sum()
Verificar quantos dados faltantes existem em nosso conjunto


df['setor'].unique()
Verificar numa série quais os valores que são únicos


df['setor'].value_counts().plot(kind='bar') | usando a matplotlib
Agrupar e gerar uma visualização simples e rápida


df.describe()
Informações estatísticas a respeito do nosso conjunto de dados: média, quartil, etc

## ***06. Introdução à biblioterca SCIKIT-LEARN***

Essa lib é reutilizável em diferentes situações, possui código aberto, sendo acessível a todos e foi construída sobre os pacotes NumPy, SciPy e matplotilib

***Exemplo de aplicação:***

Neste exemplo iremos criar uma massa de dados com 200 observações, com apenas uma
variável preditora, que será a variável x e a variável target, que será a y . Para isso
indicamos os parâmetros n_samples = 200 e n_features = 1 . O parâmetro noise define o
quão dispersos os dados estarão um dos outros.

```
pip install matplotlib
pip install scikit-learn


import matplotlib.pyplot as plt

from sklearn.datasets import make_regression

# gerando uma massa de dados
x, y = make_regression (n_samples = 200, n_features =1, noise = 30)

Utilizaremos o pacote matplotlib , com o módulo pyplot e a função scatter () que criará o
gráfico, e função show() que o exibirá na tela.

import matplotlib.pyplot as plt

# mostrando no gráfico

plt.scatter(x,y)
plt.show()

```

Após esta etapa, nosso modelo de machine learning está pronto e podemos utilizá lo para
prever dados desconhecidos . 

Simplificando este primeiro entendimento, vamos apenas visualizar a reta de regressão linear 
que o modelo gera, com os mesmos dados que criaram o modelo. 

Para isso iremos utilizar o método predict (), indicando que queremos aplicar a previsão nos 
valores de x . 

O resultado do método será uma previsão de y para cada valor de x apresentado.


A função plot do pacote pyplot gera uma reta com os dados apresentados. Como já temos os dados 
de x e y , basta indicá-los na função. 

Assim, primeiramente montamos novamente o gráfico de x e y original com a função scatter () e 
somamos a ele a reta de linearização.

✅ Mais detalhes no Arquivo ETL_ScikitLearn.ipyl 


## ***08. Framework Luigi para ETL com Python***


Luigi é um framework de execução criado pelo Spotify que cria pipelines de dados em
Python. Em tese, é um pacote Python (2.7, 3.6, 3.7 testado) que ajuda a construir pipelines
complexos de trabalhos em lote. 

Ele lida com resolução de dependências, gerenciamento de fluxo de trabalho, visualização, 
tratamento de falhas, integração de linha de comando e muito mais.


***Target***

Um alvo contém a saída de uma tarefa. Um destino pode ser um local (por exemplo: um arquivo), (MySQL etc)

***Task***

Tarefa é algo onde o trabalho real ocorre. Uma tarefa pode ser independente ou dependente. O exemplo de uma tarefa dependente é despejar os dados em um arquivo ou banco de dados. Antes de carregar os dados, os dados devem estar lá por qualquer meio (scraping , API, etc ). 

Cada tarefa é representada como uma classe Python que contém certas funções membro obrigatórias. Uma função de tarefa contém os seguintes métodos:

- require()

Esta função membro da classe task contém todas as instâncias de tarefas que
devem ser executadas antes da tarefa atual.


- output()

Este método contém o destino onde a saída da tarefa será armazenada. Isso
pode conter um ou mais objetos de destino.


- run()

Este método contém a lógica real para executar uma tarefa.

### ***Referencias***
[www.luigi.readthedocs.io](www.luigi.readthedocs.io)
















































































