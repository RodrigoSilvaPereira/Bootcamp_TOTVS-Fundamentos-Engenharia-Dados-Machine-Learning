# 📌 Desafio: Dashboard com Excel + Power Query

Este desafio consiste na criação de um dashboard completo utilizando Excel e Power Query, abordando desde a organização dos assets até a construção visual final para responder perguntas de negócio específicas.

---

# 🎯 Objetivos do Desafio

Ao final deste desafio, você será capaz de:

- Organizar assets visuais (paletas de cores, imagens, proporções) para padronização do dashboard
- Compreender e estruturar uma base de dados de assinaturas
- Utilizar Power Query para tratar e preparar os dados
- Responder perguntas de negócio por meio de cálculos e análises
- Criar gráficos e tabelas dinâmicas para visualização dos dados
- Construir um dashboard interativo e profissional

---

# 📚 Conteúdos Abordados

## 🔹 Assets

Nesta parte temos todas as paletas de cores, imagens e proporções que utilizaremos em todo o decorrer do dashboard para melhorar o visual.

**Elementos de Assets:**
- Paleta de cores da marca (cores principais, secundárias e de destaque)
- Logotipos e ícones
- Fontes e tipografia padronizada
- Proporções e tamanhos de elementos
- Layout de referência para o dashboard

---

## 🔹 Base de Dados

Contém toda a nossa base de dados que vamos utilizar no decorrer do dashboard.

### Amostra dos dados:

| Subscriber ID | Name | Plan | Start Date | Auto Renewal | Subscription Price | Subscription Type | EA Play Season Pass | EA Play Season Pass Price | Minecraft Season Pass | Minecraft Season Pass Price | Coupon Value | Total Value |
|---------------|------|------|------------|--------------|--------------------|-------------------|---------------------|---------------------------|----------------------|-----------------------------|--------------|-------------|
| 3231 | João Silva | Ultimate | 01/01/2024 | Yes | R$ 15,00 | Monthly | Yes | R$ 30,00 | Yes | R$ 20,00 | R$ 5,00 | R$ 60,00 |
| 3234 | Ana Souza | Ultimate | 20/02/2024 | No | R$ 15,00 | Monthly | Yes | R$ 30,00 | Yes | R$ 20,00 | R$ 3,00 | R$ 62,00 |
| 3237 | Camila Ribeiro | Ultimate | 03/03/2024 | Yes | R$ 15,00 | Quarterly | Yes | R$ 30,00 | Yes | R$ 20,00 | R$ 10,00 | R$ 55,00 |

### Explicação dos Campos

| Campo | Descrição |
|-------|-----------|
| **Subscriber ID** | Identificador único do assinante |
| **Name** | Nome do assinante |
| **Plan** | Tipo de plano contratado (Ultimate, etc.) |
| **Start Date** | Data de início da assinatura |
| **Auto Renewal** | Indica se a renovação é automática (Yes/No) |
| **Subscription Price** | Valor da assinatura base |
| **Subscription Type** | Tipo de assinatura (Monthly, Quarterly, Annual) |
| **EA Play Season Pass** | Indica se o assinante contratou o EA Play Season Pass (Yes/No) |
| **EA Play Season Pass Price** | Valor do EA Play Season Pass |
| **Minecraft Season Pass** | Indica se o assinante contratou o Minecraft Season Pass (Yes/No) |
| **Minecraft Season Pass Price** | Valor do Minecraft Season Pass |
| **Coupon Value** | Valor do cupom de desconto aplicado |
| **Total Value** | Valor total pago pelo assinante |

---

## 🔹 Cálculos e Perguntas de Negócio

Precisamos pegar a base de dados e separar as informações necessárias para responder as dúvidas de negócio.

### Conceitos Importantes

**Data View:** Visualização dos dados em formato de tabela, permitindo análise detalhada de cada registro.

**Perguntas de Negócio:** Questões estratégicas que orientam a análise dos dados, conectando métricas a decisões empresariais.

### Perguntas de Negócio

#### Pergunta 1
**Qual o faturamento total de vendas de planos anuais (contendo todas as assinaturas agregadas)?**

Para responder: Filtrar registros onde `Subscription Type = "Annual"` e somar `Total Value`

#### Pergunta 2
**Qual o faturamento total de vendas de planos anuais, separado por auto-renovação ou que não é por auto-renovação?**

Para responder: Filtrar `Subscription Type = "Annual"`, agrupar por `Auto Renewal` (Yes/No) e somar `Total Value`

