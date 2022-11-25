# ***DIO Introdução ao MongoDB e Bancos de Dados NoSQL***

```
Pamela Apolinario - Software Enginner 
```



## ***Introdução***


### ***Bancos não relacionais***

- Surgiu em 2009

- NoSQL = Not Only SQL

### ***Diferenças BDR e BDNoSQL***

1. Os BD Relacionais tem escalabilidade vertical:
	- Aumento do processador, memória e HD
	- Um unico recurso pode exigir escalar


2. Os BD NoSQL tem escalabilidade horizontal
	- Particionando os dados (sharding) entre os nós
	- escalabilidade teoricamente infinita (nuvem)
	- melhor performance sob aumento de demanda

3. Ausencia (quase) completa de regras de schema [schema-free or schemaless]
4. No relacional a consistencia dos dados é melhor
5. Falta de uma linguagem formal de consulta

6. Performance

	- BD Relacional tem sua performance atrelada ao desempenho dos HDs
	- BD NoSql é clusterizado e depende da infra de rede interligando os nós

7. Transações

	- BDR são transacionais e usam o princípio ACID
	- BDNoSQL não tem o conceito de transacionalidade (preferem desempenho) 
		- BASE (Basically Available Soft-State Eventually Consistent)

```
Atomicidade: uma transação tem que ser completamente executada ou descartada
Consistencia: apos uma transação concluida o BD estará em conformidade com o schema
Isolamento: Uma transação nunca interfere em outra transação
Durabilidade: uma vez concluida a transação o dado não mais será perdido.
``` 

### ***No SQL - Principais vantagens***

- Flexibilidade
- Escalabilidade
- Alta Performance

## ***Conhecendo os tipos de bancos de dados NoSql***


