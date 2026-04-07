# 📌 Módulo: Banco de Dados Relacional

Este módulo aborda os fundamentos de bancos de dados relacionais, SQL e modelagem de dados.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Compreender o conceito e a importância de bancos de dados relacionais
- Diferenciar os tipos de bancos de dados e SGBDs disponíveis no mercado
- Aplicar os comandos SQL nas categorias DDL, DML, DQL, DCL e DTL
- Criar modelos conceituais utilizando MER/DER com entidades, atributos e relacionamentos
- Configurar um ambiente de banco de dados na nuvem (CloudClusters)

---

# 📚 Conteúdos Abordados

## 🔹 Introdução aos Bancos de Dados

Um banco de dados é um sistema estruturado para armazenar, organizar e gerenciar informações de forma eficiente e segura.

### Tipos de bancos de dados

- Relacional/SQL
- Não Relacionais/NoSQL (Not OnlySQL)
- Orientado a objetos
- Hierárquico

### SGBD (Sistema de Gerenciamento de Banco de Dados)

Um SGBD é um software responsável por criar, organizar, armazenar, consultar, deletar, editar e proteger os dados dentro de um banco de dados, funcionando como um administrador central dos dados. Ele permite que usuários e aplicações interajam com os dados sem precisar gerenciar manualmente a estrutura ou a persistência das informações.

- PostgreSQL
- MySQL
- SQLite
- MariaDB
- mongoDB

### Características de um BDR

- Relacionamento entre tabelas
- Linguagem de Consulta Estruturada (SQL)
- Integridade Referencial
- Normalização de dados
- Segurança
- Flexibilidade e extensibilidade
- Suporte a transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade)

## 🔹 Introdução ao SQL

O SQL (Structured Query Language), ou Linguagem de Consulta Estruturada, é uma linguagem de programação usada para gerenciar e manipular dados em bancos de dados relacionais. Esses bancos armazenam informações em tabelas organizadas em linhas e colunas, permitindo que os dados sejam acessados, atualizados e analisados de forma eficiente.

Criado na década de 1970 pela IBM, o SQL foi projetado para simplificar o acesso a dados em sistemas complexos. Ele se tornou um padrão oficial em 1986 pelo ANSI (American National Standards Institute) e continua sendo amplamente utilizado em sistemas como MySQL, PostgreSQL, Oracle e Microsoft SQL Server.

### Organização do SQL

**1. DDL (Data Definition Language)**

A Linguagem de Definição de Dados (DDL) é responsável pela definição e gerenciamento da estrutura do banco de dados. Os principais comandos DDL incluem:
CREATE: Cria novos objetos no banco de dados, como tabelas e índices.
ALTER: Modifica a estrutura de objetos existentes.
DROP: Remove objetos do banco de dados.

Exemplo de comando DDL:

```sql
CREATE TABLE usuarios (
id INT PRIMARY KEY,
nome VARCHAR(100),
email VARCHAR(100)
);
```

**2. DML (Data Manipulation Language)**

A Linguagem de Manipulação de Dados (DML) é utilizada para manipular os dados dentro das tabelas. Os principais comandos DML incluem:
INSERT: Insere novos dados em uma tabela.
UPDATE: Modifica dados existentes em uma tabela.
DELETE: Remove dados de uma tabela.

Exemplo de comando DML:

```sql
INSERT INTO usuarios (nome, email) VALUES ('João', 'joao@example.com');
UPDATE usuarios SET email = 'joao.novo@example.com' WHERE nome = 'João';
DELETE FROM usuarios WHERE nome = 'João';
```

**3. DQL (Data Query Language)**

A Linguagem de Consulta de Dados (DQL) é utilizada para consultar e recuperar dados do banco de dados. O principal comando DQL é:
SELECT: Recupera dados de uma ou mais tabelas.

Exemplo de comando DQL:

```sql
SELECT * FROM usuarios WHERE email LIKE '%@example.com';
```

**4. DCL (Data Control Language)**

Linguagem de Controle de Dados (DCL), que é usada para controlar o acesso e gerenciar permissões de usuários no banco de dados. Os principais comandos DCL incluem:
GRANT: Concede privilégios a usuários.
REVOKE: Remove privilégios de usuários.

Essas sub-linguagens trabalham juntas para permitir a definição, manipulação, consulta e controle de bancos de dados relacionais de forma eficiente.

**5. DTL (Data Transaction Language)**

Linguagem de Transação de dados. Ela agrupa os comandos usados para controle de transações no banco de dados, garantindo que operações sejam executadas de forma consistente e segura.

