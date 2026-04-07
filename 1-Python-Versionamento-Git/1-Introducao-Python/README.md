# 📌 Módulo: Introdução ao Python

Este módulo apresenta os fundamentos da linguagem **Python**, abordando desde a configuração do ambiente até os conceitos essenciais de programação utilizados no desenvolvimento de aplicações e manipulação de dados.

---

# 🎯 Objetivo do Módulo

Capacitar o profissional para:

- Configurar corretamente o ambiente de desenvolvimento Python
- Compreender os principais tipos de dados da linguagem
- Utilizar variáveis e constantes de forma adequada
- Trabalhar com entrada e saída de dados
- Executar código em modo interativo
- Aplicar boas práticas de nomenclatura e organização

---

# ⚠️ Pré-requisitos

Para melhor aproveitamento do conteúdo:

- Conhecimento básico em lógica de programação (opcional)
- Noções básicas de uso de computador e terminal

---

# 🗂️ Estrutura do Conteúdo

Este módulo está organizado da seguinte forma:

- Configuração do ambiente
- Primeiro programa em Python
- Tipos de dados
- Modo interativo
- Variáveis e constantes
- Conversão de tipos
- Entrada e saída de dados

---

# 🧠 Conceitos Fundamentais

## 🔹 Configuração do Ambiente

Antes de iniciar o desenvolvimento em Python, é necessário preparar o ambiente:

### Instalação do Python
- Download oficial: https://www.python.org/downloads/
- Durante a instalação, marque a opção **"Add Python to PATH"**

### Verificação da instalação

```text
python -V
```

Se o comando retornar a versão instalada, o ambiente está corretamente configurado.

---

### IDE Recomendada

- Visual Studio Code: https://code.visualstudio.com/download

Extensões recomendadas:
- Python
- GitHub Copilot
- autoDocstring

---

## 🔹 Primeiro Programa

Criando o clássico "Hello World":

```python
print("Hello World!")
```

### Execução:

```text
python primeiro_programa.py
```

---

## 🔹 Tipos de Dados

Os tipos de dados definem o comportamento e a forma como os valores são armazenados na memória.

### 📊 Tipos Built-in do Python

| Categoria   | Tipos                          |
|------------|--------------------------------|
| Texto       | str                            |
| Numérico    | int, float, complex            |
| Sequência   | list, tuple, range             |
| Mapeamento  | dict                           |
| Conjunto    | set, frozenset                 |
| Booleano    | bool                           |
| Binário     | bytes, bytearray, memoryview   |

---

### Exemplos

```python
int_type = 10
float_type = 22.5
boolean_type = True
string_type = "Texto"
```

---

## 🔹 Modo Interativo

O modo interativo permite executar comandos Python em tempo real, sendo ideal para testes e aprendizado.

### Executar modo interativo:

```text
python
```

Ou executar um script e permanecer no modo interativo:

```text
python -i meu_script.py
```

### Encerrar:

```python
exit()
```

---

### 🔹 Funções úteis: dir() e help()

#### dir()
Lista atributos e métodos disponíveis:

```python
dir()
dir(100)
```

#### help()
Acessa a documentação integrada:

```python
help()
help(int)
```

---

## 🔹 Variáveis

Variáveis são utilizadas para armazenar valores em tempo de execução.

Em Python, não é necessário declarar o tipo explicitamente (tipagem dinâmica).

```python
age = 21
name = "Rodrigo"

print(f"Meu nome é {name} e eu tenho {age} anos.")
```

### Declaração múltipla:

```python
age, name = 21, "Rodrigo"
```

---

## 🔹 Constantes

Python não possui constantes nativas, mas utiliza convenção:

- Variáveis em **letras maiúsculas** representam constantes

```python
AGE = 21
NAME = "Rodrigo"
```

📌 **Boa prática:** não alterar valores definidos como constantes.

---

## 🔹 Padrões de Nomenclatura

- Utilizar **snake_case**
- Nomes descritivos e significativos
- Constantes em **UPPER_CASE**

✔ Exemplo correto:

```python
user_age = 25
MAX_CONNECTIONS = 100
```

---

## 🔹 Conversão de Tipos

Permite transformar um tipo de dado em outro.

### Exemplos:

```python
preco = 10
print(type(preco))

preco = float(preco)
print(type(preco))

preco = "10"
preco = int(preco)
print(type(preco))
```

### ⚠️ Atenção

Conversões inválidas geram erro:

```python
int("abc")  # ValueError
```

---

## 🔹 Entrada e Saída de Dados

### 📥 Função input()

Responsável por capturar dados do usuário:

```python
nome = input("Digite seu nome: ")
```

📌 O valor retornado é sempre do tipo **string**.

---

### 📤 Função print()

Exibe dados na saída padrão.

#### Estrutura:

```python
print(objetos, sep=" ", end="\n")
```

### Parâmetros:

- **sep** → separador entre valores
- **end** → caractere final
- **file** → destino da saída
- **flush** → força escrita imediata

### Exemplo:

```python
print("Python", "é", "incrível", sep="-", end="!\n")
```

---

# ⚙️ Funcionamento Interno

Python é uma linguagem:

- **Interpretada** → código executado linha a linha
- **Dinamicamente tipada** → tipos definidos em tempo de execução
- **Gerenciada por memória automática (Garbage Collector)**

Fluxo básico:

1. Código fonte (.py)
2. Interpretador Python
3. Bytecode
4. Execução pela máquina virtual Python (PVM)

---

# 🛠️ Exemplos Práticos

### Exemplo completo:

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá, {nome}. Você tem {idade} anos.")
```

---

# 📊 Boas Práticas Aplicadas

- Utilizar nomes descritivos para variáveis
- Evitar variáveis com nomes genéricos (`x`, `y`)
- Separar responsabilidades no código
- Evitar conversões desnecessárias
- Validar entradas do usuário
- Seguir padrão de nomenclatura consistente
- Utilizar o modo interativo para testes rápidos

---

# 🚀 Próximos Passos

Após dominar este módulo, avance para:

- Estruturas condicionais (`if`, `else`)
- Laços de repetição (`for`, `while`)
- Estruturas de dados (listas, dicionários)
- Funções e modularização

---

# 📚 Conclusão

Este módulo estabelece a base fundamental para desenvolvimento em Python, abordando desde configuração do ambiente até conceitos essenciais como variáveis, tipos de dados e entrada/saída.

Esses conhecimentos são indispensáveis para evolução em áreas como **Engenharia de Dados, Análise de Dados e Machine Learning**, servindo como alicerce para construção de soluções mais complexas.

---

> [🏠 Voltar ao índice](../../README.md) | [⬇ Próximo módulo: Git - Github](../2-Git-GitHub/README.md)