[Sugestão de site para comparação dos diversos BD](https://db-engines.com/en/)


## ***Tipos de BD NoSql***

✅ Document Store    [Ex. Mongo]

- json
- xml

✅ Key-value Store   [Ex. Redis]
Baseado em cache

✅ Wide-column store [Ex. Cassandra]
Apresenta maior semelhança com o BDR

✅ Graph store       [Ex. Neo4j]
Banco de dados oreintados a grafos


### ***Tipo Grafo***

. Estruturas matemáticas compostas por nós [dados] e vertices [relacionamentos]
. Muito usado na detecção de fraudes, redes sociais, mecanismos de recomendação,
  games, sistemas de arquivo.

. Ex. Neo4j, Cosmos da Microsoftware Azure



. Vamos criar uma estrutura de regeistros que compoem os dados de uma rede social
  usando um sand box do Neoj4

. Esse BD é um dos poucos BD NoSql que aplicam as propriedades ACID, lidam bem com 
  concorrência. Usa a linguagem Cipher para estruturação dos dados.

. O Neo4j oferece um sandbox disponível em: sandbox.neo4j.com

. Criação da conta: @gmail / N....A....1


Após carregamento do ambiente criamos os seguintes elementos:


CREATE (:Client {name: "Bob Esponja" , age: 28, hobbies: ['Caçar agua-viva, Comer hamburguer de siri']})

>> Added 1 label, created 1 node, set 3 properties, completed after 40 ms.



Verificação:

MATCH (bob_esponja) RETURN bob_esponja 
Nessa consulta não foi usado nenhum critério de busca (select all).
O valor foi retornado na variável bob_esponja e apresentado no ambiente.



                         [Bob Esponja]



Criando os nós Lula Molusco e o nó Patrick com relacionamento deles 

CREATE (:Client{name: "Lula Molusco", age: 30, hobbies: ['Tocar clarinete','Infernizar o Bob Esponja']}) - [:Bloqueado] -> ( :Client {name: "Patrick", hobbies: ['Caçar agua-viva']});


Visualizando:

MATCH (todos) RETURN todos;

```

                         [Patrick]<----bloqueado----[Lula Molusco]



                         [Bob Esponja]

```

Criando relacionamento entre Bob e Patrick

MATCH (patrick:Client {name: "Patrick"}), (bob: Client {name: "Bob Esponja"}) CREATE (patrick) -  [:Amigo] -> (bob)



MATCH (todos) RETURN todos;

```

                         [Patrick]<----bloqueado----[Lula Molusco]
                             |
                             | amigo
                             v
                         [Bob Esponja]
```

## ***Bancos NoSql baseado em Colunas***


Primeiro a ser criado foi o  _Cassandra_: usado pelo Facebook, Twitter, etc

Termos usados nos DB NoSql baseados em coluna:

- Keyspace: agrupamento de familias de colunas ======> database
- Column Family / table: agrupamento de colunas =====> tabelas
- Row key: chave que representa uma linha de coluna => Primary Key
- Column: representa um valor contendo: Name, Value e Timestamp

Nesse tipo de BD a pesquisa é feita pelas chaves. É importante pensar em uma chave que tenha sentido para a consulta.

Exemplo:

- Registro de transações: compras, resultados de testes, filmes assistidos, etc

- Rastreamento de praticamente qualquer coisa, incluindo status do pedido, pacotes, etc.


***Utilização do Cassandra [open source]***

- Será usado o CQL [Cassandra Query Language]


## ***Instalando o Cassandra pelo docker**

[https://www.linkedin.com/pulse/instalando-o-sgbd-cassandra-docker-douglas-littig/](https://www.linkedin.com/pulse/instalando-o-sgbd-cassandra-docker-douglas-littig/)

```
Baixar a imagem
> docker pull cassandra

Conferir imagem
> docker images


Criar pasta no Linux para persistir dados
> sudo mkdir /var/lib/cassandra -p


Criação do container chamado cassandra na porta 9000:9000
> docker run --name cassandra -p 9000:9000 -v /var/lib/cassandra:/var/lib/cassandra -d cassandra


Verificar se o docker está rodando
> docker ps 


Acessar o bash do container:
> docker exec -it cassandra bash


Acessar o CLI do CQL do Cassandra
root@<idcontainer>:/# cqlsh


cqlsh> 

cqlsh> CREATE KEYSPACE fenda_biquini WITH replication = {'class' : 'SimpleStrategy' , 'replication_factor' : 1};

cqlsh> use fenda_biquini

cql:fenda_biquini> CREATE COLUMNFAMILY clients (name TEXT PRIMARY KEY, age int);


cql:fenda_biquini> SELECT * FROM clients

nome | age 
-----+-----

cql:fenda_biquini> INSERT INTO clients (name,age) VALUES ('Bob Esponja', 33);

cql:fenda_biquini> SELECT * FROM clients

 
nome         | age 
-------------+-----
 Bob Esponja | 38 


Inserindo um novo registro dessa vez usando json

cql:fenda_biquini> INSERT INTO clients JSON '{"name":"Patrick"}';

cql:fenda_biquini> SELECT * FROM clients

 
 nome        | age 
-------------+------
 Bob Esponja |   38 
 Patrick     | NULL



cqlsh:fenda_biquini> SELECT age, WRITETIME(age) FROM clients;

 age  | writetime(age)
------+------------------
   33 | 1668177976736483
 null |             null

(2 rows)

cqlsh:fenda_biquini>

```

***Consultas no Cql***

```
cql:fenda_biquini> SELECT * FROM clients WHERE name = 'Bob Esponja';

nome         | age 
-------------+-----
 Bob Esponja | 38 

```


***Consultas com resposta em json***

```
cql:fenda_biquini> SELECT json * FROM clients WHERE name = 'Bob Esponja';


 [json]
------------------------------------
 {"name": "Bob Esponja", "age": 33}

```


***Consultas com resposta em json***

```
cqlsh:fenda_biquini> SELECT json * FROM clients;

 [json]
------------------------------------
 {"name": "Bob Esponja", "age": 33}
   {"name": "Patrick", "age": null}

(2 rows)

```

***Fazendo um Update na idade*** 

```
cqlsh:fenda_biquini> UPDATE clients SET age=33 WHERE name='Patrick';

cqlsh:fenda_biquini> SELECT json * FROM clients;

 [json]
------------------------------------
 {"name": "Bob Esponja", "age": 33}
     {"name": "Patrick", "age": 33}

(2 rows)

cqlsh:fenda_biquini>

```

***Alterando ColumnFamily do Keyspace***

```

cqlsh:fenda_biquini> ALTER COLUMNFAMILY clients ADD hobby text;

cqlsh:fenda_biquini> SELECT * FROM clients;

 name        | age | hobby
-------------+-----+-------
 Bob Esponja |  33 |  null
     Patrick |  33 |  null

(2 rows)

cqlsh:fenda_biquini> update clients set hobby='Caçar agua viva' where name= 'Patrick';

```

### ***Obs.: a função WRITETIME não funciona para coleções por isso foi usado uma string***


```
cqlsh:fenda_biquini> SELECT * FROM clients;

 name        | age | hobby
-------------+-----+-----------------
 Bob Esponja |  33 |            null
     Patrick |  33 | Caçar agua viva  <<<=== atualizado

(2 rows)
```

No BD NoSql as colunas podem ser atualizadas individualmente, diferentemente do BDR onde uma atualização é feita em todo o registro.

Isso pode ser verificado pelo Timestamp diferente para cada alteração no ColumnFamily.

O timestamp para a coluna age é diferente do da coluna hobby

```
cqlsh:fenda_biquini> select age, writetime(age), hobby, writetime(hobby) from clients;

 age | writetime(age)   | hobby           | writetime(hobby)
-----+------------------+-----------------+------------------
  33 | 1668177976736483 |            null |             null
  33 | 1668178427900173 | Caçar agua viva | 1668178762892972

(2 rows)
```

***Deletar um registro:***

```

cqlsh:fenda_biquini> delete from clients where name='Bob Esponja';

cqlsh:fenda_biquini> SELECT * FROM clients;

 name    | age | hobby
---------+-----+-----------------
 Patrick |  33 | Caçar agua viva

(1 rows)

```

---


## ***Banco de dados NoSDql baseados em chave:valor***

- Armazena um conjunto de dados, simples ou complexo, identificados por um identificador exclusivo.

- Bom desempenho em aplicações na nuvem.

- Menor capacidade de busca.

Uso:

Cache, sessão de usuário, carrinhos de compra


Hoje o Redis está em primeira posição

Iremos utilizar o Redis, um banco de dados cache e mensageira:


***REDIS - Caracteristicas***


- Alto desempenho
- Estrutura de dados na memória.
- Versatilidade de uso
- Replicação e persistência


Usado por: Twitter, Github, Stackoverflow etc


O REDIS tem um sandbox, mas não possui um console



## ***Introdução ao MongoDB***

Algumas características do MongoDB:

- BD de código aberto

- Alta performance

- Schema-free

- Dentro de uma mesma collection pode-se ter documentos de estruturas diferentes

- Utiliza bson que é o armazenamento json (pares chave-valor) em binário.

- Suporta índices

- Auto-sharding (escalagem horizontal)

- Map-reduce (ferramenta de consulta e agregação)

- Suporte ao GridFS que é a especificação de um driver apra carga e recuperação de arquivos 
  BSON maiores que  16MB. (Until the addition of GridFS in MongoDB, it was difficult to store files directly into a database using a single API request.)

- Tem uma rica linguagem de consulta permitindo quase todos os tipos de busca no BD.


## ***Estruturação do Mongo***


- O 'documento' é a menor unidade dentro do BD.

- Define uma Tupla/registro

- Precisa ser autocontido e autodescritivo

- A ideia de usar o MongoDB é a de que seus dados não vão depender de outros dados externos.

- Isso leva a algumas redundâncias.

- A estrutura análoga à tabela é a collection. Ela receberá todos os documentos.

- A collection possui o schema totalmente free e por isso cada documento tem sua propria descrição

- Embedding/linking assemelha-se ao join dos BDR. Permite que o MongoDB faça referência aos documentos
de outras collections, mas de forma embutida.



## ***Quando usar***

- Grande volume de dados

- Deve-se preocupar na modelagem com a criação de índices para melhorar a performance.

- Trabalha com dados não necessariamente estruturados (exemplo do cardápio)


## ***Quando não usar***

- Necessidade de relacionamentos/joins

- Necessidade de propriedades ACID e transações. Algumas entidades financeiras não homologam sistenas
cujos dados financeiros não estejam em BDR tradicionais.



## ***Instalação do MongoDB com Docker***


Criação do docker-compose.yml para coordenar a instalação do MongoDB em um container Docker.


## ***Instalando o docker-compose no WSL2***

```

sudo curl -L https://github.com/docker/compose/releases/download/1.27.4/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```
### ***Docker-compose.yml***

```

version: '3'

services: 
         mongodb:
            image: mongo
            container_name: mongodb
            restart: always
            environment: 
               - MONGO_INITDB_ROOT_USERNAME=dio
               - MONGO_INITDB_ROOT_PASSWORD=dio

             ports:

               - "27017:27017"
             
	      volumes:

               - ./:/app
               - ./another/folder:/folder
```


## ***Instalação sem usar docker compose (preferi usar essa opção)***

Após instalar o WSL2 abrir um terminal Linux Ubuntu e enviar os seguintes comandos:

```
docker pull mongo

docker images

docker run -p 27017:27017 -d --rm \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=password \
--name mongodb \
mongo
```

## ***Entrar no bash do Mongo***

```
docker exec -it mongodb bash

root@e22f2fc57508:/bin#
```

## ***Rodar o Mongo Client***

```
root@e22f2fc57508:/bin# mongosh --host 127.0.0.1:27017 -u admin -p password

String de conexão: mongodb://admin@127.0.0.1:27017

Password: password
```

Caso tudo transcorra corretamente receberemos o prompt do Mongo:

```
test> show databases
admin   100.00 KiB
config   12.00 KiB
local    72.00 KiB
test>
```

## ***Acessando o Mongodb pelo app Robo3T [Agora Studio 3T]***

- Baixar o app no link:  [https://studio3t.com/download/](https://studio3t.com/download/)


***Windows***

***How to install Studio 3T:***

- Download the latest release of Studio 3T. 
- Start the installer by opening the file. 
- Follow the directions on the screen.

***How to uninstall Studio 3T:***

- On Windows 8 and 10: 
	- In Search, enter Control Panel and select Control Panel. 
	- Now select Programs, next select Programs and Features, and then select Studio 3T.

- On Windows 7: 
	- Open Programs and Features by clicking the Start button, clicking Control Panel, clicking Programs, and then clicking Programs and Features.
	- Select Studio 3T, and then click Uninstall.
	- Follow the directions on the screen.


- Senha Master para o Studio 3T: MongoDbAipl#1

- Conexão ao Mongodb no Docker:

	- Nome da conexão que eu criei:  MongoDio

	- From URL: mongodb://admin@127.0.0.1:27017

	- Password: password


## ***Apresentação do MongoDB Cloud***


- Acessar o Site da Mongodb Cloud (Atlas)

- Será necessário fazer um cadastro para ter acesso às ferramentas do Mongo Cloud

```
Login:
Email: aipleite@gmail.com
Passw: AtlasAipl#1
```
Criei um Database na nuvem com os seguintes dados:

- Nome: ClusterTestDIO

- User: aiplbh

- Pass: M-------------1

### ***Mongo Compass***

Apresentação de outra ferramenta para acesso à nuvem.

Senha de conexão ao BD criado na nuvem:

mongodb+srv://aiplbh:<password>@clustertestdio.3y7oevz.mongodb.net/test

mongodb+srv://aiplbh:MongodbCloudAipl1@clustertestdio.3y7oevz.mongodb.net/test


## ***Schema design e boas práticas***

### ***Objetivo***

- Apresentar conceitos de Schema Design

- Apresentar algumas boas práticas

```Obs: O Mongo só consegue aplicar o conceito de atomicidade estiver trabalhando no mesmo documento.```

### ***Schema Design***


A prática mais recomendada é usar Embbeding para criar os relacionamentos, mas há a possibilidade de se trabalhar com referências.

| Embbeding  | 	Referência |
|---  |--- |
| Documentos auto-contidos 	|	Documentos com dependência de outros docs |


***Vantagens de se usar Embedding:***

- Consulta informações em uma única query

- Atualiza o registro em uma única operação

***Desvantagens do Embedding***

- Limite de 16 MB por documento


***Vantagens de se usar Referencia***

- Documentos menores

- Não duplica informações

- Bom de ser usado quando os dados não forem acessados em todas as consultas


***Desvantagens de se usar Referencia***

- Duas ou mais queries ou utilização do $lookup para concluir a consulta


```Para quem desejar aprofundar os estudos em design patterns para BD NoSql por documento fica o link:```

[www.mongodb.com/blog/post/building-with-patterns-a-summary](www.mongodb.com/blog/post/building-with-patterns-a-summary)  ✅


## ***Boas práticas além dos desing patterns***

- Evitar documentos muitos grandes

- Não existe um local no Mongo para guardar schemas então use nome e campos objetivos e curtos

- Analise suas queries utilizando explain()

- Atualiza apenas os campos alterados

- Evite negações em queries.

- Listas/Arrays devem ser avaliados pois se crescerem indefinidamente podem prejudicar a 
  performance do BD.


## ***JSON vs BSON***

***BSON***
É uma serialização codificada em binário de documentos, semelhantes a JSON.

Contém extensões para representar dados que estão além da especificação JSON, como por
exempo os tipos DATE e OBJECTID.

## ***Conceitos práticos***

### ***Operação de manipulação de dados***

***Mostrar as databases***  (No Mongo podem existir vários databases dentro de uma mesma instancia)

> show database;

***Criar um database*** 

No Mongodb não existe um comando para criar. Basta utilizar a palavra reservada 'use'.
```
> use fenda_biquini 
switched to db fenda_biquini
fenda_biquini>
```
O comando já muda para o DB referenciado

---

***Vamos fazer o mesmo processo no Studio 3T:***

- Criando o DB: DB_Test

Para criar um collection lembrar que o Mongo é uma collection de documentos:

Há duas formas:

- Explicitamente, antes do uso

- Referenciar a colletion. Nesse caso o Mongo verifica que ela não existe e cria. (implicita)

Na forma explicita é possível passar alguns validadores com tam_max do doc, tam_max da collection, etc.


***Criação de uma collection de forma explicita usando validadores***

```
fenda_biquini> db.createCollection("test" , {capped: true, max: 2, size: 2});
{ ok: 1 }
fenda_biquini>
```

- Inserir dado em uma Collection explicitamente criada

```
fenda_biquini> db.test.insertOne({"name": "Teste 1"});
{
  acknowledged: true,
  insertedId: ObjectId("6371c7b2a8379b70172ce822")
}
```

- Listar todos os documentos da Collection

```
fenda_biquini> db.test.find({});
[ { _id: ObjectId("6371c7b2a8379b70172ce822"), name: 'Teste 1' } ]
```

Inserir mais registros ultrapassando o tamanho maximo definido de 2

```
fenda_biquini> db.test.insertOne({"name": "Teste 2"});
{
  acknowledged: true,
  insertedId: ObjectId("6371c859a8379b70172ce823")
}
fenda_biquini> db.test.find({});
[
  { _id: ObjectId("6371c7b2a8379b70172ce822"), name: 'Teste 1' },
  { _id: ObjectId("6371c859a8379b70172ce823"), name: 'Teste 2' }
]
fenda_biquini> db.test.insertOne({"name": "Teste 3"});
{
  acknowledged: true,
  insertedId: ObjectId("6371c880a8379b70172ce824")
}
fenda_biquini> db.test.find({});
[
  { _id: ObjectId("6371c859a8379b70172ce823"), name: 'Teste 2' },
  { _id: ObjectId("6371c880a8379b70172ce824"), name: 'Teste 3' }
]
```

- Criação de outra Collection de forma implícita

```
fenda_biquini> db.test1.insertOne({"age":10});
{
  acknowledged: true,
  insertedId: ObjectId("6371c9a2a8379b70172ce825")
}
fenda_biquini> db.test1.find({});
[ { _id: ObjectId("6371c9a2a8379b70172ce825"), age: 10 } ]
fenda_biquini>

fenda_biquini>

fenda_biquini> db.test1.insertOne({"age":10});
{
  acknowledged: true,
  insertedId: ObjectId("6371c9b6a8379b70172ce826")
}
fenda_biquini> db.test1.insertOne({"age":10});
{
  acknowledged: true,
  insertedId: ObjectId("6371c9b7a8379b70172ce827")
}
fenda_biquini> db.test1.insertOne({"age":10});
{
  acknowledged: true,
  insertedId: ObjectId("6371c9b8a8379b70172ce828")
}
fenda_biquini> db.test1.insertOne({"age":10});
{
  acknowledged: true,
  insertedId: ObjectId("6371c9b9a8379b70172ce829")
}
fenda_biquini> db.test1.insertOne({"age":10});
{
  acknowledged: true,
  insertedId: ObjectId("6371c9baa8379b70172ce82a")
}
fenda_biquini> db.test1.insertOne({"age":10});
{
  acknowledged: true,
  insertedId: ObjectId("6371c9bba8379b70172ce82b")
}
fenda_biquini> db.test1.find({});
[
  { _id: ObjectId("6371c9a2a8379b70172ce825"), age: 10 },
  { _id: ObjectId("6371c9b6a8379b70172ce826"), age: 10 },
  { _id: ObjectId("6371c9b7a8379b70172ce827"), age: 10 },
  { _id: ObjectId("6371c9b8a8379b70172ce828"), age: 10 },
  { _id: ObjectId("6371c9b9a8379b70172ce829"), age: 10 },
  { _id: ObjectId("6371c9baa8379b70172ce82a"), age: 10 },
  { _id: ObjectId("6371c9bba8379b70172ce82b"), age: 10 }
]
fenda_biquini>
```

⚠️ Nesse caso não é possível definir o tamanho máximo da collection

O db.[collection].insertOne() só faz a inserção de um documento. Para fazer a inserção de mais documentos pode-se usar apenas o comando ***insert()***. Esse método recebe um array de documentos:

- Criando o DB clients e inserindo dois elementos
```
> db.clients.insert([{"name":"Patrick","age":35},{"name":"Bob Esponja"}]);
```

### ***Usando o método save() para atualizar o banco***

Esse método realiza a atualização de um dado já existente ou, caso o dado não exista, realiza
sua criação.

```
db.clients.save( {"_id": ObjectId("63730313e201fac3f9351931"), "name": "Patrick", "age": 40});
```
⚠️ Não funcionou. O comando parece estar desativado. A documentação sugere trocar por _***replaceOne()***_

Forma geral:
```
db.collection.replaceOne(filter, replacement, options)
```
- Aplicação do comando ***replaceOne()***
```
fenda_biquini> db.clients.replaceOne({_id: ObjectId("63730313e201fac3f9351931")}, {"name":"Patrick", "age":40}, { upsert: true });
{             
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}

fenda_biquini> db.clients.find({});
[
  {
    _id: ObjectId("63730313e201fac3f9351931"),
    name: 'Patrick',
    age: 40
  },
  { _id: ObjectId("63730313e201fac3f9351932"), name: 'Bob Esponja' },
  {
    _id: ObjectId("63730f34e201fac3f9351933"),
    name: 'Lula Molusco',
    age: 40
  }
]
```

- Aplicação do método ***db.update()***

``` 
db.collection.update(query, update, options)
```

Vamos atualizar o documento inserindo a idade do Bob Esponja:
```
db.collection.update({"name": "Bob Esponja"}, {$set:{"age":40}});

fenda_biquini> db.collection.update({"name": "Bob Esponja"}, {$set:{"age":40}});
```

⚠️ Resposta ao comando:

DeprecationWarning: Collection.update() is deprecated. Use updateOne, updateMany, or bulkWrite.
{                                                             
  acknowledged: true,
  insertedId: null,
  matchedCount: 0,
  modifiedCount: 0,
  upsertedCount: 0

A mensagem susger que usemos o método updateOne() que pela documentação deve ter a seguinte sintaxe:

```
db.collection.updateOne(filter, update, options)
```
Onde: 

filter corresponde a: {"name": "Bob Esponja"}

update corresponde a: {$set:{"age":40}}

options corresponde a: [nada]

Então ficará:

```
fenda_biquini> db.clients.updateOne({"name": "Bob Esponja"}, {$set:{"age":40}});
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
fenda_biquini> db.clients.find({});
[
  {
    _id: ObjectId("63730313e201fac3f9351931"),
    name: 'Patrick',
    age: 40
  },
  {
    _id: ObjectId("63730313e201fac3f9351932"),
    name: 'Bob Esponja',
    age: 40
  },
  {
    _id: ObjectId("63730f34e201fac3f9351933"),
    name: 'Lula Molusco',
    age: 40
  }
]
```


- Selecionar todos os objetos com age = 40 e mudar para 43 [usando updateMany()
```
fenda_biquini> db.clients.updateMany({"age":40}, {$set:{"age":43}});
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 3,
  modifiedCount: 3,
  upsertedCount: 0
}

fenda_biquini> db.clients.find({});
[
  {
    _id: ObjectId("63730313e201fac3f9351931"),
    name: 'Patrick',
    age: 43
  },
  {
    _id: ObjectId("63730313e201fac3f9351932"),
    name: 'Bob Esponja',
    age: 43
  },
  {
    _id: ObjectId("63730f34e201fac3f9351933"),
    name: 'Lula Molusco',
    age: 43
  }
]
```
O comando update() embora deprecated ainda funciona:
```
fenda_biquini> db.clients.update({"age":43}, {$set:{"age":47}},{multi:true});
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 3,
  modifiedCount: 3,
  upsertedCount: 0
}
fenda_biquini> db.clients.find({});
[
  {
    _id: ObjectId("63730313e201fac3f9351931"),
    name: 'Patrick',
    age: 47
  },
  {
    _id: ObjectId("63730313e201fac3f9351932"),
    name: 'Bob Esponja',
    age: 47
  },
  {
    _id: ObjectId("63730f34e201fac3f9351933"),
    name: 'Lula Molusco',
    age: 47
  }
]
```

### ***Melhorando o comando find() com operadores query (ver lista abaixo)***

[Documentação do Mongo](https://www.mongodb.com/docs/v4.4/reference/operator/query/)

***Operador $in***

Aplicação do operador $in com o métido _***db.collection.find()***_

```
db.collection.find(query, projection)

fenda_biquini> db.clients.find({"age":{$in:[40,53]}});
[
  {
    _id: ObjectId("63730313e201fac3f9351931"),
    name: 'Patrick',
    age: 40
  },
  {
    _id: ObjectId("63731f6ae201fac3f9351934"),
    name: 'Siriguejo',
    age: 53
  }
]
```


***Operador $or***

Encontrando o documento que tenha idade = 41 ou name = Lula Molusco

```
fenda_biquini> db.clients.find({$or:[{"name":"Lula Molusco"},{"age":53}]});
[
  {
    _id: ObjectId("63730f34e201fac3f9351933"),
    name: 'Lula Molusco',
    age: 47
  },
  {
    _id: ObjectId("63731f6ae201fac3f9351934"),
    name: 'Siriguejo',
    age: 53
  }
]
```

***Operador $lt (less than)***

[Documentação do Mongo](https://www.mongodb.com/docs/v4.4/reference/operator/query/lt/#mongodb-query-op.-lt)


Syntax: {field: {$lt: value} }

Encontrando o documento onde a idade seja menor que 45 anos

```
fenda_biquini> db.clients.find({age:{$lt:45}});
[
  {
    _id: ObjectId("63730313e201fac3f9351931"),
    name: 'Patrick',
    age: 40
  }
]
```


***Métodos para deleção de documentos delete()***


db.collection.deleteOne()

[Mongo Docs: deleteOne()](https://www.mongodb.com/docs/v4.4/reference/method/db.collection.deleteOne/)

db.collection.deleteMany()

[Mongo Docs: deleteMany()](https://www.mongodb.com/docs/v4.4/reference/method/db.collection.deleteMany/)


### *** Aplicação deleteOne()***

```
fenda_biquini> db.clients.find({});
[
  {
    _id: ObjectId("63730313e201fac3f9351931"),
    name: 'Patrick',
    age: 40
  },
  {
    _id: ObjectId("63730313e201fac3f9351932"),
    name: 'Bob Esponja',
    age: 47
  },
  {
    _id: ObjectId("63730f34e201fac3f9351933"),
    name: 'Lula Molusco',
    age: 47
  },
  {
    _id: ObjectId("63731f6ae201fac3f9351934"),
    name: 'Siriguejo',
    age: 53
  }
]


fenda_biquini> db.clients.deleteOne({"age":{$eq:53}});
{ acknowledged: true, deletedCount: 1 }


fenda_biquini> db.clients.find({});
[
  {
    _id: ObjectId("63730313e201fac3f9351931"),
    name: 'Patrick',
    age: 40
  },
  {
    _id: ObjectId("63730313e201fac3f9351932"),
    name: 'Bob Esponja',
    age: 47
  },
  {
    _id: ObjectId("63730f34e201fac3f9351933"),
    name: 'Lula Molusco',
    age: 47
  }
]
fenda_biquini>
```
### ***Query selectors***  👀
[MongoDocs: Query selectors](https://www.mongodb.com/docs/v4.4/reference/operator/query/#std-label-query-selectors)

***Comparison Selectors:***

Name 	Description
$eq	Matches values that are equal to a specified value.
$gt	Matches values that are greater than a specified value.
$gte	Matches values that are greater than or equal to a specified value.
$in	Matches any of the values specified in an array.
$lt	Matches values that are less than a specified value.
$lte	Matches values that are less than or equal to a specified value.
$ne	Matches all values that are not equal to a specified value.
$nin	Matches none of the values specified in an array.

***Lógicosand
$not
$nor
$or

## ***Performance e índices***

Que são índices no que se refere a MongoDb?

Estrutura para simplificar e agilizar a busca de documentos, prevenindo um scan da collection inteira o que poderia causar impacto na performance do banco. Corresponde a um try-catch.

```
try {
  
	for ( var i=0; i < 10000; i++){
        
     		db.clients2.insert({ name: "Cliente " + i, age: i});
	}

} catch (e) {
  	print (e);
}
```

## ***Criação de uma Colletction com 10000 documentos***

O Studio 3T aceita javascript para construção de scripts de consulta. 

Criando uma Colletction de nome clients2 com 10000 itens:
```
for ( var i=0; i < 10000; i++){
        
     db.clients2.insert({ name: "Cliente " + i, age: i});
}
db.getCollection('clients2').find({})
db.getCollection('clients2').estimatedDocumentCount({})
```
- Procurando pelo documento referente ao cliente 745
```
db.getCollection('clients2').find({name: "Cliente 745"}).explain(true)
```
Verifica-se no campo statistics que foram feitas 10000 consultas

Mesmo procurando pelo primeiro registro:
```
db.getCollection('clients2').find({name: "Cliente 0"}).explain(true)
```
o TotalDocsExamined = 10000.

Agora vamos criar um índice para o campo name:

```
db.getCollection('clients2')createIndex({name: 1}, {"name": "idx_name"})
```
Onde: 

name: 1 ==> indica ordenação do índice

name = idx_index ==> é necessário nomear o índice criado

Agora, ao ser pesquisada a estatístic da consulta obtemos:

TotalDocsExamined = 1

## ***Agregações***
[Mongo Docs: Aggregation](https://www.mongodb.com/docs/manual/aggregation/)

***Objetivos***

Apresentar conceitos de agregação

- Vamos importar um BD de teste para o cluster criado no MongoCloud
- Para obter as agregações usamos os operadores de queries abaixo:


***Query selectors***  👀

[Mongo Docs: Queries](
https://www.mongodb.com/docs/v4.4/reference/operator/query/#std-label-query-selectors)

Comparison Selectors:

|Name| Description |
|---   |---          |
|$eq|Matches values that are equal to a specified value.|
|$gt|Matches values that are greater than a specified value.|
|$gte|Matches values that are greater than or equal to a specified value.|
|$in|Matches any of the values specified in an array.|
|$lt|	Matches values that are less than a specified value.|
|$lte|Matches values that are less than or equal to a specified value.|
|$ne|	Matches all values that are not equal to a specified value.|
|$nin	|Matches none of the values specified in an array.|

Lógicos

$and

$not

$nor

$or

---


### ***Links úteis***

Building with Patterns: A Summary | MongoDB

  - [https://www.mongodb.com/blog/post/building-with-patterns-a-summary](https://www.mongodb.com/blog/post/building-with-patterns-a-summary)
  
MongoDB Manual
  - https://www.mongodb.com/docs/manual/

### ***Some references***

***delete command***

https://www.mongodb.com/docs/v4.4/reference/command/delete/#mongodb-dbcommand-dbcmd.delete

It removes documents from a collection. A single delete  command can contain 
multiple delete specifications. The command cannot operate on capped collections. 

***Capped collections***

https://www.mongodb.com/docs/v4.4/core/capped-collections/

Capped collections are fixed-size collections that support high-throughput 
operations that insert and retrieve documents based on insertion order. 

Capped collections work in a way similar to circular buffers: once a collection 
fills its allocated space, it makes room for new documents by overwriting the 
oldest documents in the collection.




