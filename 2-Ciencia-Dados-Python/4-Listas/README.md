# 📌 Módulo: Listas em Python

Este módulo aborda a estrutura de dados mais utilizada em Python: **listas**.

Listas são fundamentais para manipulação de dados em memória e servem como base para:

- Processamento de dados em lote
- Transformações em ETL
- Estruturas utilizadas em bibliotecas como Pandas e NumPy

---

# 🎯 Objetivo do Módulo

Capacitar o profissional para:

- Criar e manipular listas
- Acessar e modificar elementos
- Iterar sobre coleções de dados
- Aplicar transformações em massa
- Utilizar métodos essenciais da classe list

---

# 🧠 Conceitos Fundamentais

Listas em Python são:

- **Ordenadas** (mantêm a sequência)
- **Mutáveis** (podem ser alteradas)
- **Heterogêneas** (aceitam múltiplos tipos)

---

# ⚙️ Criação de Listas

## 🔹 Formas de criação

```python
frutas = ["laranja", "maçã", "uva"]
```

```python
frutas = []
```

```python
letras = list("python")
```

```python
numeros = list(range(10))
```

```python
carro = ["Ferrari", "F8", 4200000, 2020, True]
```

📌 Muito usado em pipelines para armazenar dados temporários.

---

# 🔎 Acesso a Elementos

## 🔹 Índices positivos

```python
frutas = ["maçã", "laranja", "uva", "pêra"]

print(frutas[0])  # maçã
print(frutas[2])  # uva
```

---

## 🔹 Índices negativos

```python
print(frutas[-1])  # pêra
print(frutas[-3])  # laranja
```

📌 Útil para acessar últimos registros.

---

# 🧩 Listas Aninhadas

Permitem representar estruturas mais complexas.

```python
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0][0])  # 1
```

📌 Muito usado em dados tabulares simples.

---

# ✂️ Fatiamento (Slicing)

Permite extrair subconjuntos.

```python
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])      # ['t', 'h', 'o', 'n']
print(lista[:2])      # ['p', 'y']
print(lista[1:3])     # ['y', 't']
print(lista[::2])     # ['p', 't', 'o']
print(lista[::-1])    # reverso
```

📌 Base para manipulação de dados em memória.

---

# 🔁 Iteração em Listas

## 🔹 Uso com for

```python
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
```

---

## 🔹 enumerate()

Retorna índice + valor.

```python
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

📌 Muito útil para logs e processamento estruturado.

---

# ⚡ List Comprehension

Forma eficiente e expressiva de criar listas.

---

## 🔹 Filtro

### Forma tradicional

```python
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
```

### Forma otimizada

```python
pares = [numero for numero in numeros if numero % 2 == 0]
```

---

## 🔹 Transformação

```python
quadrados = [numero ** 2 for numero in numeros]
```

📌 Muito utilizado em pipelines de transformação de dados.

---

# 🧰 Métodos da Classe List

---

## 🔹 append()

Adiciona elemento ao final.

```python
lista = []
lista.append(1)
lista.append("Python")
```

---

## 🔹 clear()

Remove todos os elementos.

```python
lista.clear()
```

---

## 🔹 copy()

Cria cópia da lista.

```python
nova_lista = lista.copy()
```

---

## 🔹 count()

Conta ocorrências.

```python
cores = ["azul", "verde", "azul"]
print(cores.count("azul"))  # 2
```

---

## 🔹 extend()

Adiciona múltiplos elementos.

```python
lista.extend(["java", "csharp"])
```

---

## 🔹 index()

Retorna posição do elemento.

```python
print(lista.index("java"))
```

---

## 🔹 pop()

Remove e retorna elemento.

```python
lista.pop()     # último
lista.pop(0)    # índice específico
```

---

## 🔹 remove()

Remove pelo valor.

```python
lista.remove("c")
```

---

## 🔹 reverse()

Inverte a lista.

```python
lista.reverse()
```

---

## 🔹 sort()

Ordena a lista.

```python
lista.sort()
```

```python
lista.sort(reverse=True)
```

### 📌 Ordenação personalizada

```python
lista.sort(key=lambda x: len(x))
```

---

# 🔢 Funções úteis

## 🔹 len()

Retorna tamanho.

```python
len(lista)
```

---

## 🔹 sorted()

Retorna nova lista ordenada.

```python
sorted(lista)
```

```python
sorted(lista, key=lambda x: len(x))
```

📌 Diferente de `sort()`, não altera a lista original.

---

# 📊 Boas Práticas

## 🔹 Prefira list comprehension

✔ Mais performático  
✔ Mais legível  

---

## 🔹 Evite mutação desnecessária

Sempre que possível:

```python
nova_lista = sorted(lista)
```

---

## 🔹 Cuidado com referências

```python
lista2 = lista  # mesma referência
```

Use:

```python
lista2 = lista.copy()
```

---

## 🔹 Nomeie listas corretamente

```python
clientes_ativos
valores_transacao
```

---

## 🔹 Evite listas muito grandes em memória

Para grandes volumes:

- Use generators
- Use processamento em batches

---

# 📚 Conclusão

Listas são a base da manipulação de dados em Python.

Dominar esse conceito permite:

- Processar dados em memória
- Aplicar transformações
- Preparar dados para análise
- Construir pipelines simples