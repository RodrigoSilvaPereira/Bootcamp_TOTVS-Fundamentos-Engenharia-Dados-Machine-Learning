# 📌 Módulo: SQL Avançado

Este módulo aborda conceitos avançados de SQL para otimização e complexidade em consultas de bancos de dados relacionais.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Aplicar a normalização de dados nas formas normais 1FN, 2FN e 3FN
- Utilizar diferentes tipos de JOINs para combinar dados de múltiplas tabelas
- Implementar subconsultas em diferentes partes de uma query
- Utilizar funções agregadas e agrupamento de resultados
- Aplicar índices para otimizar consultas

---

# 📚 Conteúdos Abordados

## 🔹 Normalização de Dados

É um processo no qual organiza e estrutura um banco de dados relacional de forma a eliminar redundâncias e anomalias, garantindo a consistência e integridade dos dados.

### Formas Normais:

**1FN: Atomicidade de Dados**

A 1FN estabelece que cada valor em uma tabela deve ser atômico, ou seja, indivisível. Nenhum campo deve conter múltiplos valores ou listas. No seu caso, o campo "endereco" contém múltiplos valores, como rua, número, cidade e estado. Para atingir a 1FN, precisamos dividir o campo "endereco" em colunas separadas.

Como corrigir:

'''sql
-- Adicionar colunas de endereço à tabela "Usuarios"
ALTER TABLE Usuarios
ADD rua VARCHAR(100),
ADD numero VARCHAR(10),
ADD cidade VARCHAR(50),
ADD estado VARCHAR(50);

-- Copia os dados da tabela original para a nova tabela
UPDATE usuarios
SET rua = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',', -1),
    numero = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',', -1),
    cidade = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',', -1),
    estado = SUBSTRING_INDEX(endereco, ',', -1);

-- Exclusão da coluna "endereco" da tabela original
ALTER TABLE usuarios
DROP COLUMN endereco;
'''

**2FN: Dependência Total da Chave Primária**

Estabelece que uma tabela deve estar na 1FN. Todos os atributos não chave devem depender totalmente da chave primária.

Dica: se sua tabela tem uma chave primária simples, não existe a possibilidade de termos dependência parcial e por tanto ela já se encontra na 2FN.

**3FN: Sem Dependência Transitiva**

Uma tabela deve estar na 2FN. Nenhuma coluna não-chave deve depender de outra coluna não-chave.

Nosso exemplo: Estado -> Cidade

**Resumo das Formas Normais:**

- A 1FN garante que cada valor seja atômico, único e identificável
- A 2FN garante que os atributos não-chave dependam totalmente da chave primária, evitando dependências parciais
- A 3FN elimina dependências transitivas entre os atributos não chave, garantindo que cada atributo não chave dependa apenas da chave primária

(São 6 ao todo, dá pra completar aqui)

## 🔹 Consultas Avançadas

### Junções: JOINs

São usados no SQL para combinar dados de duas ou mais tabelas relacionadas em uma única consulta.

**Tipos de Joins:**

- INNER JOIN
- LEFT JOIN ou LEFT OUTER JOIN
- RIGHT JOIN ou RIGHT OUTER JOIN
- FULL JOIN ou FULL OUTER JOIN

#### INNER JOIN

Retorna apenas as linhas que têm correspondência em ambas as tabelas envolvidas na junção. A junção é feita com base em uma condição de igualdade especifica na cláusula ON.

'''sql
SELECT *
FROM tabela1
INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
'''

**Exemplo no nosso banco:**

'''sql
SELECT
 u.nome, u.email, r.id_destino, r.status, d.nome as nome_destino
FROM usuarios as u
INNER JOIN reservas as r ON u.id = r.id_usuario
INNER JOIN destino as d ON d.id = r.id_destino;
'''

#### LEFT JOIN

Retorna todas as linhas da tabela à esquerda da junção e as linhas correspondentes da tabela à direita. Se não houver correspondência, os valores da tabela à direita serão NULL.

'''sql
SELECT *
FROM tabela1
LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
'''

#### RIGHT JOIN

Retorna todas as linhas da tabela à direita da junção e as linhas correspondentes da tabela à esquerda. Se não houver correspondência, os valores da tabela à esquerda serão NULL.

'''sql
SELECT *
FROM tabela1
RIGHT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
'''

#### FULL JOIN

Retorna todas as linhas de ambas as tabelas envolvidas na junção, combinando-as com base em uma condição de igualdade. Se não houver correspondência, os valores ausentes serão preenchidos com NULL.

'''sql
SELECT *
FROM tabela1
FULL JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
'''

*OBS: MariaDB não tem comando FULL JOIN*

