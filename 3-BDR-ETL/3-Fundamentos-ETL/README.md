# 📌 Módulo: Fundamentos do ETL com Python

Este módulo aborda os conceitos fundamentais de ETL (Extract, Transform, Load), suas etapas, vantagens, ferramentas e aplicações práticas utilizando Python, Pandas, Scikit-learn e o framework Luigi.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Compreender o conceito de ETL e sua importância para integração de dados
- Diferenciar Data Mart, Data Warehouse, Data Lake e Lakehouse
- Identificar as etapas de Extração, Transformação e Carregamento
- Utilizar a biblioteca Pandas para manipulação de dados tabulares
- Aplicar a biblioteca Scikit-learn para geração de dados e modelos lineares
- Compreender o framework Luigi para pipelines de dados

---

# 📚 Conteúdos Abordados

## 🔹 Introdução ao ETL

Os processos de ETL (Extract, Transform and Load) envolvem ferramentas de software, voltadas para extração de dados de diversos sistemas e, também, a transformação desses dados conforme regras de negócios bem definidas e, por fim, o carregamento dos dados para um Data Mart e/ou Data Warehouse.

O conteúdo será focado em conceitos introdutórios e práticos direcionados para extração, transformação e carregamento de dados, tópicos que são obrigatórios para o processo de ETL. Os conceitos aplicados são baseados na linguagem Python em conjunto com a biblioteca Pandas, onde adicionalmente será aplicado o framework Luigi, possibilitando a visualização dos dados tratados e centralizados em um dashboard.

ETL é um tipo de data integration em três etapas (extração, transformação e carregamento) usado para combinar dados de diversas fontes. Ele é comumente utilizado para construir um data warehouse.

### Data Mart (DM)

Um data mart é um sistema de armazenamento de dados que contém informações específicas da unidade de negócios de uma organização. Ele contém uma parte pequena e selecionada dos dados que a empresa armazena em um sistema de armazenamento maior. As empresas usam um data mart para analisar informações específicas do departamento com mais eficiência. Ele fornece dados resumidos que as principais partes interessadas podem usar para tomar decisões informadas rapidamente.

### Data Warehouse (DW)

O Data Warehouse é um repositório estruturado, otimizado para análise de dados já processados e organizados. Os dados são carregados após passar por processos de ETL (Extração, Transformação e Carga), garantindo consistência e qualidade.

**Vantagens:** Alta performance para consultas complexas, padronização, confiabilidade e suporte a relatórios de negócios.

**Desvantagens:** Custo elevado, pouca flexibilidade para dados não estruturados e maior tempo de preparação antes do uso.

### Data Lake

O Data Lake é um armazenamento de dados em seu formato bruto, podendo incluir dados estruturados, semiestruturados ou não estruturados (como vídeos, imagens e logs). Ele aceita dados antes da transformação, permitindo maior flexibilidade.

**Vantagens:** Custo mais baixo, suporte a grandes volumes e diferentes tipos de dados, ideal para análises exploratórias e uso de Machine Learning.

**Desvantagens:** Risco de se tornar um "data swamp" (pântano de dados) se não houver governança, além de consultas mais lentas e maior complexidade para garantir qualidade.

### Lakehouse

O Lakehouse surge como uma evolução, combinando a estrutura analítica do Data Warehouse com a flexibilidade do Data Lake. Ele permite armazenar dados brutos e processados em um único ambiente, suportando desde relatórios tradicionais até análises avançadas.

### Resumo do Fluxo ETL

**Extract (Extração)** -> Importar dados de diversos tipos e formatos como: Pasta de trabalho, diversos bancos de dados, CSV, TXT, JSON, etc.

**Transform (Transformação)** -> Colunas, linhas, tipos de dados, mesclar, acrescentar, listas, tabelas

**Load (Carregamento)** -> Para o modelo de dados

