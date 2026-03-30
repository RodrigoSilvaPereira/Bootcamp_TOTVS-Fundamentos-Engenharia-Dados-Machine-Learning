# 📌 Módulo: Operadores em Python

Este módulo apresenta os operadores da linguagem Python, fundamentais para manipulação de dados, construção de regras de negócio e criação de expressões lógicas.

Os operadores são amplamente utilizados em cenários reais como:

- Cálculo de métricas
- Validação de dados
- Regras de decisão
- Transformações em pipelines de dados

---

# 🎯 Objetivo do Módulo

Capacitar o profissional para:

- Utilizar operadores aritméticos para cálculos
- Aplicar operadores de comparação em validações
- Construir expressões lógicas complexas
- Manipular variáveis com operadores de atribuição
- Trabalhar com verificação de identidade e pertencimento

---

# 🧠 Conceitos Fundamentais

Operadores são símbolos utilizados para realizar operações sobre valores e variáveis.

Eles são essenciais para:

- Transformar dados
- Comparar informações
- Controlar fluxo de execução
- Implementar regras de negócio

---

# ⚙️ Funcionamento Geral

Os operadores atuam sobre operandos (valores ou variáveis), retornando um novo valor.

Exemplo:

```python
preco = 100
desconto = 20

preco_final = preco - desconto
```

📌 O operador `-` realiza uma operação entre dois valores, gerando um novo resultado.

---

# 🛠️ Tipos de Operadores

---

## 🔹 Operadores Aritméticos

Utilizados para realizar cálculos matemáticos.

### 📌 Exemplos aplicados

```python
# Cenário: cálculo de valor de venda

preco_unitario = 50
quantidade = 4

total_venda = preco_unitario * quantidade
print(total_venda)  # 200
```

### 📌 Operadores disponíveis

| Operador | Descrição            | Exemplo        |
|----------|---------------------|---------------|
| +        | Adição              | 10 + 5        |
| -        | Subtração           | 10 - 5        |
| *        | Multiplicação       | 10 * 5        |
| /        | Divisão             | 10 / 2        |
| //       | Divisão inteira     | 10 // 3       |
| %        | Módulo (resto)      | 10 % 3        |
| **       | Exponenciação       | 2 ** 3        |

---

### 📌 Precedência de Operadores

Ordem de execução:

1. Parênteses `()`
2. Exponenciação `**`
3. Multiplicação e divisão
4. Soma e subtração

```python
resultado = 10 + 5 * 2
print(resultado)  # 20
```

📌 Para alterar a ordem:

```python
resultado = (10 + 5) * 2
print(resultado)  # 30
```

---

## 🔹 Operadores de Comparação

Utilizados para comparar valores, retornando **True ou False**.

### 📌 Exemplo aplicado (validação de saque)

```python
saldo = 1000
saque = 200

pode_sacar = saldo >= saque
print(pode_sacar)  # True
```

### 📌 Operadores

| Operador | Descrição        |
|----------|------------------|
| ==       | Igualdade        |
| !=       | Diferença        |
| >        | Maior que        |
| >=       | Maior ou igual   |
| <        | Menor que        |
| <=       | Menor ou igual   |

---

## 🔹 Operadores de Atribuição

Utilizados para atribuir e atualizar valores em variáveis.

### 📌 Exemplo aplicado (controle de saldo)

```python
saldo = 500

saldo += 200  # depósito
saldo -= 100  # saque

print(saldo)  # 600
```

### 📌 Principais operadores

| Operador | Equivalente        |
|----------|--------------------|
| +=       | x = x + valor      |
| -=       | x = x - valor      |
| *=       | x = x * valor      |
| /=       | x = x / valor      |

---

## 🔹 Operadores Lógicos

Utilizados para combinar expressões booleanas.

### 📌 Exemplo aplicado (regra de negócio)

```python
saldo = 1000
saque = 200
limite = 300

pode_sacar = saldo >= saque and saque <= limite
print(pode_sacar)  # True
```

### 📌 Operadores

| Operador | Descrição |
|----------|----------|
| and      | E lógico |
| or       | OU lógico |
| not      | Negação  |

---

### 📌 Comportamento importante

```python
print(not "")        # True
print(not [1, 2])    # False
print(not 0)         # True
```

📌 Valores "vazios" são considerados False em Python.

---

## 🔹 Operadores de Identidade

Verificam se dois objetos ocupam o mesmo espaço na memória.

### 📌 Exemplo

```python
lista1 = [1, 2, 3]
lista2 = lista1

print(lista1 is lista2)  # True
```

📌 Diferente de `==`:

- `==` compara valor
- `is` compara referência na memória

---

## 🔹 Operadores de Associação

Verificam se um valor está presente em uma coleção.

### 📌 Exemplo aplicado (dados)

```python
clientes = ["Ana", "Carlos", "Maria"]

print("Ana" in clientes)      # True
print("João" not in clientes) # True
```

---

# 📊 Boas Práticas

## 🔹 Use parênteses para clareza

Mesmo quando não obrigatório:

```python
if (saldo >= saque) and (saque <= limite):
```

📌 Evita ambiguidade

---

## 🔹 Evite comparações desnecessárias

❌ Ruim:
```python
if saldo >= saque == True:
```

✅ Melhor:
```python
if saldo >= saque:
```

---

## 🔹 Cuidado com "is" vs "=="

❌ Erro comum:
```python
if valor is 10:
```

✅ Correto:
```python
if valor == 10:
```

---

## 🔹 Use operadores compostos

Melhora legibilidade e performance:

```python
saldo += 100
```

---

# 📚 Conclusão

Os operadores em Python são a base para qualquer tipo de manipulação de dados e construção de lógica.

Seu domínio permite:

- Criar regras de negócio eficientes
- Validar dados corretamente
- Construir algoritmos mais robustos