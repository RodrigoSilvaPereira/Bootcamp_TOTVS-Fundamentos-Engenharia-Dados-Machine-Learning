# 📌 Módulo: Microsoft Copilot para SQL

Este módulo aborda a utilização do Microsoft Copilot para auxiliar na construção e padronização de arquitetura de dados, incluindo organização, transformação e enriquecimento de bancos de dados, com um projeto prático envolvendo leitura de imagens e geração de scripts SQL.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Utilizar o Copilot para auxiliar na construção e padronização de arquitetura de dados
- Aplicar o Copilot para organizar, transformar e enriquecer bases de dados
- Realizar leitura de imagens com o Copilot para extrair informações estruturadas
- Gerar scripts SQL automaticamente a partir de imagens
- Criar e popular tabelas em banco de dados relacional (PostgreSQL)

---

# 📚 Conteúdos Abordados

## 🔹 Copilot para SQL

Podemos utilizar o Copilot para auxiliar na construção e padronização em arquitetura de dados. Ele pode organizar, transformar ou enriquecer nossas bases de dados.

**Principais aplicações:**
- Geração automática de scripts SQL
- Padronização de estruturas de tabelas
- Transformação de dados não estruturados em dados estruturados
- Enriquecimento de bases existentes

---

## 🔹 Projeto: Leitor de Cartas com Copilot

Nosso projeto envolve utilizar a leitura de imagens do Copilot para ler as principais informações de uma carta Pokémon, por exemplo (HP, NAME, TYPE), separar essas informações e criar um script para enviar esses dados para um banco de dados relacional (PostgreSQL).

### Estrutura do Projeto

Acesse a pasta `db_scripts`. Lá temos a seguinte estrutura:

```
db_scripts/
│
├── assets/
│ └── card_1.png # Imagem da carta Pokémon
│
├── prompts/
│ └── 001_extrair_infos_carta.txt # Prompt para o Copilot
│
├── seeds/
│ └── 001_seeds_cards.sql # Dados de exemplo (gerados pelo Copilot)
│
└── tables/
└── 001_create_cards_table.sql # Estrutura da tabela (gerada pelo Copilot)
```


### Passo a passo do projeto

1. **Ofereça a imagem** localizada em `assets/card_1.png` para o Copilot

2. **Utilize o prompt** disponível em `prompts/001_extrair_infos_carta.txt` no Copilot

3. **Observe a leitura da imagem:** A IA é capaz de realizar a leitura e extrair informações como:
   - Nome da carta (NAME)
   - Pontos de vida (HP)
   - Tipo (TYPE)
   - Habilidades
   - Outros atributos relevantes

4. **Geração automática:** O Copilot gera os scripts SQL para criar a tabela e inserir os dados

---

## 🔹 Estrutura do Código Gerado

### Tabela (001_create_cards_table.sql)

```sql
CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    hp INTEGER,
    type VARCHAR(50),
    description TEXT
);
```

### Seeds (001_seeds_cards.sql)

```sql
INSERT INTO cards (name, hp, type) VALUES 
('Pikachu', 60, 'Electric'),
('Charizard', 150, 'Fire'),
('Bulbasaur', 45, 'Grass');
```

---

# 🧠 Boas Práticas

- Utilize prompts claros e específicos para obter melhores resultados do Copilot
- Sempre revise os scripts SQL gerados pela IA antes de executar em produção
- Mantenha uma estrutura de pastas organizada (assets, prompts, seeds, tables)
- Documente os prompts utilizados para reprodutibilidade
- Valide as informações extraídas das imagens antes de inserir no banco

---

# ⚠️ Pontos de Atenção

- A precisão da leitura de imagens pode variar dependendo da qualidade da imagem
- Sempre verifique se as informações extraídas estão corretas antes de gerar os inserts
- Imagens com textos muito pequenos ou borrados podem ter leitura imprecisa
- O Copilot pode interpretar cores e símbolos de forma diferente do esperado
- Mantenha as cartas bem posicionadas na imagem para melhor extração

---

# 🧪 Exemplos Práticos

**Exemplo de prompt para extrair informações da carta:**

```
Analise a imagem da carta Pokémon anexada e extraia as seguintes informações:
- Nome da carta
- HP (Hit Points)
- Tipo (ex: Fire, Water, Grass, Electric)
- Habilidades ou ataques

Com base nessas informações, gere:
1. Um comando CREATE TABLE para PostgreSQL
2. Um comando INSERT INTO para cadastrar esta carta
```

**Exemplo de saída esperada do Copilot:**

```sql
-- CREATE TABLE
CREATE TABLE pokemon_cards (
    id SERIAL PRIMARY KEY,
    card_name VARCHAR(100),
    hp INTEGER,
    card_type VARCHAR(50),
    abilities TEXT
);

-- INSERT INTO
INSERT INTO pokemon_cards (card_name, hp, card_type, abilities)
VALUES ('Pikachu', 60, 'Electric', 'Thunder Shock, Quick Attack');
```

---

# 🚀 Conclusão

Este módulo apresentou como utilizar o Microsoft Copilot para auxiliar em tarefas de SQL e arquitetura de dados. Através do projeto "Leitor de Cartas", aprendemos a extrair informações de imagens utilizando IA, gerar scripts SQL automaticamente e estruturar um banco de dados relacional. Essa abordagem demonstra o potencial do Copilot para automatizar tarefas repetitivas e acelerar o desenvolvimento de soluções de dados.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: Microsoft Copilot](../2-Microsoft-Copilot/README.md) | [⬇ Próximo módulo: ETL com Excel e Power Query](../4-ETL-Excel-Power-Query/README.md)