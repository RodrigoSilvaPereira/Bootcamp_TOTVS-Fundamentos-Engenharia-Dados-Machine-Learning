# 📌 Módulo: Tuplas em Python

Este módulo aborda a estrutura de dados **tupla**, muito semelhante às listas, porém com uma característica fundamental: **imutabilidade**.

Tuplas são amplamente utilizadas em cenários onde os dados **não devem ser alterados**, garantindo maior segurança e previsibilidade no código.

---

# 🎯 Objetivo do Módulo

Capacitar o profissional para:

- Entender o conceito de imutabilidade
- Criar e utilizar tuplas corretamente
- Acessar e percorrer dados imutáveis
- Aplicar tuplas em cenários reais de dados

---

# 🧠 Conceitos Fundamentais

Tuplas em Python são:

- **Ordenadas**
- **Imutáveis**
- **Indexadas**
- **Heterogêneas**

📌 Diferente das listas, **não permitem alteração após criação**.

---

# ⚙️ Criação de Tuplas

## 🔹 Formas de criação

### 📌 Com parênteses

```python
frutas = ("laranja", "pera", "uva")
```

---

### 📌 Com vírgula (forma implícita)

```python
frutas = "laranja", "pera", "uva"
```

---

### 📌 Tupla com um único elemento

⚠️ Atenção: precisa da vírgula

```python
pais = ("Brasil",)
```

---

### 📌 Usando a função tuple()

```python
letras = tuple("python")
```

```python
numeros = tuple([1, 2, 3, 4])
```

---

# 🔎 Acesso a Elementos

## 🔹 Índices positivos

```python
frutas = ("maçã", "laranja", "uva")

print(frutas[0])  # maçã
print(frutas[1])  # laranja
```

---

## 🔹 Índices negativos

```python
print(frutas[-1])  # uva
```

📌 Muito útil para acessar últimos registros.

---

# 🧩 Tuplas Aninhadas

Permitem estruturas mais complexas.

```python
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

print(matriz[0])      # (1, "a", 2)
print(matriz[0][0])   # 1
```

📌 Utilizado em dados estruturados e leitura de registros.

---

# ✂️ Fatiamento (Slicing)

Funciona da mesma forma que listas.

```python
letras = ("p", "y", "t", "h", "o", "n")

print(letras[2:])    # ('t', 'h', 'o', 'n')
print(letras[:2])    # ('p', 'y')
print(letras[1:3])   # ('y', 't')
print(letras[::2])   # ('p', 't', 'o')
print(letras[::-1])  # reverso
```

---

# 🔁 Iteração em Tuplas

## 🔹 Uso com for

```python
carros = ("gol", "celta", "palio")

for carro in carros:
    print(carro)
```

---

## 🔹 enumerate()

```python
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

---

# 🚫 Imutabilidade na Prática

Tuplas **não permitem alteração**:

❌
```python
frutas[0] = "banana"
```

✔ Isso gera erro: `TypeError`

---

# 🧰 Métodos da Classe Tuple

Tuplas possuem poucos métodos devido à imutabilidade.

---

## 🔹 count()

Conta ocorrências.

```python
cores = ("azul", "verde", "azul")

print(cores.count("azul"))  # 2
```

---

## 🔹 index()

Retorna índice do elemento.

```python
print(cores.index("verde"))  # 1
```

---

## 🔹 len()

```python
len(cores)
```

---

# ⚖️ Lista vs Tupla

| Característica | Lista | Tupla |
|------|--------|--------|
| Mutabilidade | Mutável | Imutável |
| Performance | Menor | Maior |
| Segurança | Menor | Maior |
| Uso comum | Dados dinâmicos | Dados fixos |

---

# 📊 Boas Práticas

## 🔹 Use tuplas para dados imutáveis

Exemplo:

```python
coordenadas = (-23.55, -46.63)
```

---

## 🔹 Prefira tuplas para performance

- Mais leves
- Mais rápidas
- Menor uso de memória

---

## 🔹 Use tuplas para retorno de funções

```python
def obter_usuario():
    return "Rodrigo", 28
```

---

## 🔹 Evite usar tuplas quando precisar alterar dados

Nesse caso, use listas.

---

# 📚 Conclusão

Tuplas são ideais para representar dados que:

- Não devem ser alterados
- Precisam de consistência
- Devem ser mais performáticos

Elas são muito utilizadas em:

- Coordenadas
- Configurações
- Retornos de funções
- Estruturas fixas