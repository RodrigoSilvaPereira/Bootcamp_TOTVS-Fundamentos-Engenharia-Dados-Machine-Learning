# 📌 Módulo: Estruturas Condicionais e de Repetição

Este módulo aborda estruturas fundamentais de controle de fluxo em Python, utilizadas para tomada de decisão e execução repetitiva de código.

Essas estruturas são essenciais em cenários reais como:

- Validação de dados
- Regras de negócio
- Processamento de registros
- Construção de pipelines de dados

---

# 🎯 Objetivo do Módulo

Capacitar o profissional para:

- Controlar o fluxo de execução com condições
- Implementar regras de decisão
- Iterar sobre estruturas de dados
- Criar loops eficientes e controlados
- Evitar erros comuns em lógica de repetição

---

# 🧠 Conceitos Fundamentais

Estruturas de controle permitem alterar o fluxo natural do programa:

- **Condicionais (if)** → executam código com base em regras
- **Laços (for / while)** → repetem código

---

# ⚙️ Identação e Blocos de Código

Em Python, a identação define blocos de execução.

### 📌 Regra padrão

- 4 espaços por nível
- Evitar misturar TAB e espaço

### 📌 Exemplo

```python
def sacar(saldo, valor):
    if saldo >= valor:
        saldo -= valor
    return saldo
```

📌 Diferente de outras linguagens, não há `{}` — a identação é obrigatória.

---

# 🛠️ Estruturas Condicionais

## 🔹 if

Executa um bloco se a condição for verdadeira.

### 📌 Exemplo aplicado

```python
saldo = 1000
saque = 200

if saldo >= saque:
    print("Saque realizado")
```

---

## 🔹 if / else

Define dois fluxos: verdadeiro ou falso.

```python
if saldo >= saque:
    print("Saque realizado")
else:
    print("Saldo insuficiente")
```

---

## 🔹 if / elif / else

Utilizado para múltiplas condições.

### 📌 Exemplo aplicado (menu)

```python
opcao = 2

if opcao == 1:
    print("Saque realizado")
elif opcao == 2:
    print("Exibindo extrato")
else:
    print("Opção inválida")
```

---

## 🔹 IF Aninhado

Permite criar validações mais complexas.

### 📌 Exemplo aplicado (regra de negócio)

```python
conta_especial = True
saldo = 500
saque = 600
limite = 200

if conta_especial:
    if saldo + limite >= saque:
        print("Saque permitido com limite")
    else:
        print("Saldo insuficiente")
else:
    if saldo >= saque:
        print("Saque permitido")
    else:
        print("Saldo insuficiente")
```

---

## 🔹 IF Ternário

Forma reduzida de escrever uma condição.

```python
status = "Aprovado" if saldo >= saque else "Negado"
```

📌 Use apenas para condições simples.

---

# 🔁 Estruturas de Repetição

---

## 🔹 For

Utilizado para percorrer estruturas iteráveis.

### 📌 Estrutura do for

```python
for elemento in iteravel:
    # bloco de código
```

- `elemento` → variável temporária
- `iteravel` → lista, string, etc.

---

### 📌 Exemplo aplicado (dados)

```python
clientes = ["Ana", "Carlos", "Maria"]

for cliente in clientes:
    print(f"Processando cliente: {cliente}")
```

---

### 📌 Exemplo com validação

```python
valores = [10, 25, 30, 5]

for valor in valores:
    if valor > 20:
        print(f"Valor alto: {valor}")
```

---

## 🔹 For com else

Executa o `else` quando o loop termina normalmente (sem break).

```python
for numero in range(3):
    print(numero)
else:
    print("Loop finalizado")
```

---

## 🔹 Função range()

Gera sequência de números.

### 📌 Estrutura

```python
range(start, stop, step)
```

- `start` → início (opcional)
- `stop` → fim (obrigatório)
- `step` → passo (opcional)

---

### 📌 Exemplos

```python
list(range(4))  # [0, 1, 2, 3]
```

```python
for i in range(0, 11):
    print(i)
```

```python
for i in range(0, 51, 5):
    print(i)
```

---

## 🔹 While

Executa enquanto a condição for verdadeira.

### 📌 Exemplo aplicado

```python
saldo = 1000

while saldo > 0:
    print("Saldo disponível")
    saldo -= 200
```

---

## 🔹 While com controle de menu

```python
opcao = -1

while opcao != 0:
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Extrato...")
```

---

## 🔹 While com else

```python
while False:
    print("Nunca executa")
else:
    print("Finalizado")
```

---

# 🔄 Controle de Fluxo em Loops

## 🔹 break

Interrompe o loop imediatamente.

```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
```

---

## 🔹 continue

Pula para a próxima iteração.

```python
for numero in range(10):
    if numero % 2 == 0:
        continue
    print(numero)
```

📌 Exemplo acima imprime apenas números ímpares.

---

# 📊 Boas Práticas

## 🔹 Evite ifs aninhados complexos

Prefira simplificar:

❌ Ruim:
```python
if a:
    if b:
```

✅ Melhor:
```python
if a and b:
```

---

## 🔹 Use nomes claros

```python
if saldo_suficiente:
```

---

## 🔹 Cuidado com loops infinitos

```python
while True:
```

Sempre use com controle:

```python
if condicao:
    break
```

---

## 🔹 Prefira for quando possível

- Mais seguro
- Menos propenso a erro

---

# 📚 Conclusão

As estruturas condicionais e de repetição são fundamentais para construção de lógica em Python.

Elas permitem:

- Criar regras de decisão
- Processar grandes volumes de dados
- Controlar fluxos complexos

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior](../1-Operadores/README.md) | [⬇ Próximo módulo: Strings](../3-Strings/README.md)