Nesse processo os dados são extraídos de um sistema-fonte, transformados em um formato que possa ser analisado, e carregados em nuvem ou outro sistema. Extração, carregamento, transformação (ELT) é uma abordagem alternativa, embora relacionada, projetada para jogar o processamento para o banco de dados, de modo a aprimorar a performance.

## 🔹 Etapas do ETL

### Extração

Nesta etapa, os dados brutos são coletados de diferentes fontes, como bancos de dados SQL, sistemas CRM, arquivos JSON ou até sensores IoT. Os dados são transferidos para uma área de preparação, onde ficam prontos para o próximo estágio.

### Transformação

Os dados extraídos passam por um processo de limpeza e formatação para atender aos requisitos do sistema de destino. Isso pode incluir:

- Remoção de duplicatas e inconsistências
- Conversão de formatos (como unidades de medida ou moedas)
- Agregação e sumarização para análises específicas
- Criptografia ou anonimização para atender a regulamentações de privacidade

### Carregamento

Os dados transformados são carregados no repositório de destino. Isso pode ser feito de forma completa (todos os dados) ou incremental (apenas alterações recentes). Normalmente, essa etapa é automatizada e ocorre em horários de menor tráfego.

## 🔹 Vantagens do ETL

- Garantia significativa da qualidade dos dados
- Funcionalidade de execução
- Facilidade no desenvolvimento de cargas
- Facilidade na manutenção das cargas
- Metainformação gerados e mantidos de forma automática pela ferramenta
- Alta Performance
- Deslocamento facilitado de servidores (Transferência)
- Conectividade com várias fontes
- Reinicialização de carga
- Segurança e Estabilidade

## 🔹 Ferramentas de ETL

Existem muitas ferramentas de ETL: IBM Information Server (Data Stage), Oracle Data Integrator (ODI), Informatica Power Center, Microsoft Integration Services (SSIS), Talend Studio (TS). Existe também um conjunto de ferramentas de ETL Open Source como o PDI - Pentaho Data Integrator e Talend ETL.

As ferramentas são softwares utilizados para facilitar o processo de integração de dados. Inicialmente muito usadas em projetos de Data Warehouse e Business Intelligence em geral, ultimamente têm sido utilizadas em processo de integração de software, bancos de dados, etc.

## 🔹 Introdução à Biblioteca Pandas

O Pandas permite trabalhar com diferentes tipos de dados:

- Dados tabulares, como uma planilha do Excel ou uma tabela SQL
- Dados ordenados de modo temporal ou não
- Qualquer outro conjunto de dados, que não necessariamente precisam estar rotulados

Os dois principais objetos da biblioteca Pandas são as Series e os DataFrames:

- Uma **Serie** é uma matriz unidimensional que contém uma sequência de valores que apresentam uma indexação (que podem ser numéricos inteiros ou rótulos), muito parecida com uma única coluna no Excel.
- **Dataframe** é uma estrutura de dados tabular, semelhante a planilha de dados do Excel, em que tanto as linhas quanto as colunas apresentam rótulos.

### Comandos Equivalentes ao Excel

| R / Pandas | Descrição |
|------------|-----------|
| dim(df) / df.shape | Dimensões do dataframe |
| head(df) / df.head() | Primeiras linhas |
| slice(df, 1:10) / df.iloc[:9] | Fatia de linhas |
| filter(df, col1 == 1, col2 == 1) / df.query('col1 == 1 & col2 == 1') | Filtro com múltiplas condições |
| df[df$col1 == 1 & df$col2 == 1,] / df[(df.col1 == 1) & (df.col2 == 1)] | Filtro com condições |

### Principais Comandos do Pandas (df.)

