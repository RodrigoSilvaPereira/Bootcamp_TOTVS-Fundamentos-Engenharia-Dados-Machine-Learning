# 📌 Módulo: SQL Básico

Este módulo aborda os comandos fundamentais do SQL para manipulação e consulta de dados em bancos de dados relacionais.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Compreender a estrutura de tabelas, colunas e registros em bancos relacionais
- Criar tabelas utilizando os tipos de dados e opções adequadas
- Executar operações CRUD (INSERT, SELECT, UPDATE, DELETE)
- Utilizar cláusulas WHERE e LIKE para filtros avançados
- Alterar e excluir tabelas com ALTER TABLE e DROP TABLE
- Implementar Primary Keys e Foreign Keys para integridade referencial

---

# 📚 Conteúdos Abordados

## 🔹 Modelagem de Dados Relacionais

### Tabelas

Usado para armazenar os dados de forma organizada, nomenclatura única e divisão de colunas e linhas.

### Colunas

Estrutura dentro da tabela que representa um atributo específico dos dados armazenados. Cada coluna tem um nome único e um tipo de dados associado que define o tipo de informação que pode ser armazenado nela, como números, textos, datas, etc.

### Registro

Um registro, conhecido como linha ou tupla, é uma instância individual de dados em uma tabela.

## 🔹 Comandos Básicos SQL

```sql
CREATE TABLE {{nome}}
    ({{coluna}} {{tipo}} {{opções}} COMMENT '{{COMENTÁRIO}}');
```

### Tipos de Dados

Os dados podem variar muito entre os diversos SGBD, os mais comuns são:

- Integer
- Decimal/Numeric
- Character/Varchar
- Date/Time
- Boolean
- Text

### Opções (Create Table)

- Restrições de valor:
    - NOT NULL
    - UNIQUE
    - DEFAULT
- Chaves primárias e estrangeiras
- Auto Incremento

## 🔹 Criando uma Tabela

No banco viagens, criado no módulo anterior, clique na Aba > SQL

```sql
CREATE TABLE usuarios (
  id INT,
  nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
  email VARCHAR(255) NOT NULL UNIQUE COMMENT 'Endereço de e-mail do usuário',
  data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário',
  endereco VARCHAR(50) NOT NULL COMMENT 'Endereço do Cliente'
);

CREATE TABLE viagens.destinos (
  id INT,
  nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'Nome do destino',
  descricao VARCHAR(255) NOT NULL COMMENT 'Descrição do destino'
);

CREATE TABLE viagens.reservas (
  id INT COMMENT 'Identificador único da reserva',
  id_usuario INT COMMENT 'Referência ao ID do usuário que fez a reserva',
  id_destino INT COMMENT 'Referência ao ID do destino da reserva',
  data DATE COMMENT 'Data da reserva',
  status VARCHAR(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confirmada, pendente, cancelada, etc.)'
);
```

## 🔹 Operações CRUD

### Comando INSERT

INSERT INTO {{nome-tabela}} ([coluna1, coluna2, ...]) **Você pode ocultar as colunas**

VALUES ([valor-coluna1, valor-coluna2, ...])

#### Código para inserir

```sql
INSERT INTO viagens.usuarios (id, nome, email, data_nascimento, endereco) VALUES 
(1, 'João Silva', 'joao@example.com', '1990-05-15', 'Rua A, 123, Cidade X, Estado Y'),
(2, 'Maria Santos', 'maria@example.com', '1985-08-22', 'Rua B, 456, Cidade Y, Estado Z'),
(3, 'Pedro Souza', 'pedro@example.com', '1998-02-10', 'Avenida C, 789, Cidade X, Estado Y');

INSERT INTO viagens.destinos (id, nome, descricao) VALUES 
(1, 'Praia das Tartarugas', 'Uma bela praia com areias brancas e mar cristalino'),
(2, 'Cachoeira do Vale Verde', 'Uma cachoeira exuberante cercada por natureza'),
(3, 'Cidade Histórica de Pedra Alta', 'Uma cidade rica em história e arquitetura');

INSERT INTO viagens.reservas (id, id_usuario, id_destino, data, status) VALUES 
(1, 1, 2, '2023-07-10', 'confirmada'),
(2, 2, 1, '2023-08-05', 'pendente'),
(3, 3, 3, '2023-09-20', 'cancelada');
```

### Comando SELECT

SELECT {{lista_colunas}} FROM tabela;

Lembrando que o * retorna todas as colunas.

#### Código para Selecionar

```sql
SELECT * FROM usuarios;
SELECT nome, email FROM usuarios;
```

### Comando SELECT com WHERE

SELECT {{lista_colunas}} FROM tabela WHERE {{condicao}}

#### Código para Selecionar com WHERE

```sql
-- Selecionar os usuários que possuem o nome "João Silva"
SELECT * FROM usuarios WHERE nome = 'João Silva';

-- Selecionar os usuários que nasceram antes de uma determinada data
SELECT * FROM usuarios WHERE data_nascimento < '1990-01-01';
```

### Comando SELECT com LIKE

SELECT {{lista_colunas}} FROM tabela WHERE coluna LIKE {{valor}} 

*Pode-se utilizar o % para representar caracteres curinga*

#### Código para Selecionar com LIKE

```sql
SELECT * FROM usuarios WHERE nome LIKE '%Silva%';
SELECT * FROM usuarios WHERE nome LIKE 'Jo_o%';
```

### Comando UPDATE

UPDATE {{tabela}} SET {{coluna_1}} = {{novo_valor_1}}, {{coluna_2}} = {{novo_valor_2}} WHERE {{condicao}};

#### Código para realizar UPDATE

```sql
UPDATE usuarios SET endereco = 'Nova Rua, 123' WHERE email = 'joao@example.com';
```

