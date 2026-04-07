# 📌 Módulo: Strings e Fatiamento em Python

Este módulo aborda manipulação de strings em Python, incluindo métodos essenciais, interpolação de valores e técnicas de fatiamento.

Strings são fundamentais em cenários de dados, sendo amplamente utilizadas em:

- Limpeza de dados (data cleaning)
- Padronização de informações
- Processamento de arquivos (CSV, JSON)
- Extração de informações (parsing)

---

# 🎯 Objetivo do Módulo

Capacitar o profissional para:

- Manipular e transformar strings
- Utilizar métodos built-in da linguagem
- Formatar saídas de dados
- Extrair partes específicas de textos
- Trabalhar com dados textuais de forma eficiente

---

# 🧠 Conceitos Fundamentais

Strings em Python são:

- Sequências imutáveis de caracteres
- Indexadas (podem ser acessadas por posição)
- Iteráveis (podem ser percorridas com loops)

---

# ⚙️ Funcionamento das Strings

Cada caractere possui um índice:

```python
texto = "Python"

P  y  t  h  o  n
0  1  2  3  4  5
```

---

# 🛠️ Métodos úteis da classe String

---

## 🔹 Transformação de texto

### 📌 Exemplo aplicado (padronização de dados)

```python
nome_cliente = "rOdRiGo sIlVa"

print(nome_cliente.upper())   # RODRIGO SILVA
print(nome_cliente.lower())   # rodrigo silva
print(nome_cliente.title())   # Rodrigo Silva
```

📌 Muito utilizado para normalizar dados inconsistentes.

---

## 🔹 Remoção de espaços

### 📌 Exemplo aplicado (dados sujos)

```python
email = "   usuario@email.com   "

print(email.strip())   # remove ambos os lados
print(email.lstrip())  # remove esquerda
print(email.rstrip())  # remove direita
```

📌 Fundamental em pipelines de ETL.

---

## 🔹 Junção e formatação

```python
texto = "Python"

print(texto.center(10, "#"))  # ##Python##
print("-".join(texto))        # P-y-t-h-o-n
```

📌 `join()` é muito usado para reconstruir strings.

---

# 🧾 Interpolação de Variáveis

Permite inserir valores dentro de strings.

---

## 🔹 Método % (Legado)

```python
nome = "Rodrigo"
idade = 28

print("Nome: %s | Idade: %d" % (nome, idade))
```

📌 Não recomendado em código moderno.

---

## 🔹 Método format()

```python
nome = "Rodrigo"
idade = 28

print("Nome: {} | Idade: {}".format(nome, idade))
```

### 📌 Variações

```python
print("Nome: {1} | Idade: {0}".format(idade, nome))
```

```python
pessoa = {"nome": "Rodrigo", "idade": 28}

print("Nome: {nome} | Idade: {idade}".format(**pessoa))
```

---

## 🔹 f-strings (Recomendado)

```python
nome = "Rodrigo"
idade = 28

print(f"Nome: {nome} | Idade: {idade}")
```

### 📌 Formatação numérica

```python
PI = 3.14159

print(f"{PI:.2f}")      # 3.14
print(f"{PI:10.2f}")    # alinhamento
```

📌 Mais legível, performático e moderno.

---

# ✂️ Fatiamento de Strings (Slicing)

Permite extrair partes específicas de uma string.

---

## 🔹 Estrutura

```python
string[inicio:fim:passo]
```

- `inicio` → índice inicial (inclusivo)
- `fim` → índice final (exclusivo)
- `passo` → intervalo

---

## 🔹 Exemplos aplicados

```python
nome = "Guilherme Arthur"
```

```python
print(nome[:9])      # Guilherme
print(nome[10:])     # Arthur
print(nome[10:16])   # Arthur
print(nome[::2])     # pega de 2 em 2
```

---

## 🔹 Inversão de string

```python
print(nome[::-1])
```

📌 Muito útil em algoritmos e validações.

---

# 🧾 Strings de Múltiplas Linhas

Utilizadas para textos longos.

```python
nome = "Rodrigo"

mensagem = f"""
Olá, meu nome é {nome}.
Estou aprendendo Python.
"""
```

📌 Muito útil para logs, relatórios e templates.

---

# 📊 Boas Práticas

## 🔹 Sempre normalizar dados

```python
nome = nome.strip().title()
```

---

## 🔹 Prefira f-strings

✔ Mais legível  
✔ Mais rápido  

---

## 🔹 Evite concatenação com +

❌ Ruim:
```python
nome + " tem " + str(idade)
```

✅ Melhor:
```python
f"{nome} tem {idade}"
```

---

## 🔹 Atenção à imutabilidade

Strings não podem ser alteradas diretamente:

❌
```python
nome[0] = "A"
```

---

## 🔹 Use slicing com cuidado

Evite índices fixos sem validação (dados podem variar).

---

# 📚 Conclusão

A manipulação de strings é essencial para qualquer profissional que trabalha com dados.

Dominar esse conceito permite:

- Limpar dados inconsistentes
- Padronizar informações
- Extrair dados relevantes
- Preparar dados para análise

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior](../2-IFs-For-While/README.md) | [⬇ Próximo módulo: Listas](../4-Listas/README.md)