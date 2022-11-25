# ***DIO - Geração Tech Unimed-BH - Ciência de Dados***

Notas de aula de [Argemiro Leite](https://github.com/Aiplbh) durante o bootcamp  Geração Tech da [Unimed-BH](https://portal.unimedbh.com.br/wps/portal/corp/unimedbh/trabalhe_conosco) em parceria com a [DIO](https://web.dio.me/)

## ***Módulo: Imersão Cloud Computer***

```
Módulo: Boas práticas com DynamoDB [Banco NoSQL]
Instrutor: Cassiano Peres - Brexit
```

## ***Conhecendo o AWS IAM***


IAM = Identity and Access  Manager

Permite o gerenciamento seguro do acesso aos serviços e recurso da AWS por meio da criação de usuários, grupos de usuários e permissões.


## ***Recursos do IAM***

- Acesso compartilhado
- Permissões granulares: níveis de acesso de acordo com as funções cadastradas.
- MFA: Autenticação de múltiplos fatores
- Identidades federadas: credenciais podem ser importadas de outros provedores de identidade
- Integração com serviços AWS: define níveis de permissão de aceso aos serviços AWS
- Gratuidade: não possui custos ou limite de uso

## ***Termos e conceitos***

- Identity: Fornece acesso a uma conta na AWS
- IAM Users: Representa uma pessoa ou serviço que usa
- User Groups: Coleção de usuários IAM: testers, admnistradores, clientes
- IAM roles: Conjunto de permissões que determinam o nível de acesso de uma ID aos serviços AWS

	- Inline policy: atreladas diretamente a uma identidade

	- Managed policy: conjunto de policies disponíveis para várias identidades

- IAM policies: São definidas em formato JSON. Define o efeito, as ações e os recursos habilitados

- IAM permissions: Nível mais baixo da hierarquia, determina se uma ID pode ou não tomar uma ação na AWS.

## ***Boas práticas de utilização do IAM***

1. conta raiz: não utilizar em tarefas diária

2. usuarios: crie usuários individuais

3. privilégios mínimos: prover apenas o nível de acesso necessãrio

4. permissões: usar grupos de usuários com permissões

5. autidoria: ativar AWS Cloud Trail

6. senhas: use senhas fortes [com caracteres especiais]

7. MFA: ative MFA para usuários privilegiados

## ***Criação de usuários no IAM***

- Acessar o IAM

  https://console.aws.amazon.com/iamv2/home?#/users

  conta AWS numero: [563xxxxxxx36]

  ai.........rbh@gmail.com | C...........7


- Criar um novo usuário

  adminuser | A.............1

- Gerar credenciais

- Atribuir permissões

- Acessar o console com o novo usuário criado 

- Testar permissões de acesso atribuídas


## ***Criando grupos de usuários no IAM***


1. Habilitar o MFA para o root

   - Escolher o Virtual MFA

   - Scanear os 2 QR Code gerados na AWS com o dispositivo móvel

   - Instalei o Google Authenticator para isso

   - Confirme os dois QR gerados e clique em [Assign MFA]

   - Ativar as chaves de acesso para o root [Recomendado]


2. Clicar em USERS > [Add User]

   - Colocar nome: adminuser


   - Tipo de acesso: Marque as duas opções:

	✅ Access Ky - Acesso programático
	
	✅ Password - AWS Management Console access


   - Console password:

	( ) Autogerada

	(x) Definida pelo usuário

       [ A----------1 ]

   - Exigir ou não reset da senha no primeiro uso e clicar em [Next permitions]


3. Setar permissões: há tres possibilidades

   - add user to group

   - copia permissões de um grupo já criado

   - anexar políticas existentes diretamente [ vou marcar essa opção]

	- escolher perfil de administrator [primeira opção]: as permissões são apresentadas no formato JSON. Ex.:

      ```
       {

           "Version": "2022-10-17"

	     "Statement": [

		   {
			"Effect": "Alow",
			
			"Action": "*",

			"Resources": "*"
		   }
	      ]
       }
      ```

   - Adicionar tags [optional]  
         
         São informações do tipo chave-valor sobre o seu usuário. Por exemplo: 
         job title, email, address, etc. 

	  Clicar no botão [Next review]

	  Clicar em [Create user]

      
   - Se tudo correu bem será apresentada uma tela de ***```Success```***

   - Anote o link para acesso a console fornecida

   - Anote a chave de acesso

   - Anote a chave secreta 

   - Envie um email com instruções de login


   - ⚠️⚠️⚠️ Faça o download.csv que tem todas as informações carregadas

   - Clicar em [Close]


## ***Logando com o novo user criado e revendo as políticas de acesso***


1. Use o link de acesso a console gerado anteriormente

2. Faça o login [usuario] [password] [entrar]

3. Redefinir a senha [Confirm]

4. Trabalhar a criação de um novo usuário (devuser) e atribuir permissões a ele


## ***Criação de grupos e funçoes [roles]***


1. Dashboard - Access management

2. User groups

3. Clicar em Create groups [Create group]

4. Nomear o Grupo [Developers]

5. Adicione o usuário desejado [Next]

6. Associe políticas de permissões ao group 

7. Pesquisar pelo BD Dynamo da full access selecionado a política:

   - AmazonDynamoDBFullAccess

8. Procure lambda e selecione a opção:

   - AWSLambda_FullAccess

9. Clicar em [create group]


Repetir o processo agora para criar um grupo de administradores


1. Criar um novo grupo de admnistradores [Create group]

2. Nomear o grupo: [Administrators]

3. Adicionar o usuário ao grupo: [AdminUsers]

4. [Close]

Após criar os dois tipos de usuários foi feita a tentativa de acesso a serviços para
os quais os usuários não estavam autorizados e confirmados o recebimento de mensagens
de alerta impedindo o acesso


## ***Criação de grupos e funçoes [roles] personalizadas***

Uma política é um objeto que ao ser associado a uma ID ou Resource define permissões.

Uma função [role] é uma identidade da AWS com políticas associadas de permissão que 
determinam quais ações podem ou não serem executadas.


1. Logar com o usuário que possui acesso como Administrador

2. Acessar o Dashboard do IAM

3. Selecionar Roles no menu lateral

4. Create role

5. Escolher uma role dentre 4 opções:

   - AWS service ............. [vamos usar essa]

   - Another AWS account

   - Web identity

   - SAML 2.0 Federation


6. Selecionar trabalhar com funões lambda e [Next to permissions]

7. Create role

   - Clicar no botão [Create policy]

   - Nessa tela deverão ser especificados 4 itens:

         . Services: [ex. S3]

         . Actions: [ex. ListBucket]

         . Resources: [ex. Specific  bucket    [x] any

         . Request conditions: [ex. none optional]


   - Revisar a politica e nomeá-la: [ex.: s3LimitedActions]

   - Dar uma descrição

   - Procurar em filtrar politica e as politicas criadas acima devem aparecer

   - Selecionar , verificar e nomear a Role: [s3LimitedActionsRole]


8. Atrelar essa função criada a um grupo de usuários

   - User groups > Developers > selecionar o Usuário DevConsole
