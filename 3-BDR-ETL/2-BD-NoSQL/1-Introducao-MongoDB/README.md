# 📌 Módulo: Introdução ao MongoDB

Este módulo aborda os conceitos fundamentais de bancos de dados NoSQL, com foco no MongoDB, sua modelagem flexível e estratégias de armazenamento.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Compreender o conceito de bancos de dados NoSQL e suas diferenças para bancos relacionais
- Identificar os diferentes tipos de bancos NoSQL e seus casos de uso
- Configurar o MongoDB Atlas na nuvem
- Modelar dados utilizando documentos e coleções no MongoDB
- Aplicar estratégias de modelagem como Inner Documents e Referências

---

# 📚 Conteúdos Abordados

## 🔹 O que é um Banco de Dados Não Relacional

Termo Correto: NOT Only SQL

- Não seguem modelos de tabelas e relacionamento
- Projetados para lidar com alto volume de dados, alta escalabilidade
- Alta flexibilidade na estrutura de dados
- São amplamente utilizados em cenários onde a consistência imediata dos dados não é crítica

### Diferenças entre SQL e NoSQL

| SQL | NoSQL |
|-----|-------|
| Modelo de dados fixo | Modelo de dados flexível |
| Escalabilidade vertical (hardware) | Escalabilidade horizontal |
| Transações ACID 100% | Transações ACID ausentes total ou parcial |
| Linguagem de consulta SQL | Cada SGBD tem sua própria |

### Vantagens dos bancos de dados NoSQL

- Flexibilidade na modelagem
- Alta escalabilidade
- Melhor desempenho em cenário de consulta intensiva
- Tolerância a falhas

### Desvantagens dos bancos de dados NoSQL

- Menor consistência de dados imediata
- Menor suporte a consultas complexas (depende do SGBD)

## 🔹 Tipos de NoSQL

### Key-Value (Chave-Valor)

Armazena dados como pares de chave e valor, onde cada chave é um identificador único para acessar o valor correspondente.

**Exemplos de SGBD:** Redis, Riak, Amazon DynamoDB

**Uso:** Um site pode usar um banco de dados Redis para armazenar informações de sessão do usuário.

### Document (Documento)

Armazenam dados em documentos semiestruturados, geralmente em formato JSON ou BSON.

**Exemplos de SGBD:** MongoDB, Couchbase, Apache CouchDB

**Uso:** Um catálogo de e-commerce pode usar o MongoDB para armazenar informações de produtos, como nome, descrição, preço e atributos adicionais.

### Column (Coluna)

Armazenam dados em formato de colunas, o que permite alta escalabilidade e eficiência em determinados tipos de consultas.

**Exemplos de SGBD:** Apache Cassandra, ScyllaDB, HBase

**Uso:** Um sistema de registro de aplicativos pode usar o Apache Cassandra para armazenar registros de log.

### Grafo

Armazenam e consultam dados interconectados onde os relacionamentos entre os dados são tão importantes quanto os próprios dados.

**Exemplos de SGBD:** Neo4j, Amazon Neptune, JanusGraph

**Uso:** Uma rede social pode usar o Neo4j para armazenar os perfis dos usuários e suas conexões, permitindo consultas eficientes para encontrar amigos em comum.

## 🔹 MongoDB

Banco de dados NoSQL orientado a documentos, possui suporte a grandes volumes de dados, escalabilidade horizontal e modelagem flexível, não exige esquema e permite que os documentos sejam armazenados em formato BSON (Binary JSON), proporcionando uma estrutura semiestruturada.

### Vantagens do MongoDB

- Flexibilidade na modelagem de dados
- Escalabilidade horizontal para lidar com grandes volumes de dados
- Consultas ricas e suporte a consultas complexas
- Alta disponibilidade e tolerância a falhas
- Comunidade ativa e recursos de suporte

### Desvantagens do MongoDB

- Menor consistência imediata em comparação com bancos de dados relacionais
- Consultas complexas podem exigir um maior conhecimento e planejamento adequado
- Maior consumo de espaço de armazenamento em comparação com bancos de dados relacionais devido à flexibilidade dos documentos

### Onde é usado?

- Aplicações Web
- Análise de big data
- Armazenamento de dados semiestruturados