| Comando | Função |
|---------|--------|
| BEGIN TRANSACTION / START TRANSACTION | Inicia uma nova transação. |
| COMMIT | Confirma todas as operações realizadas na transação, tornando-as permanentes no banco. |
| ROLLBACK | Desfaz todas as operações realizadas desde o último BEGIN ou SAVEPOINT. |
| SAVEPOINT | Cria um ponto de restauração dentro da transação para permitir rollback parcial. |
| SET TRANSACTION | Define características da transação (como nível de isolamento). |

## 🔹 Introdução a Modelagem de Dados (MER e DER)

O MER (Modelo Entidade-Relacionamento) é representado através de diagramas chamados de Diagramas Entidade-Relacionamento (DER).

### Entidades

São nomeadas com substantivos concretos ou abstratos que representam de forma clara sua função dentro do domínio.

### Atributos

São as características e propriedades de cada entidade. Eles descrevem informações específicas sobre uma entidade.

### Relacionamentos

Os relacionamentos representam associações entre entidades.

### Cardinalidade

Forma como as entidades se relacionam uma com as outras, indica o número máximo de instâncias ou ocorrências que podemos ter em uma entidade relacionada com outra entidade.

- Relacionamento 1..1 (um para um)
- Relacionamento 1..n ou 1..* (um para muitos)
- Relacionamento n..n ou *..* (muitos para muitos)

**Cardinalidade máxima:** Trata-se do número máximo de instâncias de entidade que podem participar em um relacionamento. Pode ser 1 ou N (muitos).

**Cardinalidade mínima:** Número mínimo de instâncias de entidade que devem obrigatoriamente participar em um relacionamento; zero é participação opcional e um é obrigatória.

### Exemplo de diagrama

Exemplo de diagrama com entidades, relacionamentos e cardinalidade feito em módulo.

Pode ser encontrado na pasta [Diagramas](../3-BDR-ETL/1-BD-Relacional/Diagramas/Diagrama_1.png)

## 🔹 Configuração de Ambiente

Acesse a URL: https://clients.cloudclusters.io e crie sua conta.

Você terá acesso a 7 dias gratuitos.

Clique em New Application > MariaDB.

Após criar com o plano gratuito, aguarde o serviço ficar disponível.

Clique para configurar o seu banco de dados.

Menu > DB & User > Create Database.

Crie o Database.

Menu > DB & User > Create User.

Crie o Usuário.

Agora vá no submenu > phpMyAdmin > Launch. Utilize as credenciais criadas para acessar.

Pronto, nosso ambiente está criado.

---

# 🧠 Boas Práticas

- Utilizar SGBDs apropriados para cada necessidade (PostgreSQL, MySQL, SQLite, MariaDB, mongoDB)
- Aplicar normalização de dados para evitar redundância
- Garantir integridade referencial entre tabelas relacionadas
- Utilizar transações ACID para operações que exigem consistência
- Documentar o modelo DER antes da implementação
- Seguir os princípios de segurança no gerenciamento de bancos de dados

---

# ⚠️ Pontos de Atenção

- Entender a diferença entre bancos relacionais e NoSQL antes de escolher uma tecnologia
- Compreender corretamente os conceitos de cardinalidade mínima e máxima na modelagem
- Diferenciar os comandos DDL, DML, DQL, DCL e DTL para não usar o comando errado
- Cuidado com transações: sempre usar COMMIT ou ROLLBACK para não deixar transações abertas
- Atenção às cardinalidades 1..1, 1..n e n..n para não modelar relacionamentos incorretamente
- No CloudClusters, lembrar que o período gratuito é de apenas 7 dias

---

# 🧪 Exemplos Práticos

**Exemplo de transação com COMMIT e ROLLBACK:**

```sql
START TRANSACTION;
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT; -- Confirma a transferência
-- Ou ROLLBACK; -- Desfaz em caso de erro
```

**Exemplo de criação de tabela com chave estrangeira:**

```sql
CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    cliente_id INT,
    data_pedido DATE,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

---

# 🚀 Conclusão

Este módulo apresentou os fundamentos essenciais de bancos de dados relacionais, incluindo conceitos de SGBD, características ACID, organização do SQL em DDL, DML, DQL, DCL e DTL, além de modelagem de dados com MER/DER e cardinalidades. Também foi configurado um ambiente prático no CloudClusters. Esses conhecimentos são base para trabalhar com armazenamento e consulta de dados em aplicações reais.

---

> [🏠 Voltar ao índice](../../README.md) | [⬇ Próximo módulo: SQL Básico](../2-SQL-Basico/README.md)