| Comando | Descrição |
|---------|-----------|
| df.head(n) | Retorna as primeiras n linhas (padrão 5) |
| df.tail(n) | Retorna as últimas n linhas (padrão 5) |
| df.info() | Informações sobre tipos de dados e valores não nulos |
| df.describe() | Estatísticas descritivas das colunas numéricas |
| df.shape | Retorna uma tupla (linhas, colunas) |
| df.columns | Retorna os nomes das colunas |
| df.dtypes | Retorna os tipos de cada coluna |
| df.isnull().sum() | Conta valores nulos por coluna |
| df.dropna() | Remove linhas com valores nulos |
| df.fillna(valor) | Preenche valores nulos com um valor específico |
| df.groupby(coluna) | Agrupa dados por uma ou mais colunas |
| df.merge(outro_df, on=coluna) | Mescla dois dataframes |
| df.to_csv('arquivo.csv') | Salva o dataframe em arquivo CSV |

## 🔹 Biblioteca Scikit-learn

Dispõe de ferramentas simples e eficientes para análise preditiva de dados, é reutilizável em diferentes situações, possui código aberto, sendo acessível a todos e foi construída sobre os pacotes NumPy, SciPy e Matplotlib.

### Exemplo Prático com Scikit-learn

Massa de dados com 200 observações, com apenas uma variável preditora, que será a variável x e a variável target, que será a y. Para isso indicamos os parâmetros n_samples = 200 e n_features = 1. O parâmetro noise define o quão dispersos os dados estarão um dos outros.

**Etapa 1: Gerar dados de regressão**

```py
from sklearn.datasets import make_regression

x, y = make_regression(n_samples=200, n_features=1, noise=30)
```

Usando o matplotlib, com o módulo pyplot e a função scatter(), que criará o gráfico, e função show() que exibirá na tela:

```py
import matplotlib.pyplot as plt

# mostrando no gráfico:
plt.scatter(x, y)
plt.show()
```

Com os dados gerados, já podemos iniciar a criação de nosso modelo de machine learning. Para isso utilizaremos o módulo linear_model, e a função LinearRegression().

```py
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(x, y)
```

O objeto de modelo está pronto para receber os dados que dão origem ao modelo.

**Etapa 2: Visualizar a reta de regressão linear**

Vamos visualizar a reta de regressão linear que o modelo gera, com os mesmos dados que criaram o modelo. Para isso iremos utilizar o método predict(), indicando que queremos aplicar a previsão nos valores de x. O resultado do método será uma previsão de y para cada valor x apresentado.

```py
modelo.predict(x)
```

A função plot() do pacote pyplot gera uma reta com os dados apresentados. Como já temos os dados de x e y, basta indicá-los na função. Assim, primeiramente montamos novamente o gráfico de x e y original com a função scatter(), e somamos a ele a reta de regressão:

```py
plt.scatter(x, y)
plt.plot(x, modelo.predict(x), color='red', linewidth=3)
plt.show()
```

## 🔹 Exemplo de Leitura de Arquivo CSV com Python

```py
import pandas as pd

# Leitura de arquivo CSV a partir de uma URL
url = "https://raw.githubusercontent.com/datasets/iris/master/data/iris.csv"
df = pd.read_csv(url)

# Visualizando as primeiras linhas
print(df.head())

# Informações básicas do dataset
print(df.info())

# Estatísticas descritivas
print(df.describe())
```

## 🔹 Framework Luigi para ETL com Python

Luigi é um framework de execução criado pelo Spotify que cria pipelines de dados em Python. É um pacote Python (2.7, 3.6, 3.7 testado) que ajuda a construir pipelines complexos de trabalhos em lote. Ele lida com resolução de dependências, gerenciamento de fluxo de trabalho, visualização, tratamento de falhas, integração de linha de comando e muito mais.

### Componentes do Luigi

**Target:** Em palavras simples, um alvo contém a saída de uma tarefa. Um destino pode ser um local (por exemplo: um arquivo, MySQL etc).

**Task:** Tarefa é algo onde o trabalho real ocorre. Uma tarefa pode ser independente ou dependente. O exemplo de uma tarefa dependente é despejar os dados em um arquivo ou banco de dados. Antes de carregar os dados, os dados devem estar lá por qualquer meio (scraping, API, etc). Cada tarefa é representada como uma classe Python que contém certas funções-membro obrigatórias.