### Caso de uso usando geolocalização

Com suas funcionalidades de consulta geoespacial, é adequado para casos de uso que envolvem dados baseados em localização, como aplicativos de mapeamento e rastreamento.

## 🔹 Instalação e Configuração do MongoDB Atlas

Acesse o site: https://cloud.mongodb.com/

Crie a sua conta.

Acesse para criar um cluster.

Escolha a opção free > Provedor AWS > nome: viagens.

Crie sua senha e usuário.

Crie seu cluster.

Você pode se conectar a ele de diversas formas. Vamos utilizar o MongoDB Compass.

*Lembrar de colocar a explicação de como instalar e conectar.*

## 🔹 Modelagem de Dados Usando Documentos

**Database** > Várias **Coleções** > Vários **Documentos**

### Coleções

Agrupamento lógico de documentos, não exige esquema ou que os documentos tenham a mesma estrutura.

**Características:**
- Os nomes das coleções devem seguir regras
- Devem começar com uma letra ou um underscore (_)
- Podem conter letras, números ou underscores
- Não podem ser vazios
- Não podem ter mais que 64 bytes de comprimento

### Documentos

São armazenados em documentos BSON (Binary JSON), são estruturados flexíveis e semiestruturados. Cada documento possui um identificador chamado "_id" e é composto por pares chave e valores.

**Características:**
- Tamanho máximo: 16MB
- Aninhamento de documentos
- Flexibilidade na evolução do esquema

### Tipos de Dados

**Básicos:**
- String
- Number
- Boolean
- Date
- Null
- ObjectId

**Dados complexos:**
- Array
- Documento Embutido
- Referência (Reference)
- GeoJSON

### Estrutura do Documento

```json
{
   _id: ObjectId(""),
   "nome_campo":"valor_campo",
   ... 
}
```

### Site para ajudar a criar um JSON

https://jsonformatter.curiousconcept.com/

## 🔹 Criando a Estrutura do Banco

### Estrutura da coleção "usuarios"

```json
{
   "_id":1,
   "nome":"Rodrigo da Silva Pereira",
   "idade":21,
   "data_nascimento":"2005-05-01",
   "endereco":[
      {
         "logradouro":"Vila Orlando",
         "numero":123,
         "bairro":"Park Imperador",
         "cidade":"Araraquara"
      }
   ],
   "interesses":[
      "kart",
      "culinária",
      "ciclismo"
   ],
   "reservas":[
      1,
      2
   ]
}
```

### Estrutura da coleção "destinos"

```json
{
   "_id":1,
   "nome":"Parque Ibirapuera",
   "descricao":"Principal parque de São Paulo",
   "localizacao":{
      "type":"Point",
      "coordinates":[
         -46.661056,
         -23.587384
      ]
   }
}
```

## 🔹 Estratégias de Modelagem de Dados Eficientes e Escaláveis

- **Modelagem orientada por consultas:** A modelagem de dados no MongoDB deve ser orientada pelas consultas que serão realizadas com mais frequência.

### Inner Documents

No MongoDB, é comum **desnormalizar** os dados para evitar operações de junção (join) custosas. Isso significa que os dados relacionados podem ser armazenados juntos em um único documento, em vez de serem distribuídos em várias coleções.

**Modelando usuários com estratégia desnormalizada:** Perceba que trabalhamos com a reserva de forma interna ao usuário (Nesse exemplo não é a melhor escolha fazer isso, mas é possível).

```json
{
   "_id":1,
   "nome":"Rodrigo da Silva Pereira",
   "idade":21,
   "data_nascimento":"2005-05-01",
   "endereco":[
      {
         "logradouro":"Vila Orlando",
         "numero":123,
         "bairro":"Park Imperador",
         "cidade":"Araraquara"
      }
   ],
   "interesses":[
      "kart",
      "culinária",
      "ciclismo"
   ],
   "reservas":[{
      "data": "2020-10-20",
      "status": "Pendente",
      "destino": "ObjectId("123")"
   }]
}
```

#### Quando usar Inner Documents

- Os dados aninhados são específicos para o documento pai
- Os dados aninhados são sempre acessados juntamente com o documento pai
- A cardinalidade do relacionamento é um-para-um/muitos (um usuário pode ter uma/várias reservas)

