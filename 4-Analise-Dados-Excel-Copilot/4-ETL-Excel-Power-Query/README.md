# 📌 Módulo: ETL com Excel e Power Query

Este módulo aborda a aplicação prática de processos de ETL (Extract, Transform, Load) utilizando Excel e Power Query, com um case real de tratamento de dados de jogos da Nintendo.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Compreender a aplicação do ETL no contexto de planilhas Excel
- Utilizar o Power Query para limpeza e transformação de dados
- Aplicar técnicas de remoção de inconsistências e dados incorretos
- Separar colunas utilizando delimitadores personalizados
- Padronizar valores textuais (como siglas de regiões)
- Criar colunas calculadas a partir de operações matemáticas
- Limpar campos com caracteres especiais ou indesejados
- Exportar dados transformados para uma nova planilha

---

# 📚 Conteúdos Abordados

## 🔹 Case Situation

Uma base de dados com informações de jogos que a Nintendo envia para os lojistas revenderem. A base de dados oferece diversos problemas como:

- Dados de diferentes colunas juntas (jogo - console)
- Campos com (`---` ou `-----`) para realizar a divisão de lotes
- Linhas em branco
- Inconsistências nos dados

### Exemplo dos dados brutos:

| Package Id | Game | Send Date | Region | Order Status | E-commerce | Stock Quantity | Preço Unit Price | Store Manager | Batch | Age Rating | Publisher |
|------------|------|-----------|--------|--------------|------------|----------------|------------------|---------------|-------|------------|-----------|
| 95774 | The Legend of Zelda: Breath of the Wild - Switch | 15/04/2024 | EN | Pending | GameShop | 167 | 50.07 | Crystal Haynes | Batch-202 | Free | First Party |

## 🔹 ETL com Power Query

### Passo a passo do processo:

1. **Criar uma pasta de trabalho no Excel** e importar os dados do arquivo `raw_data_nintendo.xlsx`

2. **Clicar na opção "Transformar Dados"** - isso abre o Power Query, onde vamos iniciar as transformações

### Etapas de Transformação:

| Etapa | Descrição |
|-------|-----------|
| 1 | Remover a coluna `Package Id` |
| 2 | Remover incidências incorretas na coluna `Game` (como em branco ou tracejados `---`, `----`, `-----`) |
| 3 | Separar o console do nome do game com a opção "Dividir colunas" > Por delimitador > Personalizado > Extrema direita. Renomear as colunas para `Game_Name` e `Game_Console` |
| 4 | Alterar as siglas das regiões: selecionar a coluna `Region` > Transformar > Substituir Valores. Converter `EN` para `English`, `JP` para `Japanese`, `PT` para `Portuguese` |
| 5 | Criar a coluna `total_price` fazendo a multiplicação de `Stock Quantity` e `Unit Price` |
| 6 | Substituir `Batch-` por vazio, para ficar apenas o número do lote |

### Código Avançado do Power Query (M Language)