### Comando DELETE

DELETE FROM {{tabela}} WHERE {{condicao}};

#### Código para realizar DELETE

```sql
DELETE FROM reservas WHERE status = 'cancelada';
```

## 🔹 Alterando e Excluindo Tabelas

A cláusula ALTER TABLE é usada no SQL para modificar a estrutura de uma tabela existente de um banco de dados relacional.

A cláusula DROP TABLE é usada no SQL para excluir uma tabela em um banco de dados relacional.

### Exemplo de código alterando e excluindo tabela

```sql
-- Criando nova tabela --
CREATE TABLE usuarios_nova (
  id INT,
  nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
  email VARCHAR(255) NOT NULL UNIQUE COMMENT 'Endereço de e-mail do usuário',
  data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário',
  endereco VARCHAR(100) NOT NULL COMMENT 'Endereço do Cliente'
);

-- Migrando os dados --
INSERT INTO usuarios_nova
SELECT * from usuarios;

-- Excluindo tabela anterior --
DROP TABLE usuarios;

-- Renomeando nova tabela --
ALTER TABLE usuarios_nova RENAME usuarios;

-- Ou opção 2: Alterar tamanho da coluna endereço --
ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(100);
```

## 🔹 Primary Keys e Foreign Keys

### Primary Key

```sql
-- Tabela "usuarios"
ALTER TABLE usuarios
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

-- Tabela "destinos"
ALTER TABLE destinos
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

-- Tabela "reservas"
ALTER TABLE reservas
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);
```

#### Exemplos após adicionar Primary Keys

```sql
-- Inserção na tabela "usuarios"
INSERT INTO usuarios (nome, email, data_nascimento, endereco)
VALUES ('João Maria', 'joaomaria@example.com', '1990-01-01', 'Rua A, 123');

-- Inserção na tabela "destinos"
INSERT INTO destinos (nome, descricao)
VALUES ('Praia Teste', 'Destino paradisíaco com belas praias.');

-- Inserção na tabela "reservas"
INSERT INTO reservas (id_usuario, id_destino, data, status)
VALUES (4, 4, '2023-07-01', 'pendente');
```

### Foreign Keys

```sql
-- Adicionando chave estrangeira na tabela "reservas" referenciando a tabela "usuarios"
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id);

-- Adicionando chave estrangeira na tabela "reservas" referenciando a tabela "destinos"
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY (id_destino) REFERENCES destinos(id);

-- Alterando a restrição da chave estrangeira "fk_reservas_usuarios" na tabela "reservas" para ON DELETE CASCADE
ALTER TABLE reservas
DROP FOREIGN KEY fk_reservas_usuarios;

ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
ON DELETE CASCADE;
```

---

# 🧠 Boas Práticas

- Utilizar nomenclatura única e descritiva para tabelas e colunas
- Sempre definir restrições como NOT NULL, UNIQUE e DEFAULT quando apropriado
- Utilizar AUTO_INCREMENT para chaves primárias numéricas
- Documentar colunas com COMMENT para facilitar manutenção
- Antes de excluir uma tabela com DROP TABLE, migrar ou fazer backup dos dados
- Utilizar ON DELETE CASCADE com cautela para evitar exclusões em cascata indesejadas
- Sempre usar WHERE em operações UPDATE e DELETE para evitar modificações em massa acidentais

---

# ⚠️ Pontos de Atenção

- Ocultar a lista de colunas no INSERT pode causar erros se a estrutura da tabela mudar
- O uso de LIKE com % no início da string (%Silva) pode tornar a consulta lenta em tabelas grandes
- DELETE sem WHERE remove TODOS os registros da tabela
- DROP TABLE exclui a tabela e todos os seus dados permanentemente
- Foreign Keys exigem que os valores referenciados existam na tabela pai
- É necessário dropar a Foreign Key antes de dropar uma tabela referenciada
- ALTER TABLE pode bloquear a tabela dependendo do SGBD e da operação

---

# 🧪 Exemplos Práticos

**Exemplo de INSERT com e sem especificação de colunas:**

```sql
-- Com especificação de colunas (recomendado)
INSERT INTO usuarios (nome, email, data_nascimento, endereco) 
VALUES ('Ana Souza', 'ana@email.com', '1995-03-10', 'Rua X, 456');

-- Sem especificação (exige TODAS as colunas na ordem correta)
INSERT INTO usuarios VALUES (5, 'Ana Souza', 'ana@email.com', '1995-03-10', 'Rua X, 456');
```

**Exemplo de SELECT com múltiplas condições:**

```sql
-- Usuários nascidos depois de 1990 com email terminando em .com
SELECT * FROM usuarios 
WHERE data_nascimento > '1990-01-01' AND email LIKE '%.com';
```

**Exemplo de UPDATE com junção de condições:**

```sql
-- Atualizar reservas de um usuário específico para um destino
UPDATE reservas 
SET status = 'confirmada' 
WHERE id_usuario = 1 AND id_destino = 2;
```

---

# 🚀 Conclusão

Este módulo apresentou os comandos essenciais do SQL para manipulação de bancos de dados relacionais. Foram abordados a criação de tabelas com tipos de dados e restrições, as operações CRUD (INSERT, SELECT, UPDATE, DELETE), filtros com WHERE e LIKE, alteração e exclusão de tabelas com ALTER TABLE e DROP TABLE, além da implementação de Primary Keys e Foreign Keys para garantir integridade referencial. Esses conceitos formam a base para trabalhar com qualquer banco de dados relacional no mercado.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: Banco de Dados Relacional](../1-Bancos-Relacionais/README.md) | [⬇ Próximo módulo: SQL Avançado](../3-SQL-Avancado/README.md)