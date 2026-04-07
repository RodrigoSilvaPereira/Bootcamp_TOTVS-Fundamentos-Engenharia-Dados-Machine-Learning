# 📌 Módulo: Dicionários em Python

Este módulo aborda a estrutura de dados **dicionário (dict)**, utilizada para armazenar dados no formato **chave → valor**.

Dicionários são fundamentais em engenharia de dados, pois representam diretamente estruturas como:

- JSON
- Respostas de APIs
- Dados semi-estruturados
- Registros de banco de dados

---

# 🎯 Objetivo do Módulo

Capacitar o profissional para:

- Criar e manipular dicionários
- Trabalhar com dados estruturados
- Acessar e modificar informações de forma eficiente
- Utilizar métodos essenciais da classe dict
- Preparar dados para integração com APIs e bancos

---

# 🧠 Conceitos Fundamentais

Dicionários em Python são:

- Estruturas **não ordenadas** (conceitualmente)
- Compostos por pares **chave: valor**
- **Mutáveis**
- Com **chaves únicas**

📌 As chaves devem ser tipos imutáveis (str, int, tuple, etc.)

---

# ⚙️ Criação de Dicionários

## 🔹 Forma literal

```python
pessoa = {"nome": "Rodrigo", "idade": 21}
```

---

## 🔹 Usando dict()

```python
pessoa = dict(nome="Rodrigo", idade=28)
```

---

## 🔹 Adicionando novos campos

```python
pessoa["telefone"] = "3333-1234"
```

---

# 🔎 Acesso e Manipulação de Dados

```python
dados = {"nome": "Rodrigo", "idade": 21}

print(dados["nome"])
print(dados["idade"])
```

---

## 🔹 Atualizando valores

```python
dados["nome"] = "Maria"
```

---

## 🔹 Problema comum (KeyError)

❌
```python
dados["endereco"]
```

✔ Solução segura:

```python
dados.get("endereco")
```

---

# 🧩 Dicionários Aninhados

Estruturas extremamente comuns em dados reais.

```python
contatos = {
    "ana@email.com": {"nome": "Ana", "telefone": "1111-1111"},
    "bob@email.com": {"nome": "Bob", "telefone": "2222-2222"}
}

print(contatos["ana@email.com"]["telefone"])
```

📌 Isso é equivalente a JSON.

---

# 🔁 Iteração em Dicionários

---

## 🔹 Percorrendo chaves

```python
for chave in contatos:
    print(chave, contatos[chave])
```

---

## 🔹 Percorrendo chave e valor

```python
for chave, valor in contatos.items():
    print(chave, valor)
```

📌 Forma mais recomendada.

---

# 🧰 Métodos da Classe Dict

---

## 🔹 clear()

Remove todos os elementos.

```python
contatos.clear()
```

---

## 🔹 copy()

Cria cópia do dicionário.

```python
copia = contatos.copy()
```

---

## 🔹 fromkeys()

Cria dicionário com chaves padrão.

```python
dict.fromkeys(["nome", "telefone"], None)
```

---

## 🔹 get()

Acesso seguro.

```python
contatos.get("chave")
contatos.get("chave", {})
```

📌 Evita erro (KeyError)

---

## 🔹 items()

Retorna pares chave-valor.

```python
contatos.items()
```

---

## 🔹 keys()

Retorna apenas as chaves.

```python
contatos.keys()
```

---

## 🔹 values()

Retorna apenas os valores.

```python
contatos.values()
```

---

## 🔹 pop()

Remove chave específica.

```python
contatos.pop("email")
```

---

## 🔹 popitem()

Remove último item inserido.

```python
contatos.popitem()
```

---

## 🔹 setdefault()

Adiciona chave se não existir.

```python
contato.setdefault("idade", 28)
```

---

## 🔹 update()

Atualiza ou adiciona múltiplos valores.

```python
contatos.update({"email": {"nome": "Novo"}})
```

---

# 🔍 Operações com Dicionários

---

## 🔹 Verificar existência

```python
"email" in contatos
```

---

## 🔹 Remoção com del

```python
del contatos["email"]
```

---

# 📊 Boas Práticas

## 🔹 Use get() ao acessar dados externos

✔ Evita erros em APIs e JSON

---

## 🔹 Nomeie chaves de forma consistente

```python
"user_id"
"created_at"
```

---

## 🔹 Evite estruturas muito profundas

Prefira normalização quando possível.

---

## 🔹 Use dicionários para representar registros

```python
usuario = {
    "id": 1,
    "nome": "Rodrigo",
    "email": "email@email.com"
}
```

---

## 🔹 Combine com list para datasets

```python
usuarios = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Carlos"}
]
```

📌 Estrutura base de dados em memória.

---

# 📚 Conclusão

Dicionários são a estrutura mais importante para manipulação de dados em Python.

Eles permitem:

- Representar dados estruturados
- Trabalhar com APIs e JSON
- Organizar informações de forma eficiente
- Construir pipelines de dados

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior](../6-Conjuntos/README.md) | [⬇ Próximo módulo: Funções](../8-Funcoes/README.md)