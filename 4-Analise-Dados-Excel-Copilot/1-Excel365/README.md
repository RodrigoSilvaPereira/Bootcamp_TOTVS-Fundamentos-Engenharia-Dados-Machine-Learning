# 📌 Módulo: Introdução ao Excel 365

Este módulo aborda os conceitos fundamentais do Microsoft Excel 365, incluindo estrutura de arquivos, células, intervalos, formatação, fórmulas e atalhos essenciais para produtividade.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Compreender a estrutura de Workbooks, Worksheets, células e intervalos
- Navegar e utilizar menus e menus de contexto
- Aplicar formatação adequada a diferentes tipos de dados
- Criar e utilizar fórmulas no Excel
- Utilizar atalhos para produtividade (F2, Ctrl+Enter, Ctrl+Alt+V, F4)
- Aplicar Cell Freezing para fixar valores em fórmulas
- Criar uma ferramenta de controle de tarefas

---

# 📚 Conteúdos Abordados

## 🔹 Estrutura do Excel

### Workbook

O Workbook é o arquivo do Excel (extensão .xlsx, .xls, .xlsm). Ele pode conter uma ou várias planilhas.

### Worksheet / Sheet

A Worksheet é a planilha dentro do arquivo. Cada workbook pode conter múltiplas sheets, acessíveis pelas abas na parte inferior da tela.

### Cells

Uma célula é o cruzamento entre uma linha (numerada) e uma coluna (letrada). Cada célula tem um endereço único, como A1, B2, C3.

### Ranges

Range é um intervalo de células. Existem duas formas principais de representar ranges:

| Notação | Significado | Exemplo |
|---------|-------------|---------|
| `:` (dois pontos) | Intervalo contínuo | A1:B10 (todas as células de A1 até B10) |
| `;` (ponto e vírgula) | Células específicas | A1;B5;C10 (apenas as células mencionadas) |

## 🔹 Formatação

Podemos escolher vários tipos de dados para as células, incluindo:

- Número (geral, moeda, contábil, percentual, etc.)
- Data e hora
- Texto
- Personalizado

## 🔹 Menus

O Excel 365 possui uma interface de faixa de opções (ribbon) com menus organizados por abas:

- **Página Inicial:** Formatação básica, área de transferência, fontes, alinhamento
- **Inserir:** Tabelas, gráficos, imagens, formas
- **Dados:** Classificação, filtros, conexões de dados
- **Revisão:** Ortografia, comentários, proteger planilhas
- **Exibição:** Layout, zoom, janelas

### Menus de Contexto

Menus de contexto aparecem ao clicar com o botão direito do mouse sobre uma célula, range, ou objeto. Eles oferecem opções rápidas como:

- Copiar/Colar
- Formatar células
- Inserir/Excluir linhas ou colunas
- Filtrar
- Classificar

## 🔹 Fórmulas

Uma fórmula no Excel é uma equação que realiza cálculos ou manipulações de dados em uma célula, começando sempre com o sinal de igual (=).

```excel
=SOMA(A1:A10)
=MÉDIA(B1:B20)
=SE(C1>10, "Aprovado", "Reprovado")
```

### Dicas de Produtividade com Fórmulas

**Aplicar fórmula em coluna inteira:**
1. Selecione todo o intervalo onde deseja aplicar a fórmula
2. Aperte **F2** (entra no modo de edição)
3. Digite ou ajuste a fórmula
4. Aperte **Ctrl + Enter** (aplica a fórmula em todas as células selecionadas)

**Copiar valor da fórmula (não a fórmula em si):**
1. Selecione a célula com a fórmula
2. Aperte **Ctrl + Alt + V** (abre o menu Colar Especial)
3. Selecione "Valores" para colar apenas o resultado, não a fórmula

## 🔹 Cell Freezing (Trava de Células)

O Cell Freezing é usado para "prender" uma célula específica em uma fórmula, impedindo que ela seja alterada ao arrastar a fórmula para outras células.

