***DIO Bootcamp - Geração Tech Unimed-BH - Aiplbh - Novembro / 2022*** <br>

Notas de aula de [Argemiro Leite](https://github.com/Aiplbh) durante o bootcamp  Geração Tech da [Unimed-BH](https://portal.unimedbh.com.br/wps/portal/corp/unimedbh/trabalhe_conosco) em parceria com a [DIO](https://web.dio.me/)
```
Módulo: Boas práticas com DynamoDB [Banco NoSQL]
Instrutor: Cassiano Peres - Brexit

```


# ***Boas práticas com DynamoDB [Banco NoSQL]***
## ***Objetivos***
- Conhecer DynamoDB da AWS
- Explorar boas práticas de modelagem
- Otimizar desempenho e custos
- Criar tabelas e realizar queries de pesquisa
---
## ***Roteiro***
### Etapa 1 - Banco de dados relacional x não relacional
### Etapa 2 - Sobre o DynamoDB
### Etapa 3 - Boas práticas com DynamoDB
### Etapa 4 - Pratica

---

# ***Introdução ao Dynamo DB***

### Banco de dados não-relacional (NoSQL)
É um banco de dados que não segue o modelo relacional com tabelas, fazendo uso do modelo chave-valor para armazenar os dados.

Ex.: MongoDB, DynamoDB, Redis


![Modelo key-value](https://drive.google.com/uc?id=1giZ5CM1HsUoLHkJtL6tzBwv1YBtxnXMd "Key-value")

## ***Amazon Dynamo DB***

Por ser totalmente gerenciado traz as seguintes vantagens:
- Trata do provisionamento
- Instalação e configuração do hardware
- Replicação e correção de software
- Escalabilidade de cluster
- Permite setar o tempo de vida do registro (time-to-live)

### Aplicação

Sistemas com grande volume de dados e necessidade de baixa latência.

- 10 trilhoes de solicitações / dia
- picos de 20 milhoes de solicitações / segundo
- 99,9 % de disponibilidade

<br>

## ***Componentes principais*** 

<br>

### Tabelas
O ***DynamoDB*** armazena suas informações em tabelas que são coleções de dados (collections).

### Itens
Um item é um grupo de atributos identificável exclusivamente entre todos os outros itens.

### Atributos
Cada item é composto de um ou mais atributos. Um atributo é um elemento atômico fundamental. 

É o menor elemento da hierarquia de objetos dos bancos NoSQL.

### Chaves primárias
Identifica cada item na tabela de modo que não possam existir dois registros com a mesma chave.

Existem dois tipos de chave primária:

- ***Simples*** 
- ***Composta***

### Chave primária simples
É conhecida como ***partition key*** e usada para identificar um documento na tabela. Sua entrada é uma função _hash_ e sua saída identifica fisicamente onde o registro será gravado.

### Chave primária composta
Chave formada por dois atributos: ***Partition Key*** e uma  ***sort key***. As duas juntas identificam um único registro.

É uma boa prática usar essas chaves compostas, pois facilitam a pesquisa e permitem a identificação unívoca de um registro.

Exemplo de uma tabela com primary key composta

![Modelo key-value](https://drive.google.com/uc?id=1raoOcPQ4yHLP_oyx9uA_9DGDtnAcpc0j "Primary key composta")


### Indices secundários

Componente que permite a consulta de dados na tabela usando uma chave alternativa. O Dynamo é compatível com dois tipos de índices:

- ***Indice secundário global:*** Possui uma _partition key_ e uma chave de classificação que podem ser diferentes das que existem na tabela.

- ***Índice secundário local:*** Possui a mesma _partition key_ da tabela, mas uma chave de classificação diferente.

Visualização de um índice secundário global (GSI)

![Modelo key-value](https://drive.google.com/uc?id=1ruSV7c_-EYapd9_0XBP2gz-zkv75VKuq "Índice secundário global")

---


# ***Componentes e boas práticas com Dynamo DB***

O Dynamo DB e outros NoSQL devem ser construídos não com  o foco na criação de tabelas e definição dos relacionamentos entre elas, mas com ênfase na maneira de como os dados serão acessados.

Existe um conceito chamado _***Access patterns***_ ou padrões de acesso onde são definidos os formatos para se construir as _queries_ de pesquisa.

Assim, a modelagem no DynamoDB deve ser feita pensando na maneira em como os dados serão acessados. 

É muito importante que esse princípio seja muito bem projetado, pois é muito complicado de ser alterado posteriormente. O DynamoDB não é fácil de ser remodelado depois de ser implementado.


## ***Tipos de dados*** 

### Tipos escalares
Representam um valor exato, como número, boolean, string e nulo

### Documentos
Representam uma estrutura complexa com atributos aninhados, como JSON

### Collections
Conjunto de tipos escalares

## ***Modos de leitura e gravação***

Esse tópico impacta diretamente no custo, ou seja na maneira como será cobrado. Ele vai definir o modo de cobrança por taxa de _'rendimento de leitura e gravação'_ e no modo como se gerencia a capacidade. Existem dois modos:

- ***Sob demanda:*** Opção de faturamento flexível capaz de atender centenas de solicitações por segundo sem planejamento de capacidade.

- ***Provisionado:*** Permite especificar o número de leituras/gravações por segundo, exigidas pela aplicação. 

---

# ***Pensando 'fora da caixa' com Dynamo DB***

O Amazon Dynamo DB possui características que exigem 'pensar fora da caixa' para se trabalhar com ele:

- Não é normalizado
- Não existe apenas uma entidade por tabela
- Não permite joins para pesquisa de dados
- Tabelas podem receber atributos de forma dinâmica

## ***Orientações para o projeto no DynamoDB***

Pontos a serem observados:

- ***Access patterns:*** definem como os itens serão buscados
- ***Regras de negócio:*** o DynamoDB não é flexível a alterações no modelo após a implementação.
- ***Dimensionamento:*** importante conhecer o pico das cargas de consulta, possibilitando o melhor particionamento dos dados.
- ***Atenção aos índices:*** manter os índices no mínimo. Não criar índices secundários para atributos pouco consultados.
- ***Design eficiente:*** atentar para as três propriedades fundamentais de padrões de acesso a dados: tamanho dos dados, formato dos dados e velocidade dos dados.

# ***Hands on com Dynamo DB***

## ***Roteiro:***

- Criar uma tabela no DynamoDB usando o Amazon CLI
- Inserir alguns dados
- Criar índices globais e secundários
- Realizar pesquisas

## ***Link para repositório:***

[https://github.com/cassianobrexbit/dio-live-dynamodb](https://github.com/cassianobrexbit/dio-live-dynamodb)

## ***Arquitetura da prática***

![](./img/arquitetura.png "Arquitetura proposta")

Para iniciar a criação da tabela precisei instalar o AWS CLI.

A instalação pode ser feita seguindo as orientações disponíveis no link abaixo:

[AWS Command Line Interface](https://aws.amazon.com/cli)

![](https://drive.google.com/uc?id=1uqOOKrA14WplwucsS257J_wW5XPhAYuV "Página do AWS CLI")


Para acessar remotamente o DynamoDB foi necessário instalar o AWS Cli para Linux conforme orientação da documentação da Amazon.

Basicamente os comandos foram:

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Após a instalação foi necessário configurar o AWS cli com o comando:

```
~ aws configure
```

Serão solicitadas as seguintes informações:
```
AWS Access Key ID [None]: AKIA.....7PL
AWS Secret Access Key [None]: trVZ.............5rV/
Default region name [None]: sa-east-1
Default output format [None]: json
```
As chaves de acesso e secreta foram geradas na criação do usuário com perfil administrador anteriormente com o serviço IAM.

Em seguida foram enviados os comandos para criação da tabela Music, cujos comandos foram copiados do repositório do github disponibilizado pelo instrutor Cassiano Peres.

- ***Criação da tabela Music***

```
aws dynamodb create-table \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5
```

Nos comandos acima além da criação da tabela _Music_ foram definidos:

- _Artist_ como uma chave de partição (Partition Key) e _SongTitle_ como uma chave de ordenação (Sort Key).
- A capacidade do acesso sendo 10 kB para leitura e 5kB para escrita.

Obs.: A chave de partição é definida como KeyType=HASH e a chave de ordenação como KeyType =RANGE


- ***Inserindo itens na tabela****

Para inserir um item no banco de dados DynamoDB usaremos a sequência de comandos:

```
aws dynamodb put-item \
    --table-name Music \
    --item file://itemmusic.json \
```

Observe que o item foi inserido através de um arquivo denominado itemmusic.json.

Essa estratégia foi adotada porque o aws cli pode não reconhecer alguns comandos json.

Segue abaixo o conteúdo do arquivo itemmusic.json:

```
{
  "Artist": {"S": "Iron Maiden"},
  "SongTitle": {"S": "Chains of Misery"},
  "AlbumTitle": {"S": "Fear of the Dark"},
  "SongYear": {"S": "1992"}
}
```

Conferindo o resultado no DynamoDB:

![](https://drive.google.com/uc?id=123fHBjnpdApAYSxiBBa4vYI6ZQQzREWe "Item inserido")

Para inserir vários itens usaremos o comando abaixo:

```
aws dynamodb batch-write-item \
    --request-items file://batchmusic.json
```

O arquivo batch.json contem vários itens como pode ser visto abaixo:

```
{
    "Music": [
        {
            "PutRequest": {
                "Item": {
                  "Artist": {"S": "Iron Maiden"},
                  "SongTitle": {"S": "Wasting Love"},
                  "AlbumTitle": {"S": "Fear of the Dark Live"},
                  "SongYear": {"S": "1992"}
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                  "Artist": {"S": "Iron Maiden"},
                  "SongTitle": {"S": "Weekend Warrior"},
                  "AlbumTitle": {"S": "Fear of the Dark"},
                  "SongYear": {"S": "1992"}
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                  "Artist": {"S": "Iron Maiden"},
                  "SongTitle": {"S": "Fear of the Dark"},
                  "AlbumTitle": {"S": "Fear of the Dark Tour"},
                  "SongYear": {"S": "1992"}
                }
            }
        }
      ]
}

```
Após o comando verificamos o resultados das múltiplas inserções no DynamoDB:

![](https://drive.google.com/uc?id=1OXrW9-ccKnVhf0vpRwbL7rtS-3bWq6iq "Vários itens inseridos com batch")

- ***Criar um index global secundário baseado no título do álbum***

```
aws dynamodb update-table \
    --table-name Music \
    --attribute-definitions AttributeName=AlbumTitle,AttributeType=S \
    --global-secondary-index-updates \
        "[{\"Create\":{\"IndexName\": \"AlbumTitle-index\",\"KeySchema\":[{\"AttributeName\":\"AlbumTitle\",\"KeyType\":\"HASH\"}], \
        \"ProvisionedThroughput\": {\"ReadCapacityUnits\": 10, \"WriteCapacityUnits\": 5      },\"Projection\":{\"ProjectionType\":\"ALL\"}}}]"
```

Visualizando alteração no AWS DynamoDB Console:

![](https://drive.google.com/uc?id=1_I0Y4FzGd8TzKOlIVuHpxTgEnVHkMMtX "Indice Global secundário")


- ***Criar um index global secundário baseado no nome do artista e no título do álbum***

Para criar esse novo índice enviaremos o comando abaixo no AWS CLI:

```
aws dynamodb update-table \
    --table-name Music \
    --attribute-definitions\
        AttributeName=Artist,AttributeType=S \
        AttributeName=AlbumTitle,AttributeType=S \
    --global-secondary-index-updates \
        "[{\"Create\":{\"IndexName\": \"ArtistAlbumTitle-index\",\"KeySchema\":[{\"AttributeName\":\"Artist\",\"KeyType\":\"HASH\"}, {\"AttributeName\":\"AlbumTitle\",\"KeyType\":\"RANGE\"}], \
        \"ProvisionedThroughput\": {\"ReadCapacityUnits\": 10, \"WriteCapacityUnits\": 5      },\"Projection\":{\"ProjectionType\":\"ALL\"}}}]"

```
Verificação no AWS DynamoDB Console:

![](https://drive.google.com/uc?id=1CrHgVA7yXvbRyLJ0U1qphi1xb_XQAdTH "Indice secundario por Artista e Título")

Vamos então efetuar algumas pesquisas já que criamos os índices globais secundários:

- ***Pesquisar um item pelo nome do artista***

```
aws dynamodb query \
    --table-name Music \
    --key-condition-expression "Artist = :artist" \
    --expression-attribute-values  '{":artist":{"S":"Iron Maiden"}}'
```
Obtemos o seguinte resultado:

```
{
    "Items": [
        {
            "AlbumTitle": {
                "S": "Fear of the Dark"
            },
            "Artist": {
                "S": "Iron Maiden"
            },
            "SongYear": {
                "S": "1992"
            },
            "SongTitle": {
                "S": "Chains of Misery"
            }
        },
        {
            "AlbumTitle": {
                "S": "Fear of the Dark Tour"
            },
            "Artist": {
                "S": "Iron Maiden"
            },
            "SongYear": {
                "S": "1992"
            },
            "SongTitle": {
                "S": "Fear of the Dark"
            }
        },
        {
            "AlbumTitle": {
                "S": "Fear of the Dark Live"
            },
            "Artist": {
                "S": "Iron Maiden"
            },
            "SongYear": {
                "S": "1992"
            },
            "SongTitle": {
                "S": "Wasting Love"
            }
        },
        {
            "AlbumTitle": {
                "S": "Fear of the Dark"
            },
            "Artist": {
                "S": "Iron Maiden"
            },
            "SongYear": {
                "S": "1992"
            },
            "SongTitle": {
                "S": "Weekend Warrior"
            }
        }
    ],
    "Count": 4,
    "ScannedCount": 4,
    "ConsumedCapacity": null
}
```
- ***Pesquisando pelo index secundario baseado no título do álbum***

```
aws dynamodb query \
    --table-name Music \
    --index-name AlbumTitle-index \
    --key-condition-expression "AlbumTitle = :name" \
    --expression-attribute-values  '{":name":{"S":"Fear of the Dark"}}'

```
Resposta do comando:

```
{
    "Items": [
        {
            "AlbumTitle": {
                "S": "Fear of the Dark"
            },
            "Artist": {
                "S": "Iron Maiden"
            },
            "SongYear": {
                "S": "1992"
            },
            "SongTitle": {
                "S": "Weekend Warrior"
            }
        },
        {
            "AlbumTitle": {
                "S": "Fear of the Dark"
            },
            "Artist": {
                "S": "Iron Maiden"
            },
            "SongYear": {
                "S": "1992"
            },
            "SongTitle": {
                "S": "Chains of Misery"
            }
        }
    ],
    "Count": 2,
    "ScannedCount": 2,
    "ConsumedCapacity": null
}
```
- ***Criar um index global secundário baseado no título da música e no ano***

```
aws dynamodb update-table \
    --table-name Music \
    --attribute-definitions\
        AttributeName=SongTitle,AttributeType=S \
        AttributeName=SongYear,AttributeType=S \
    --global-secondary-index-updates \
        "[{\"Create\":{\"IndexName\": \"SongTitleYear-index\",\"KeySchema\":[{\"AttributeName\":\"SongTitle\",\"KeyType\":\"HASH\"}, {\"AttributeName\":\"SongYear\",\"KeyType\":\"RANGE\"}], \
        \"ProvisionedThroughput\": {\"ReadCapacityUnits\": 10, \"WriteCapacityUnits\": 5      },\"Projection\":{\"ProjectionType\":\"ALL\"}}}]"
```

Resposta do comando enviado pelo AWS CLI:

```
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "AlbumTitle",
                "AttributeType": "S"
            },
            {
                "AttributeName": "Artist",
                "AttributeType": "S"
            },
            {
                "AttributeName": "SongTitle",
                "AttributeType": "S"
            },
            {
                "AttributeName": "SongYear",
                "AttributeType": "S"
            }
        ],
        "TableName": "Music",
        "KeySchema": [
            {
                "AttributeName": "Artist",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "SongTitle",
                "KeyType": "RANGE"
            }
        ],
        "TableStatus": "UPDATING",
        "CreationDateTime": "2022-11-17T23:26:59.834000-03:00",
        "ProvisionedThroughput": {
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 5
        },
        "TableSizeBytes": 325,
        "ItemCount": 4,
        "TableArn": "arn:aws:dynamodb:sa-east-1:563620716536:table/Music",
        "TableId": "b7b4936a-57e5-4de7-ad18-f8aafeb03e46",
        "GlobalSecondaryIndexes": [
            {
                "IndexName": "AlbumTitle-index",
                "KeySchema": [
                    {
                        "AttributeName": "AlbumTitle",
                        "KeyType": "HASH"
                    }
                ],
                "Projection": {
                    "ProjectionType": "ALL"
                },
                "IndexStatus": "ACTIVE",
                "ProvisionedThroughput": {
                    "NumberOfDecreasesToday": 0,
                    "ReadCapacityUnits": 10,
                    "WriteCapacityUnits": 5
                },
                "IndexSizeBytes": 0,
                "ItemCount": 0,
                "IndexArn": "arn:aws:dynamodb:sa-east-1:563620716536:table/Music/index/AlbumTitle-index"
            },
            {
                "IndexName": "ArtistAlbumTitle-index",
                "KeySchema": [
                    {
                        "AttributeName": "Artist",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "AlbumTitle",
                        "KeyType": "RANGE"
                    }
                ],
                "Projection": {
                    "ProjectionType": "ALL"
                },
                "IndexStatus": "ACTIVE",
                "ProvisionedThroughput": {
                    "NumberOfDecreasesToday": 0,
                    "ReadCapacityUnits": 10,
                    "WriteCapacityUnits": 5
                },
                "IndexSizeBytes": 0,
                "ItemCount": 0,
                "IndexArn": "arn:aws:dynamodb:sa-east-1:563620716536:table/Music/index/ArtistAlbumTitle-index"
            },
            {
                "IndexName": "SongTitleYear-index",
                "KeySchema": [
                    {
                        "AttributeName": "SongTitle",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "SongYear",
                        "KeyType": "RANGE"
                    }
                ],
                "Projection": {
                    "ProjectionType": "ALL"
                },
                "IndexStatus": "CREATING",
                "Backfilling": false,
                "ProvisionedThroughput": {
                    "NumberOfDecreasesToday": 0,
                    "ReadCapacityUnits": 10,
                    "WriteCapacityUnits": 5
                },
                "IndexSizeBytes": 0,
                "ItemCount": 0,
                "IndexArn": "arn:aws:dynamodb:sa-east-1:563620716536:table/Music/index/SongTitleYear-index"
            }
        ]
    }
}
```
Verificando a criação do índice na Console do Dynamo DB:

![](https://drive.google.com/uc?id=16Rsh4v8LQKdWKYFpLdORlPvzGlS50BVf "Criação de pesquisa pelo indice secundario baseado no título da música e no ano")

- ***Pesquisa pelo index secundário baseado no título da música e no ano***

```
aws dynamodb query \
    --table-name Music \
    --index-name SongTitleYear-index \
    --key-condition-expression "SongTitle = :v_song and SongYear = :v_year" \
    --expression-attribute-values  '{":v_song":{"S":"Wasting Love"},":v_year":{"S":"1992"} }'
```
Resposta no AWS CLI:  

```
{
    "Items": [
        {
            "AlbumTitle": {
                "S": "Fear of the Dark Live"
            },
            "Artist": {
                "S": "Iron Maiden"
            },
            "SongTitle": {
                "S": "Wasting Love"
            },
            "SongYear": {
                "S": "1992"
            }
        }
    ],
    "Count": 1,
    "ScannedCount": 1,
    "ConsumedCapacity": null
}
```

### ***References***


https://www.intodeeplearning.com/embedding-images-in-google-drive-to-markdown/
