### Subconsultas

Elas permitem realizar consultas mais complexas no qual podemos usar o resultado de uma consulta como entrada para outra consulta.

As subconsultas podem ser usadas em várias partes de uma consulta:
- SELECT
- FROM
- WHERE
- HAVING
- JOIN

**Exemplos:**

'''sql
SELECT * FROM destinos
WHERE id NOT in (SELECT id_destino FROM reservas);
'''

'''sql
SELECT
  u.nome,
  u.email,
  (SELECT COUNT(*) from reservas WHERE id_usuario = usuarios.id) AS total_reservas
FROM usuarios u;
'''

'''sql
SELECT
  u.nome,
  u.email,
  (SELECT COUNT(*) 
   FROM reservas r
   WHERE r.id_usuario = u.id) AS total_reservas
FROM usuarios u;
'''

### Funções Agregadas e Agrupamento de Resultados

**Funções Agregadas:**

- COUNT: Conta o número de registros
- SUM: Soma os valores de uma coluna numérica
- AVG: Calcula a média de valores de uma coluna numérica
- MIN: Retorna o valor mínimo de uma coluna
- MAX: Retorna o valor máximo de uma coluna

**Exemplos de código:**

'''sql
SELECT COUNT(*) FROM usuarios;

-- Media da idade dos usuarios
SELECT AVG(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS idade
FROM usuarios;

-- Soma da idade dos usuarios
SELECT SUM(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS media_idade
FROM usuarios;

-- Menor Idade
SELECT MIN(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS media_idade
FROM usuarios;

-- Maior Idade
SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS media_idade
FROM usuarios;

-- Calcula quantidade de reservas por destino
SELECT *, COUNT(*) AS total_reservas FROM reservas GROUP BY id_destino;

-- Limit
SELECT *, COUNT(*) AS total_reservas FROM reservas GROUP BY id_destino LIMIT 1 OFFSET 2;
SELECT *, COUNT(*) AS total_reservas FROM reservas GROUP BY id_destino LIMIT 1;

-- Ordenação
SELECT nome
FROM usuarios
ORDER BY nome;

SELECT nome, data_nascimento
FROM usuarios
ORDER BY data_nascimento, nome;

SELECT nome, data_nascimento
FROM usuarios
ORDER BY data_nascimento, nome DESC;
'''

## 🔹 Índices

Em SQL, índices são estruturas de dados usadas para acelerar a busca e filtragem de registros em tabelas, funcionando de forma semelhante ao índice de um livro.

### Inserindo massa de dados

'''sql
INSERT INTO usuarios (nome, email, data_nascimento, rua) VALUES
('João Silva', 'joao.silva@example.com', '1990-01-01', 'Rua A'),
('Maria Santos', 'maria.santos@example.com', '1992-03-15', 'Rua B'),
('Pedro Almeida', 'pedro.almeida@example.com', '1985-07-10', 'Rua C'),
('Ana Oliveira', 'ana.oliveira@example.com', '1998-12-25', 'Rua D'),
('Carlos Pereira', 'carlos.pereira@example.com', '1991-06-05', 'Rua E'),
('Laura Mendes', 'laura.mendes@example.com', '1994-09-12', 'Rua F'),
('Fernando Santos', 'fernando.santos@example.com', '1988-02-20', 'Rua G'),
('Mariana Costa', 'mariana.costa@example.com', '1997-11-30', 'Rua H'),
('Ricardo Rodrigues', 'ricardo.rodrigues@example.com', '1993-04-18', 'Rua I'),
('Camila Alves', 'camila.alves@example.com', '1989-08-08', 'Rua J'),
('Bruno Carvalho', 'bruno.carvalho@example.com', '1995-03-25', 'Rua K'),
('Amanda Silva', 'amanda.silva@example.com', '1996-12-02', 'Rua L'),
('Paulo Mendonça', 'paulo.mendonca@example.com', '1999-07-20', 'Rua M'),
('Larissa Oliveira', 'larissa.oliveira@example.com', '1987-10-15', 'Rua N'),
('Fernanda Sousa', 'fernanda.sousa@example.com', '1992-05-08', 'Rua O'),
('Gustavo Santos', 'gustavo.santos@example.com', '1993-09-18', 'Rua P'),
('Helena Costa', 'helena.costa@example.com', '1998-02-22', 'Rua Q'),
('Diego Almeida', 'diego.almeida@example.com', '1991-11-27', 'Rua R'),
('Juliana Lima', 'juliana.lima@example.com', '1997-04-05', 'Rua S'),
('Rafaela Silva', 'rafaela.silva@example.com', '1996-01-10', 'Rua T'),
('Lucas Pereira', 'lucas.pereira@example.com', '1986-08-30', 'Rua U'),
('Fábio Rodrigues', 'fabio.rodrigues@example.com', '1989-03-12', 'Rua V'),
('Isabela Santos', 'isabela.santos@example.com', '1994-12-07', 'Rua W'),
('André Alves', 'andre.alves@example.com', '1995-09-28', 'Rua X'),
('Clara Carvalho', 'clara.carvalho@example.com', '1990-02-15', 'Rua Y'),
('Roberto Mendes', 'roberto.mendes@example.com', '1992-07-21', 'Rua Z'),
('Mariana Oliveira', 'mariana.oliveira@example.com', '1997-05-03', 'Av. A'),
('Gustavo Costa', 'gustavo.costa@example.com', '1998-11-16', 'Av. B'),
('Lara Sousa', 'lara.sousa@example.com', '1993-06-09', 'Av. C'),
('Pedro Lima', 'pedro.lima@example.com', '1996-09-27', 'Av. D');
'''

