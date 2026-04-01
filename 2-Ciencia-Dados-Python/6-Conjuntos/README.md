# 📌 Módulo: Conjuntos (Sets) em Python

Este módulo aborda a estrutura de dados **set**, utilizada para representar coleções de elementos **únicos e não ordenados**.

Sets são amplamente utilizados em cenários de dados para:

- Remoção de duplicidades
- Comparação entre datasets
- Operações matemáticas (união, interseção)
- Otimização de performance em buscas

---

# 🎯 Objetivo do Módulo

Capacitar o profissional para:

- Trabalhar com dados únicos
- Eliminar duplicidades de forma eficiente
- Realizar operações entre conjuntos
- Utilizar sets para otimização de performance

---

# 🧠 Conceitos Fundamentais

Sets em Python são:

- **Não ordenados**
- **Não indexados**
- **Mutáveis**
- **Sem elementos duplicados**

---

# ⚙️ Criação de Conjuntos

## 🔹 Exemplos

```python
set([1, 2, 3, 1, 3, 4])  
# {1, 2, 3, 4}
```

```python
set("abacaxi")  
# {'a', 'b', 'c', 'x', 'i'}
```

```python
set(("palio", "gol", "celta", "palio"))  
# {'gol', 'celta', 'palio'}
```

```python
linguagens = {"python", "java", "python"}  
# {'python', 'java'}
```

📌 Sets removem duplicidade automaticamente.

---

# ⚠️ Importante: Não possuem ordem

```python
numeros = {1, 2, 3}
```

📌 A ordem dos elementos não é garantida.

---

# 🔎 Acessando Dados

Sets **não suportam indexação**.

❌
```python
numeros[0]
```

✔ Alternativa:

```python
numeros = {1, 2, 3}
lista = list(numeros)

print(lista[0])
```

📌 Use apenas se realmente precisar de índice.

---

# 🔁 Iteração em Sets

```python
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)
```

---

## 🔹 enumerate()

```python
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

📌 Ordem pode variar a cada execução.

---

# 🧮 Operações Matemáticas

---

## 🔹 union() → União

```python
a = {1, 2}
b = {3, 4}

print(a.union(b))  
# {1, 2, 3, 4}
```

---

## 🔹 intersection() → Interseção

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))  
# {2, 3}
```

📌 Muito usado para encontrar dados em comum.

---

## 🔹 difference() → Diferença

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.difference(b))  # {1}
print(b.difference(a))  # {4}
```

---

## 🔹 symmetric_difference()

```python
print(a.symmetric_difference(b))  
# {1, 4}
```

📌 Elementos exclusivos de cada conjunto.

---

# 🔍 Relações entre Conjuntos

---

## 🔹 issubset()

```python
a.issubset(b)
```

📌 Verifica se A está contido em B.

---

## 🔹 issuperset()

```python
b.issuperset(a)
```

📌 Verifica se B contém A.

---

## 🔹 isdisjoint()

```python
a.isdisjoint(b)
```

📌 Verifica se não possuem interseção.

---

# 🧰 Métodos da Classe Set

---

## 🔹 add()

Adiciona elemento.

```python
sorteio = {1, 23}
sorteio.add(25)
```

---

## 🔹 clear()

Remove todos os elementos.

```python
sorteio.clear()
```

---

## 🔹 copy()

Cria cópia do conjunto.

```python
novo = sorteio.copy()
```

---

## 🔹 discard()

Remove elemento sem erro.

```python
numeros.discard(1)
```

📌 Não gera erro se não existir.

---

## 🔹 remove()

```python
numeros.remove(2)
```

⚠️ Gera erro se o elemento não existir.

---

## 🔹 pop()

Remove elemento aleatório.

```python
numeros.pop()
```

📌 Não garante qual elemento será removido.

---

# 🔢 Funções úteis

## 🔹 len()

```python
len(numeros)
```

---

## 🔹 in

```python
1 in numeros
```

📌 Busca extremamente rápida (O(1)).

---

# 📊 Boas Práticas

## 🔹 Use sets para remover duplicados

```python
lista = [1, 2, 2, 3]
unicos = list(set(lista))
```

---

## 🔹 Use sets para validações rápidas

```python
if item in conjunto:
```

✔ Muito mais rápido que listas

---

## 🔹 Evite depender da ordem

Sets não são ordenados.

---

## 🔹 Prefira discard ao invés de remove

Evita exceções desnecessárias.

---

## 🔹 Use sets em joins manuais

📌 Exemplo (engenharia de dados):

```python
ids_validos = {1, 2, 3}

dados = [1, 4, 2, 5]

filtrados = [x for x in dados if x in ids_validos]
```

---

# 📚 Conclusão

Sets são ideais para:

- Remover duplicidade
- Realizar operações matemáticas
- Otimizar buscas
- Comparar conjuntos de dados

Eles são fundamentais em pipelines de dados eficientes.