```m
let
    Fonte = Excel.Workbook(File.Contents("C:\Users\Rodrigo\Desktop\Bootcamp_TOTVS-Fundamentos-Engenharia-Dados-Machine-Learning\4-Analise-Dados-Excel-Copilot\4-ETL-Excel-Power-Query\raw_data_nintendo.xlsx"), null, true),
    Planilha1_Sheet = Fonte{[Item="Planilha1",Kind="Sheet"]}[Data],
    #"Cabeçalhos Promovidos" = Table.PromoteHeaders(Planilha1_Sheet, [PromoteAllScalars=true]),
    #"Tipo Alterado" = Table.TransformColumnTypes(#"Cabeçalhos Promovidos",{{"Package Id", type any}, {"Game", type text}, {"Send Date", type any}, {"Region", type text}, {"Order Status", type text}, {"E-commerce", type text}, {"Stock Quantity", type any}, {"Preço Unit Price", type text}, {"Store Manager", type text}, {"Batch", type text}, {"Age Rating", type text}, {"Publisher", type text}}),
    #"Colunas Removidas" = Table.RemoveColumns(#"Tipo Alterado",{"Package Id"}),
    #"Linhas Filtradas" = Table.SelectRows(#"Colunas Removidas", each ([Game] <> null and [Game] <> "---" and [Game] <> "----" and [Game] <> "-----")),
    #"Dividir Coluna por Delimitador" = Table.SplitColumn(#"Linhas Filtradas", "Game", Splitter.SplitTextByEachDelimiter({"-"}, QuoteStyle.Csv, true), {"Game.1", "Game.2"}),
    #"Tipo Alterado1" = Table.TransformColumnTypes(#"Dividir Coluna por Delimitador",{{"Game.1", type text}, {"Game.2", type text}}),
    #"Linhas Filtradas1" = Table.SelectRows(#"Tipo Alterado1", each [Game.2] <> null and [Game.2] <> ""),
    #"Linhas Filtradas2" = Table.SelectRows(#"Linhas Filtradas1", each [Game.1] <> null and [Game.1] <> ""),
    #"Colunas Renomeadas" = Table.RenameColumns(#"Linhas Filtradas2",{{"Game.1", "Game_Name"}, {"Game.2", "Game_Console"}}),
    #"Valor Substituído" = Table.ReplaceValue(#"Colunas Renomeadas","EN","English",Replacer.ReplaceText,{"Region"}),
    #"Valor Substituído1" = Table.ReplaceValue(#"Valor Substituído","JP","Japanese",Replacer.ReplaceText,{"Region"}),
    #"Valor Substituído2" = Table.ReplaceValue(#"Valor Substituído1","PT","Portuguese",Replacer.ReplaceText,{"Region"}),
    #"Linhas Filtradas3" = Table.SelectRows(#"Valor Substituído2", each true),
    #"Valor Substituído3" = Table.ReplaceValue(#"Linhas Filtradas3",".",",",Replacer.ReplaceText,{"Preço Unit Price"}),
    #"Tipo Alterado2" = Table.TransformColumnTypes(#"Valor Substituído3",{{"Stock Quantity", Int64.Type}}),
    #"Valor Substituído4" = Table.ReplaceValue(#"Tipo Alterado2","$","",Replacer.ReplaceText,{"Preço Unit Price"}),
    #"Tipo Alterado3" = Table.TransformColumnTypes(#"Valor Substituído4",{{"Preço Unit Price", type number}}),
    #"Personalização Adicionada" = Table.AddColumn(#"Tipo Alterado3", "total_price", each [Stock Quantity]*[Preço Unit Price]),
    #"Tipo Alterado4" = Table.TransformColumnTypes(#"Personalização Adicionada",{{"total_price", Currency.Type}, {"Preço Unit Price", Currency.Type}}),
    #"Colunas Renomeadas1" = Table.RenameColumns(#"Tipo Alterado4",{{"Preço Unit Price", "Unit Price"}}),
    #"Valor Substituído5" = Table.ReplaceValue(#"Colunas Renomeadas1","Batch-","",Replacer.ReplaceText,{"Batch"})
in
    #"Valor Substituído5"
```

### Exportação

Clique para exportar os dados transformados para uma nova planilha. O resultado final será salvo em `transform_data_nintendo.xlsx`.

---

# 🧠 Boas Práticas

- Sempre mantenha uma cópia dos dados brutos (raw data) antes de iniciar as transformações
- Documente cada etapa da transformação no Power Query
- Utilize nomes descritivos para as etapas no Power Query
- Valide os dados após cada transformação importante
- Exporte os dados transformados para um novo arquivo, em vez de sobrescrever o original

---

# ⚠️ Pontos de Atenção

- O Power Query não altera o arquivo original diretamente - você precisa exportar as alterações
- Ao substituir valores, cuidado com letras maiúsculas/minúsculas (a diferenciação pode afetar o resultado)
- A divisão por delimitador pode criar colunas extras indesejadas se houver múltiplos delimitadores
- Remover linhas em branco pode eliminar dados importantes se o filtro não for bem definido
- Conversões de tipo (ex: texto para número) podem falhar se houver caracteres não numéricos

---

# 🧪 Exemplos Práticos

**Exemplo de dados antes da transformação:**

| Game | Region | Batch |
|------|--------|-------|
| Mario Odyssey - Switch | EN | Batch-101 |
| --- | JP | Batch-102 |
| (linha vazia) | PT | Batch-103 |

**Exemplo de dados depois da transformação:**

| Game_Name | Game_Console | Region | Batch |
|-----------|--------------|--------|-------|
| Mario Odyssey | Switch | English | 101 |

---

# 🚀 Conclusão

Este módulo apresentou a aplicação prática de ETL utilizando Excel e Power Query. Através de um case real com dados de jogos da Nintendo, aprendemos a importar dados, limpar inconsistências, separar colunas por delimitador, padronizar valores textuais, criar colunas calculadas e exportar os dados transformados. O Power Query se mostrou uma ferramenta poderosa para processos de transformação de dados sem necessidade de programação complexa.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: Copilot com SQL](../3-Copilot-SQL/README.md) | [⬇ Próximo módulo: Análise de Dados com Copilot](../5-Analise-Dados-Copilot/README.md)