### Análise de Consultas com EXPLAIN

'''sql
EXPLAIN SELECT * FROM usuarios WHERE nome = "Maria";

EXPLAIN SELECT * FROM usuarios us
INNER JOIN reservas rs
ON us.id = rs.id_usuario
WHERE nome = "Maria";
'''

### Criando Índice

'''sql
CREATE INDEX idx_nome ON usuarios (nome);

EXPLAIN SELECT * FROM usuarios WHERE nome = "Maria";
'''

---

# 🧠 Boas Práticas

- Aplicar a normalização até a 3FN para evitar redundâncias e anomalias
- Utilizar JOINs adequados ao tipo de relacionamento entre as tabelas
- Preferir INNER JOIN quando apenas registros com correspondência são necessários
- Usar LEFT JOIN quando todos os registros da tabela principal são necessários
- Criar índices em colunas frequentemente usadas em WHERE, JOIN e ORDER BY
- Utilizar EXPLAIN para analisar o desempenho das consultas antes de criar índices
- Em subconsultas, verificar se não podem ser substituídas por JOINs para melhor performance
- Utilizar LIMIT para restringir resultados em consultas de teste

---

# ⚠️ Pontos de Atenção

- Índices aceleram leituras mas desaceleram operações de escrita (INSERT, UPDATE, DELETE)
- O MariaDB não suporta FULL JOIN (é necessário simular com UNION)
- Subconsultas em linhas muito grandes podem ter performance inferior a JOINs
- A normalização excessiva pode levar a muitas tabelas e joins complexos
- O uso de SELECT * com JOINs pode trazer colunas desnecessárias
- Ao usar GROUP BY, todas as colunas do SELECT precisam estar no GROUP BY ou serem agregadas
- O operador LIKE com '%' no início não utiliza índices de forma eficiente

---

# 🧪 Exemplos Práticos

**Exemplo de simulação de FULL JOIN no MariaDB:**

'''sql
SELECT * FROM usuarios u
LEFT JOIN reservas r ON u.id = r.id_usuario
UNION
SELECT * FROM usuarios u
RIGHT JOIN reservas r ON u.id = r.id_usuario;
'''

**Exemplo de subconsulta correlacionada vs JOIN:**

'''sql
-- Subconsulta
SELECT nome FROM usuarios u
WHERE EXISTS (SELECT 1 FROM reservas r WHERE r.id_usuario = u.id);

-- JOIN equivalente (geralmente mais performático)
SELECT DISTINCT u.nome FROM usuarios u
INNER JOIN reservas r ON u.id = r.id_usuario;
'''

**Exemplo de ordenação com múltiplos critérios:**

'''sql
-- Ordenar destinos por nome decrescente e depois por descrição
SELECT nome, descricao FROM destinos
ORDER BY nome DESC, descricao ASC;
'''

---

# 🚀 Conclusão

Este módulo apresentou conceitos avançados de SQL essenciais para trabalhar com bancos de dados relacionais de forma eficiente. Foram abordados a normalização de dados (1FN, 2FN e 3FN) para eliminar redundâncias, os diferentes tipos de JOINs para combinar tabelas, subconsultas para consultas aninhadas, funções agregadas com agrupamento e ordenação, além da criação de índices para otimização de performance com o comando EXPLAIN. Esses conhecimentos permitem construir consultas mais complexas e otimizadas para aplicações reais.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: SQL Básico](../2-SQL-Basico/README.md) | [⬇ Próximo módulo: Introdução ao MongoDB](../../2-BD-NoSQL/1-Introducao-MongoDB/README.md)