# 📌 Módulo: Funções em Python

Este módulo aborda a definição, utilização e boas práticas relacionadas a **funções em Python**, um dos pilares da programação estruturada e modular.

Funções permitem encapsular lógica, promover reutilização de código e melhorar significativamente a organização e legibilidade de sistemas.

---

# 🎯 Objetivo do Módulo

Capacitar o uso de funções em Python para construção de códigos reutilizáveis, organizados e escaláveis, preparando o desenvolvedor para:

- Modularização de código
- Reutilização de lógica
- Organização de aplicações
- Construção de pipelines e rotinas de dados
- Desenvolvimento de soluções mais limpas e manuteníveis

---

# 🧠 Conceitos Fundamentais

## 🔹 O que é uma função?

Uma função é um bloco de código reutilizável, identificado por um nome, que pode receber parâmetros e retornar valores.

### 📌 Por que usar funções?

- Evita repetição de código (**DRY - Don't Repeat Yourself**)
- Facilita manutenção
- Melhora legibilidade
- Permite abstração de lógica complexa

---

## 🔹 Estrutura básica de uma função

```python
def nome_funcao(parametros):
    # bloco de código
    return valor
```

---

# ⚙️ Funcionamento / Arquitetura

## 🔹 Definindo e chamando funções

```python
def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem-vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2("Rodrigo")
exibir_mensagem_3()
```

### ✔️ Pontos importantes

- Parâmetros podem ter valores padrão
- Argumentos podem ser posicionais ou nomeados
- Funções podem ser reutilizadas em diferentes partes do código

---

## 🔹 Retorno de valores

Toda função em Python retorna um valor. Caso não haja `return`, o retorno padrão é `None`.

```python
def calcular_total(numeros):
    return sum(numeros)

def antecessor_sucessor(numero):
    return numero - 1, numero + 1

print(calcular_total([10, 20, 30]))  # 60
print(antecessor_sucessor(10))       # (9, 11)
```

### ✔️ Boas práticas

- Sempre deixe explícito o retorno
- Evite funções com múltiplas responsabilidades

---

## 🔹 Argumentos nomeados (Keyword Arguments)

Permitem maior clareza na chamada da função:

```python
def salvar_carro(marca, modelo, ano, placa):
    print(f"{marca}/{modelo}/{ano}/{placa}")

salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
```

---

## 🔹 *args e **kwargs

Permitem trabalhar com múltiplos argumentos dinâmicos.

### 📌 *args → múltiplos argumentos posicionais (tupla)

### 📌 **kwargs → múltiplos argumentos nomeados (dicionário)

```python
def exibir_dados(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

exibir_dados(1, 2, 3, nome="Rodrigo", idade=28)
```

---

## 🔹 Parâmetros especiais

### ✔️ Positional-only (somente por posição)

```python
def criar_carro(modelo, ano, placa, /, marca, motor):
    print(modelo, ano, placa, marca, motor)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0")
```

---

### ✔️ Keyword-only (somente por nome)

```python
def criar_carro(*, modelo, ano, placa, marca, motor):
    print(modelo, ano, placa, marca, motor)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0")
```

---

### ✔️ Misto (posicional + nomeado)

```python
def criar_carro(modelo, ano, placa, /, *, marca, motor):
    print(modelo, ano, placa, marca, motor)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0")
```

---

## 🔹 Funções como objetos (First-Class Functions)

Em Python, funções são objetos de primeira classe.

Isso permite:

- Atribuir funções a variáveis
- Passar funções como parâmetro
- Retornar funções

```python
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado: {resultado}")

exibir_resultado(10, 10, somar)
```

---

## 🔹 Escopo local e global

Python trabalha com escopos:

- Local → dentro da função
- Global → fora da função

```python
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))  # 2500
```

### ⚠️ Atenção

- Evite uso de `global`
- Prefira passar valores como parâmetro

---

# 🛠️ Exemplos Práticos

## 🔹 Função para validação de dados

```python
def validar_idade(idade):
    if idade < 0:
        return False
    return True
```

---

## 🔹 Função para transformação de dados (ETL)

```python
def normalizar_nome(nome):
    return nome.strip().title()

print(normalizar_nome("  rodrigo  "))
```

---

## 🔹 Função com lógica de negócio

```python
def calcular_desconto(valor, percentual):
    return valor - (valor * percentual / 100)

print(calcular_desconto(100, 10))  # 90
```

---

# 📊 Boas Práticas

## ✔️ Organização

- Uma função deve ter **uma única responsabilidade**
- Nomes devem ser claros e descritivos

## ✔️ Legibilidade

- Prefira funções curtas
- Evite aninhamentos excessivos

## ✔️ Performance

- Evite recalcular valores desnecessários
- Utilize funções built-in (ex: `sum`, `map`, `filter`)

## ✔️ Arquitetura

- Separe funções por domínio (ex: validação, transformação, cálculo)
- Utilize funções como base para pipelines de dados

---

# 📚 Conclusão

Funções são a base da programação estruturada em Python e fundamentais para construção de sistemas escaláveis.

Neste módulo, foram abordados:

- Definição e uso de funções
- Tipos de parâmetros
- Retorno de valores
- Uso avançado com `args` e `kwargs`
- Escopo e boas práticas

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior](../7-Dicionario/README.md) | [⬇ Próximo módulo: BDR - ETL](../../3-BDR-ETL/README.md)