#### Quando não usar Inner Documents

- Se os dados aninhados precisarem ser consultados e atualizados independentemente do documento pai, é mais adequado utilizar coleções separadas

## 🔹 Referências

Forma de relacionar os documentos entre si.

### Modelando usuários utilizando Referências

**Reservas:**

```json
{
   "_id": ObjectId("123"),
   "destino": ObjectId("456"),
   "data": "2023-10-10",
   "status": "pendente",
   "usuario": ObjectId("345")
}
```

**Usuário:**

```json
{
   "_id":1,
   "nome":"Rodrigo da Silva Pereira",
   "idade":21,
   "data_nascimento":"2005-05-01",
   "endereco":[
      {
         "logradouro":"Vila Orlando",
         "numero":123,
         "bairro":"Park Imperador",
         "cidade":"Araraquara"
      }
   ],
   "interesses":[
      "kart",
      "culinária",
      "ciclismo"
   ],
   "reservas":[ ObjectId("123"), ObjectId("456") ]
}
```

#### Quando usar Referências

- Os dados têm seu próprio significado e podem ser acessados independente do seu pai
- Os dados têm uma cardinalidade mais alta (por exemplo, vários usuários podem ter reservas)

#### Quando não usar Referências

- Se os dados aninhados precisarem ser consultados e atualizados junto com o documento pai, é mais adequado utilizar a mesma coleção

---

# 🧠 Boas Práticas

- Modelar os dados orientado pelas consultas mais frequentes da aplicação
- Utilizar Inner Documents quando os dados são sempre acessados junto com o documento pai
- Utilizar Referências quando os dados precisam ser acessados independentemente
- Seguir as regras de nomenclatura para coleções (iniciar com letra ou underscore)
- Manter os documentos dentro do limite de 16MB
- Utilizar o ObjectId como identificador único padrão dos documentos

---

# ⚠️ Pontos de Atenção

- NoSQL não significa ausência total de consistência, mas sim consistência eventual em alguns casos
- Cada tipo de NoSQL (Key-Value, Document, Column, Grafo) atende a casos de uso específicos
- O MongoDB não substitui completamente bancos relacionais em todos os cenários
- Inner Documents podem levar à redundância se não forem bem planejados
- Referências exigem múltiplas consultas para acessar dados relacionados
- O tamanho máximo do documento é 16MB (atenção a documentos muito grandes)
- A escolha entre Inner Document e Referência impacta diretamente na performance

---

# 🧪 Exemplos Práticos

**Exemplo de documento com GeoJSON para consulta espacial:**

```json
{
   "_id": 1,
   "nome": "Parque Ibirapuera",
   "localizacao": {
      "type": "Point",
      "coordinates": [-46.661056, -23.587384]
   }
}
```

**Exemplo de documento com array de objetos aninhados:**

```json
{
   "_id": 1,
   "nome": "Rodrigo",
   "telefones": [
      {"tipo": "residencial", "numero": "1234-5678"},
      {"tipo": "celular", "numero": "98765-4321"}
   ]
}
```

**Exemplo de documento com diferentes tipos de dados:**

```json
{
   "_id": ObjectId("507f1f77bcf86cd799439011"),
   "nome": "Rodrigo",
   "ativo": true,
   "data_cadastro": ISODate("2024-01-15T10:30:00Z"),
   "pontuacao": null,
   "tags": ["premium", "verificado"]
}
```

---

# 🚀 Conclusão

Este módulo apresentou os fundamentos dos bancos de dados NoSQL, com ênfase no MongoDB. Foram abordados os diferentes tipos de NoSQL (Key-Value, Document, Column e Grafo), suas vantagens e desvantagens. Aprendemos sobre a instalação e configuração do MongoDB Atlas, a modelagem de dados utilizando coleções e documentos, os tipos de dados disponíveis e as estratégias de modelagem com Inner Documents e Referências. Esses conceitos são essenciais para trabalhar com dados não estruturados e aplicações que exigem alta escalabilidade e flexibilidade.

---

> [🏠 Voltar ao índice](../../README.md) | [⬇ Próximo módulo: Operações MongoDB](../2-Operacoes-MongoDB/README.md)