**Como fazer:**
- Selecione a referência da célula na fórmula (ex: A1)
- Aperte **F4**

**Resultado:**
- `A1` → `$A$1` (fixa coluna e linha)
- Apertar F4 novamente: `A$1` (fixa apenas a linha)
- Apertar F4 novamente: `$A1` (fixa apenas a coluna)
- Apertar F4 novamente: volta ao normal `A1`

**Caracterização:** Os símbolos `$` antes da letra e/ou número indicam quais partes estão fixadas.

```excel
Exemplo de uso:
= B2 * $C$1
Ao arrastar para baixo, C1 permanece fixo enquanto B2 se ajusta.
```

## 🔹 Projeto Prático: Controle de Tarefas

Foi criada uma ferramenta de controle de tarefas no arquivo `tarefas.xlsx`.

**Funcionalidades do arquivo:**
- Listagem de tarefas com status
- Datas de criação e conclusão
- Prioridades (Alta, Média, Baixa)
- Formatação condicional para tarefas atrasadas
- Fórmulas para contagem de tarefas concluídas e pendentes

---

# 🧠 Boas Práticas

- Sempre inicie fórmulas com o sinal de igual (=)
- Utilize nomes descritivos para suas planilhas (ex: "Janeiro", "Vendas_2024")
- Documente fórmulas complexas com comentários na planilha
- Use Cell Freezing ($) quando referenciar valores fixos em fórmulas
- Prefira intervalos nomeados em vez de referências de célula diretas (ex: "Total_Vendas" em vez de "B2:B100")
- Utilize formatação condicional para destacar automaticamente dados importantes
- Salve versões do arquivo antes de fazer alterações estruturais grandes

---

# ⚠️ Pontos de Atenção

- Esquecer o `=` antes de uma fórmula faz o Excel interpretar como texto
- Ao colar valores com `Ctrl + Alt + V`, a fórmula original é perdida (apenas o resultado permanece)
- Cell Freezing sem `$` pode causar erros ao arrastar fórmulas para outras células
- Menus de contexto variam dependendo do que está selecionado (célula, gráfico, imagem, etc.)
- Formatação incorreta (ex: número como texto) pode impedir cálculos
- Workbooks com muitas fórmulas podem ficar lentos - considere usar valores estáticos quando possível

---

# 🧪 Exemplos Práticos

**Exemplo de Soma com Cell Freezing:**

```excel
Preço Unitário em $C$1
Quantidade em A2:A10

Fórmula em B2: =A2*$C$1
Arraste para baixo até B10
```

**Exemplo de SE com condições:**

```excel
=SE(B2>=7, "Aprovado", SE(B2>=5, "Recuperação", "Reprovado"))
```

**Exemplo de CONT.SE para contagem condicional:**

```excel
=CONT.SE(C2:C100, "Concluído")  # Conta quantas tarefas estão concluídas
```

**Exemplo de SOMA.SE para soma condicional:**

```excel
=SOMA.SE(D2:D100, "Alta", E2:E100)  # Soma valores de E onde prioridade é Alta
```

**Exemplo de PROCV (PROCURAR VERTICAL):**

```excel
=PROCV(F2, A2:B100, 2, 0)  # Procura F2 na coluna A e retorna o valor correspondente da coluna B
```

---

# 🚀 Conclusão

Este módulo apresentou os fundamentos essenciais do Microsoft Excel 365, incluindo a estrutura de Workbooks e Worksheets, células e intervalos, formatação de dados, menus e menus de contexto. Aprendemos sobre fórmulas, atalhos de produtividade como F2, Ctrl+Enter, Ctrl+Alt+V e F4 para Cell Freezing. Esses conhecimentos são a base para utilizar o Excel de forma eficiente em análises de dados, controles e dashboards.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: Fundamentos de ETL](../../3-BDR-ETL/3-Fundamentos-ETL/README.md) | [⬇ Próximo módulo: Microsoft Copilot](../2-Microsoft-Copilot/README.md)