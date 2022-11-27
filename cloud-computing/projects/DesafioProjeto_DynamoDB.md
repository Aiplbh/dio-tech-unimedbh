# ***Desafio de Projeto com Dynamo DB***

Elaborado por [Argemiro Leite](https://github.com/aiplbh) como parte dos desafios de projeto propostos no Bootcamp Geração Tech Unimed-BH - Data Science

<center>Novembro / 2022</center>

```
Digital Innovation One - DIO
Geração Tech Unimed -BH Ciência de dados
Módulo    : Imersão Cloud Computing    
Submódulo : Boas práticas com DynamoDB
Orientador: Cassiano Peres - CTO Brexbit
```
## ***Descrição do Desafio***

Características Relacionais (SQL) e Não Relacionais (NoSQL) usando o mesmo banco de dados? Isso é possível? Com o DynamoDB sim! Entenda um pouco das possibilidades desse banco de dados totalmente gerenciado da AWS. Para isso, nosso super expert apresenta uma série de boas práticas para o DynamoDB em um desafio totalmente prático. Sendo assim, você poderá reproduzir essa solução e, caso queira ir além, implementar suas próprias evoluções e melhorias 

## ***Introdução***

O Amazon DynamoDB é um banco de dados de chave-valor NoSQL, sem servidor e totalmente gerenciado, projetado para executar aplicações de alta performance em qualquer escala. O DynamoDB oferece segurança integrada, backups contínuos, replicação multirregional automatizada, armazenamento em cache na memória e ferramentas de importação e exportação de dados.

## ***Objetivo***

Reproduzir as etapas de criação de uma tabela no banco de dados não relacional (NoSQL) Amazon DynamoDB desenvolvido pela AWS para conhecimento desse tipo de banco de dados, além de explorar boas práticas de modelagem, otimizar desempenho e custos. Para atingimento deste objetivo proposto as seguintes etapas constantes na seção "_Roteiro_" serão desenvolvidas. 

### ***Roteiro***
Com o intuito de implementar as boas práticas aprendidas duranto o teinamento ministrado pelo Prof. Cassiano Peres as seguintes etapas serão desenvolvidas:

- Criar uma tabela no DynamoDB usando o Amazon CLI
- Inserir alguns dados
- Criar índices globais e secundários
- Realizar pesquisas

### ***Link para repositório de referência:***

[https://github.com/cassianobrexbit/dio-live-dynamodb](https://github.com/cassianobrexbit/dio-live-dynamodb)

## ***Desenvolvimento***

### ***Arquitetura da prática***

![](./img/arquitetura.png "Arquitetura proposta")

Para iniciar a criação da tabela foi instalado o AWS CLI em uma versão Linux Ubuntu do WSL (Windows Subsystem Linux)

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
## ***Conclusão***

O DynamoDB oferece suporte a modelos de dados de documentos e chave/valor. Isso permite que o DynamoDB tenha um esquema flexível, por isso, cada linha pode ter qualquer número de colunas a qualquer momento. Isso permite que você adapte as tabelas facilmente à medida que seus requisitos comerciais mudam, sem a necessidade de redefinir o esquema de tabelas como você faria em bancos de dados relacionais.

Pode ser verificado através dos exemplos que o uso de índices secundários favorecem a busca de resultados, porém seu uso deve ser bem avaliado ainda na fase de projeto do banco de dados, uma vez que alterações estruturais podem ter grande impacto na reestruturação do schema.


### ***References***


https://www.intodeeplearning.com/embedding-images-in-google-drive-to-markdown/

https://aws.amazon.com/pt/dynamodb/getting-started/
