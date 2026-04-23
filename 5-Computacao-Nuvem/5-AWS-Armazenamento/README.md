# 📌 Módulo: Armazenamento e Banco de Dados na AWS

Este módulo aborda os principais serviços de armazenamento e banco de dados da AWS, incluindo EBS, S3, EFS, RDS, DynamoDB e Redshift.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Compreender os diferentes tipos de armazenamento em nuvem (objetos, arquivos, blocos)
- Utilizar o Amazon EBS para armazenamento persistente de instâncias EC2
- Armazenar e recuperar dados com o Amazon S3
- Configurar sistemas de arquivos compartilhados com o Amazon EFS
- Gerenciar bancos de dados relacionais com o Amazon RDS
- Utilizar o DynamoDB para bancos de dados NoSQL serverless
- Compreender o Amazon Redshift para Big Data e data warehouse

---

# 📚 Conteúdos Abordados

## 🔹 Armazenamento de Dados em Nuvem

### Tipos de Armazenamento

| Tipo | Descrição | Casos de Uso |
|------|-----------|--------------|
| **Armazenamento de Objetos** | Dados como objetos (arquivos e metadados), não estruturados | Data lakes, mídias, backup e recuperação |
| **Armazenamento de Arquivos** | Sistemas de arquivos compartilhados, acesso via servidores e usuários | Ferramentas de desenvolvimento, diretórios pessoais |
| **Armazenamento de Blocos** | Discos HDD/SSD com diferentes configurações de leitura/escrita | Máquinas virtuais, contêineres, banco de dados |

## 🔹 Amazon Elastic Block Store (EBS)

### Volume Instance Store

Armazenamento de blocos, discos anexados fisicamente ao computador host. Ideal para dados de armazenamento temporário como buffers, cache ou dados de rascunho.

**Atenção:** Os dados serão perdidos se houver:
- Falha de disco
- Instância parada
- Instância hibernada
- Instância encerrada

### Amazon EBS

Para corrigir esse caso de uso, surgiu o EBS. É um armazenamento de um HD físico projetado para o EC2. Os HDs são chamados de **volumes**. Agora você tem o armazenamento vinculado à sua EC2, podendo ser configurado no momento da criação da instância.

## 🔹 Amazon S3 - Simple Storage Service

O Amazon S3 armazena objetos com a estrutura: Dados, Metadados e Chave.

| Componente | Descrição |
|------------|-----------|
| **Chave** | Nome que você atribui ao objeto, usado para recuperá-lo |
| **Valor (Dados)** | Conteúdo que você está armazenando |
| **Metadados** | Conjunto de pares nome-valor para armazenar informações relacionadas ao objeto |

### Buckets

Os objetos são armazenados em **Buckets**. Buckets são contêineres para objetos. Você pode armazenar qualquer número de objetos em um bucket. Objetos podem ter de 0 até 5TB de tamanho. Você pode usar até 100 buckets na sua conta.

**Características:**
- Controle de acesso por objeto
- Versionamento de objetos

**Casos de uso:** Data lakes, arquivamento de dados, hospedagem de sites estáticos.

### Classes de Armazenamento S3

| Classe | Uso | Características |
|--------|-----|-----------------|
| **S3 Standard** | Dados acessados com frequência | Alta durabilidade (99,999999999%) e disponibilidade (99,99%) |
| **S3 Intelligent-Tiering** | Padrões de acesso desconhecidos ou variáveis | Move dados automaticamente entre camadas para otimizar custos |
| **S3 Standard-IA** | Dados acessados com menos frequência | Menor custo de armazenamento, com taxa de recuperação |
| **S3 One Zone-IA** | Dados que podem ser armazenados em uma única AZ | Custo 20% menor que Standard-IA |
| **S3 Glacier** | Arquivos acessados raramente (arquivamento) | Baixo custo, recuperação de minutos a horas |
| **S3 Glacier Deep Archive** | Arquivamento de longo prazo | Menor custo de armazenamento, recuperação em horas |

## 🔹 Amazon EFS - Elastic File System

Fornece um sistema de arquivos serverless e totalmente elástico. Escala até Petabytes, aumentando e diminuindo conforme adição e remoção de arquivos.

**Características:**
- Compatível com protocolo NFS (Network File System)
- Pode ser acessado por EC2, Lambda e ECS
- Acesso simultâneo aos mesmos dados sem problemas de performance

### Classes de Armazenamento EFS

| Classe | Descrição |
|--------|-----------|
| **Padrão (instância regional)** | Standard e Standard-IA |
| **Uma AZ** | One Zone e One Zone-IA |

## 🔹 Amazon RDS - Relational Database Service

O Amazon RDS é um serviço gerenciado da AWS que facilita a configuração, operação e escalabilidade de bancos de dados relacionais na nuvem. Ele automatiza tarefas administrativas, como provisionamento, backups, aplicação de patches e recuperação.

### Mecanismos de Banco de Dados Suportados

- MySQL
- PostgreSQL
- MariaDB
- Oracle
- Microsoft SQL Server
- IBM Db2

### Benefícios do Amazon RDS

| Benefício | Descrição |
|-----------|-----------|
| **Gerenciamento simplificado** | Automatiza backups, atualizações e detecção de falhas |
| **Alta disponibilidade** | Suporte a implantações multi-AZ com failover automático |
| **Escalabilidade** | Ajuste de recursos de computação e armazenamento |
| **Segurança** | Controle de acesso granular e isolamento em VPC |
| **Custo-benefício** | Elimina necessidade de gerenciar infraestrutura física |

