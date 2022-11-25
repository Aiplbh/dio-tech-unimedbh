# ***Projeto Conceitual de Banco de Dados – E-COMMERCE***


## ***Descrição do desafio***

O esquema deverá ser adicionado a um repositório do Github para futura avaliação do desafio de projeto. Adicione ao Readme a descrição do projeto conceitual para fornecer o contexto sobre seu esquema.

## ***Objetivo***
 
Refine o modelo apresentado acrescentando os seguintes pontos:

- Cliente PJ e PF: Uma conta pode ser PJ ou PF, mas não pode ter as duas informações;
- Pagamento: Pode ter cadastrado mais de uma forma de pagamento;
- Entrega: Possui status e código de rastreio;


Agora é a sua vez de ser o protagonista! Implemente o desafio sugerido pela expert e suba seu projeto para um repositório próprio, com isso, você aumentará ainda mais seu portfólio de projetos no GitHub!

## ***Levantamento de requisitos***

### Escopo do projeto: Venda de produtos

Entidades inferidas:

- Produto
- Estoque
- Cliente
- Pedido
- Fornecedor

Cliente faz um pedido que contem produtos. Esse produto pode estar em estoque ou não e está associado a um fornecedor.

***Narrativas - Produtos***

- Os _***produtos***_ são vendidos por uma única plataforma online, mas podem ter _***vendedores***_ distintos.
- Cada  _***produto***_ possui um _***fornecedor***_ .
- Um ou mais _***produtos***_ podem compor um _***pedido***_.


***Narrativas - Cliente***

- O _***cliente***_ pode se cadastrar no site com seu _***CPF***_ ou  _***CNPJ***_.
- O endereço do   _***cliente***_ irá determinar o valor do _***frete***_.
- Um _***cliente***_ pode fazer mais de um _***pedido***_ e terá um prazo de carência para devolução do _***produto***_.


***Narrativas - Pedido***

- Os _***pedidos***_ são criados por _***clientes***_ e possuem informações da compra, endereço e status da entrega.
- O _***pedido***_ pode ser cancelado.


***Narrativas - Fornecedores e estoque***