#### Pergunta 3
**Total de vendas de assinatura do EA Play**

Para responder: Filtrar registros onde `EA Play Season Pass = "Yes"` e somar `EA Play Season Pass Price`

#### Pergunta 4
**Total de Assinaturas do Minecraft Season Pass**

Para responder: Filtrar registros onde `Minecraft Season Pass = "Yes"` e contar o número de assinaturas (ou somar o valor, dependendo da métrica desejada)

### Visualização dos Dados

Criar um gráfico da tabela dinâmica e um filtro para entender o comportamento dos dados.

**Sugestões de gráficos:**
- Gráfico de barras para faturamento por tipo de assinatura
- Gráfico de pizza para proporção de auto-renovação vs não auto-renovação
- Cartões (cards) para valores totais de cada KPI
- Segmentação de dados (slicer) para filtrar por período ou plano

---

## 🔹 Dashboard

Agora que entendemos os gráficos que vamos usar e os dados relevantes, vamos fazer o dashboard e levar tudo para lá.

### Etapas para construção do Dashboard:

1. **Preparação dos dados no Power Query**
   - Importar a base de dados
   - Limpar e transformar dados conforme necessário
   - Criar colunas calculadas se necessário

2. **Criação das Tabelas Dinâmicas**
   - Criar tabelas dinâmicas para cada pergunta de negócio
   - Organizar linhas, colunas e valores

3. **Criação dos Gráficos**
   - Inserir gráficos baseados nas tabelas dinâmicas
   - Escolher o tipo de gráfico adequado para cada análise

4. **Montagem do Dashboard**
   - Organizar os elementos em uma planilha dedicada
   - Aplicar os assets (cores, fontes, proporções)
   - Inserir slicers para filtros interativos
   - Adicionar título e contexto ao dashboard

5. **Formatação e Ajustes Finais**
   - Padronizar cores e fontes
   - Ajustar tamanhos e posições
   - Testar interatividade dos filtros

---

# 🧠 Boas Práticas

- Utilize uma paleta de cores consistente em todo o dashboard
- Mantenha os gráficos simples e de fácil interpretação
- Coloque os filtros mais importantes em posição de destaque
- Cada gráfico deve responder a uma pergunta específica
- Inclua um título descritivo no dashboard
- Utilize cards (cartões) para valores totais importantes
- Teste o dashboard com usuários reais antes de publicar

---

# ⚠️ Pontos de Atenção

- Dados desatualizados comprometem a confiabilidade do dashboard
- Gráficos muito complexos podem confundir em vez de ajudar
- Cores em excesso poluem o visual - use com moderação
- Slicers devem estar conectados a todas as tabelas dinâmicas relevantes
- Verifique se os cálculos estão corretos antes de publicar o dashboard
- O dashboard deve ser responsivo a diferentes tamanhos de tela

---

# 🧪 Exemplos Práticos

**Exemplo de cálculo para Pergunta 1 (Faturamento total de planos anuais):**

'''
=SOMA(SE(Subscription Type="Annual"; Total Value; 0))
'''

**Exemplo de estrutura do dashboard sugerida:**

'''
-----------------------------------------------------
|  TÍTULO DO DASHBOARD - ASSINATURAS               |
-----------------------------------------------------
|                    |                             |
|   FILTROS          |   CARDS (KPIs principais)   |
|   (Slicers)        |   R$ Total   |   Total Itens |
|                    |              |               |
-----------------------------------------------------
|                                                    |
|   GRÁFICO 1                    |   GRÁFICO 2     |
|   Faturamento por Tipo         |   Auto-Renovação|
|                                                    |
-----------------------------------------------------
|                                                    |
|   TABELA DETALHADA                                 |
|   (Registros filtrados)                            |
|                                                    |
-----------------------------------------------------
'''

---

# 🚀 Conclusão

Este desafio consolidou os conhecimentos de Excel e Power Query aplicados à criação de dashboards profissionais. Aprendemos a organizar assets visuais, estruturar uma base de dados, responder perguntas de negócio por meio de cálculos, criar gráficos e tabelas dinâmicas, e montar um dashboard interativo. O resultado final é uma ferramenta poderosa para monitoramento e tomada de decisão baseada em dados.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: Dashboards](../6-Dashboards/README.md) | [⬇ Próximo módulo: Computação em Nuvem](../../5-Computacao-Nuvem/README.md)