### Casos de Uso

- Aplicações web, móveis e corporativas
- Migração de bancos de dados legados para a nuvem

## 🔹 Amazon DynamoDB

O Amazon DynamoDB é um banco de dados NoSQL, sem servidor e totalmente gerenciado, projetado para oferecer desempenho de milissegundos de um dígito em qualquer escala.

### Características Principais

| Característica | Descrição |
|----------------|-----------|
| **Serverless** | Elimina necessidade de provisionar ou manter servidores |
| **Escala automática** | Ajusta capacidade conforme demanda |
| **Modelos flexíveis** | Suporta chave-valor e documentos |
| **Totalmente gerenciado** | Provisionamento, backups, segurança e monitoramento |

### Casos de Uso

| Setor | Aplicação |
|-------|-----------|
| **Serviços financeiros** | Transações, roteamento em tempo real, geração de tokens |
| **Jogos** | Dados de jogadores, histórico de sessões, rankings |
| **Streaming** | Indexação de metadados, listas de reprodução |
| **E-commerce** | Carrinhos de compras, rastreamento de inventário, perfis de clientes |

### Recursos Avançados

- **Tabelas globais:** Replicação multi-ativa entre regiões (99,999% disponibilidade)
- **Transações ACID:** Alterações consistentes e atômicas em múltiplos itens
- **DynamoDB Streams:** Captura de alterações em tempo quase real
- **Índices secundários:** Consultas flexíveis com atributos alternativos

## 🔹 Amazon Redshift - Big Data

Amazon Redshift é um data warehouse totalmente gerenciado e baseado em nuvem, projetado para análises em escala petabyte.

### Principais Capacidades-Chave

| Capacidade | Descrição |
|------------|-----------|
| **Escalabilidade** | De centenas de GBs a múltiplos PBs (sob demanda ou serverless) |
| **Desempenho** | Custo-benefício até 3x melhor que muitos data warehouses |
| **Integrações Zero-ETL** | Conexão direta a bancos operacionais e serviços de streaming |
| **Segurança** | Isolamento de rede, criptografia, controle de acesso detalhado |
| **Integração com IA** | Amazon Q para SQL em linguagem natural, integração com Bedrock |

### Tecnologias Utilizadas

- Armazenamento em colunas
- Processamento massivamente paralelo (MPP)
- Consulta baseada em SQL

### Integração com Outros Serviços

O Redshift integra-se perfeitamente com serviços AWS como S3, RDS, DynamoDB, Kinesis e SageMaker.

---

# 🧠 Boas Práticas

- Utilize EBS para dados persistentes de instâncias EC2
- Prefira S3 para armazenamento de objetos não estruturados e data lakes
- Utilize S3 Glacier para arquivamento de longo prazo com baixo custo
- Utilize EFS para sistemas de arquivos compartilhados entre múltiplas instâncias
- Utilize RDS para bancos de dados relacionais com requisitos de consistência ACID
- Utilize DynamoDB para workloads NoSQL de alta escala e baixa latência
- Utilize Redshift para análises complexas em grandes volumes de dados
- Escolha a classe de armazenamento S3 adequada com base na frequência de acesso

---

# ⚠️ Pontos de Atenção

- Instance Store é volátil - dados são perdidos ao parar ou encerrar a instância
- EBS volumes não são compartilháveis entre múltiplas instâncias (exceto EBS Multi-Attach)
- S3 não é um sistema de arquivos tradicional - não suporta locks ou edições parciais
- EFS tem custo mais elevado que EBS para certos workloads
- RDS não suporta todos os mecanismos de banco em todas as regiões
- DynamoDB tem limite de 400KB por item
- Redshift não é ideal para workloads OLTP (transacionais)

---

# 🧪 Exemplos Práticos

**Exemplo de arquitetura de armazenamento:**

'''
Aplicação Web
     ↓
Load Balancer (ALB)
     ↓
EC2 (com EBS para dados persistentes)
     ↓
EFS (compartilhado entre múltiplas EC2)
     ↓
S3 (arquivos estáticos e backups)
'''

**Exemplo de arquitetura de banco de dados:**

'''
Aplicação
     ↓
DynamoDB (dados de sessão e carrinho)
     ↓
RDS (dados transacionais ACID)
     ↓
Redshift (análises e relatórios)
'''

**Comando AWS CLI para criar bucket S3:**

'''bash
aws s3 mb s3://meu-bucket-exemplo --region sa-east-1
'''

**Comando AWS CLI para copiar arquivo para S3:**

'''bash
aws s3 cp ./arquivo.txt s3://meu-bucket-exemplo/
'''

---

# 🚀 Conclusão

Este módulo apresentou os principais serviços de armazenamento e banco de dados da AWS, incluindo EBS para armazenamento persistente de blocos, S3 para armazenamento de objetos com diferentes classes de acesso, EFS para sistemas de arquivos compartilhados, RDS para bancos de dados relacionais gerenciados, DynamoDB para NoSQL serverless de alta escala e Redshift para data warehouse e Big Data. Esses conhecimentos são fundamentais para projetar soluções de dados completas e escaláveis na AWS.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: AWS Redes](../4-AWS-Redes/README.md) | [⬇ Próximo módulo: Projeto Nuvem AWS](../../7-Projetos-Práticos/3-Infraestrutura-Cloud-AWS/README.md)