### Métodos de uma Task no Luigi

- **require():** Esta função membro da classe task contém todas as instâncias de tarefas que devem ser executadas antes da tarefa atual.
- **output():** Este método contém o destino onde a saída da tarefa será armazenada. Isso pode conter um ou mais objetos de destino.
- **run():** Este método contém a lógica real para executar uma tarefa.

### Interface Gráfica

O framework Luigi tem suporte para trabalho de forma gráfica, disponível em `localhost:8082`.

---

# 🧠 Boas Práticas

- Sempre documentar as regras de negócio aplicadas na etapa de transformação
- Utilizar área de preparação (staging) antes de carregar os dados no destino final
- Preferir cargas incrementais em vez de cargas completas quando possível
- Implementar logs e monitoramento para acompanhar a execução dos pipelines
- Manter a governança de dados para evitar o "data swamp" em Data Lakes
- Utilizar versionamento de código para pipelines de ETL
- Testar pipelines com amostras de dados antes da execução completa

---

# ⚠️ Pontos de Atenção

- A falta de governança em Data Lakes pode transformá-los em "data swamp" (pântano de dados)
- Data Warehouses têm custo elevado e pouca flexibilidade para dados não estruturados
- A etapa de transformação pode se tornar um gargalo se não for otimizada
- ELT (carga primeiro, transformação depois) é diferente de ETL e tem aplicações específicas
- O framework Luigi exige que as tarefas sejam bem definidas para evitar dependências circulares
- A qualidade dos dados na extração impacta diretamente todo o pipeline

---

# 🧪 Exemplos Práticos

**Exemplo de pipeline simples com Luigi:**

```py
import luigi
import pandas as pd

class ExtrairDados(luigi.Task):
    def output(self):
        return luigi.LocalTarget('dados_extraidos.csv')
    
    def run(self):
        df = pd.read_csv('https://raw.githubusercontent.com/datasets/iris/master/data/iris.csv')
        df.to_csv(self.output().path, index=False)

class TransformarDados(luigi.Task):
    def requires(self):
        return ExtrairDados()
    
    def output(self):
        return luigi.LocalTarget('dados_transformados.csv')
    
    def run(self):
        df = pd.read_csv(self.input().path)
        df['sepal_area'] = df['sepallength'] * df['sepalwidth']
        df.to_csv(self.output().path, index=False)

class CarregarDados(luigi.Task):
    def requires(self):
        return TransformarDados()
    
    def run(self):
        print(f"Dados prontos em: {self.input().path}")

if __name__ == '__main__':
    luigi.build([CarregarDados()], local_scheduler=True)
```

**Exemplo de leitura de CSV de uma URL com Pandas:**

```py
import pandas as pd

# Base de dados pública de vinhos (exemplo)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=';')

print("Shape:", df.shape)
print("\nPrimeiras linhas:")
print(df.head())
print("\nEstatísticas:")
print(df.describe())
```

---

# 🚀 Conclusão

Este módulo apresentou os fundamentos do ETL (Extract, Transform, Load), essenciais para integração e preparação de dados. Foram abordados os conceitos de Data Mart, Data Warehouse, Data Lake e Lakehouse, as três etapas do ETL, suas vantagens e ferramentas disponíveis. Também foram introduzidas as bibliotecas Pandas para manipulação de dados tabulares, Scikit-learn para geração de dados e modelos lineares, e o framework Luigi para construção de pipelines de dados em Python. Esses conhecimentos são base para trabalhar com processos de integração e preparação de dados em projetos de dados e machine learning.

---


> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: Operações MongoDB](../2-BD-NoSQL/README.md) | [⬇ Próximo módulo: Análise de Dados com Excel](../../4-Analise-Dados-Excel-Copilot/README.md)