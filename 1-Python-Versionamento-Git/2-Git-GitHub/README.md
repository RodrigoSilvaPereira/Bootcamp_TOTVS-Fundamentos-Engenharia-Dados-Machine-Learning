# 📌 Módulo: Versionamento de Código com Git e GitHub

Este módulo apresenta de forma prática e detalhada o uso do **Git** e do **GitHub**, com foco na execução real de comandos e no entendimento profundo de como o versionamento funciona.

O conteúdo foi estruturado para permitir que qualquer pessoa consiga seguir passo a passo e reproduzir todos os cenários apresentados.

---

# 🎯 Objetivo do Módulo

Capacitar o profissional para:

- Utilizar Git no dia a dia de desenvolvimento
- Controlar versões de código de forma segura
- Trabalhar com repositórios locais e remotos
- Entender profundamente o comportamento dos comandos
- Resolver conflitos e gerenciar histórico
- Aplicar boas práticas utilizadas no mercado

---

# ⚠️ Pré-requisitos

- Conhecimento básico de terminal (CLI)
- Noções básicas de programação

---

# 🧠 Conceitos Fundamentais

## 🔹 O que é Versionamento de Código

Versionamento de código é o processo de registrar alterações em arquivos ao longo do tempo, permitindo:

- Rastrear mudanças
- Recuperar versões anteriores
- Trabalhar em equipe com segurança

---

## 🔹 Git (Visão Técnica)

Git é um sistema de controle de versão distribuído baseado em snapshots (não diffs).

📌 Isso significa:
- Cada commit representa o estado completo do projeto
- Não apenas mudanças linha a linha

---

## 🔹 Áreas do Git

'''
Working Directory → Staging Area → Repository → Remote
'''

- **Working Directory** → onde você edita arquivos
- **Staging Area** → onde você prepara alterações
- **Repository** → histórico local
- **Remote** → repositório no GitHub

---

# 🛠️ Passo a Passo Completo

## 🔹 1. Instalação e Configuração

'''
git config --global user.name "seu_nome"
git config --global user.email "seu_email"
git config --global init.defaultBranch main
git config --global --list
'''

### 📌 Explicação

- `user.name` → define o autor dos commits  
- `user.email` → vincula commits à conta  
- `init.defaultBranch` → define branch padrão  
- `--list` → mostra todas configurações  

---

## 🔹 2. Criando Repositório Local

'''
mkdir projeto-git
cd projeto-git
git init
'''

### 📌 O que acontece

- Cria pasta `.git`
- Inicializa controle de versão
- Define a branch principal

---

## 🔹 3. Verificando Estado

'''
git status
'''

### 📌 O que faz

- Mostra arquivos modificados
- Mostra arquivos não rastreados
- Indica o que será commitado

---

## 🔹 4. Adicionando Arquivos (Staging)

'''
git add arquivo.txt
git add .
'''

### 📌 O que faz

- Move arquivos para staging area

### 📌 Diferença

- `arquivo.txt` → adiciona específico  
- `.` → adiciona todos  

---

## 🔹 5. Criando Commit

'''
git commit -m "mensagem"
'''

### 📌 O que faz

- Salva snapshot do projeto
- Registra no histórico

### 📌 Boa prática

- Mensagem clara e objetiva

---

## 🔹 6. Histórico de Commits

'''
git log
'''

### 📌 O que faz

- Lista commits com hash, autor e data

---

# 🔐 Conectando ao GitHub

## 🔹 Adicionar repositório remoto

'''
git remote add origin URL_GITHUB
git remote -v
'''

### 📌 O que faz

- Conecta repositório local ao remoto

---

## 🔹 Enviando código

'''
git push -u origin main
'''

### 📌 O que faz

- Envia commits para o GitHub
- `-u` define upstream (facilita próximos pushes)

---

## 🔹 Clonando repositório

'''
git clone URL_GITHUB
'''

### 📌 O que faz

- Cria cópia local do repositório remoto

---

# 🔄 Manipulação de Alterações

## 🔹 Restaurar arquivo

'''
git restore arquivo.txt
'''

### 📌 O que faz

- Descarta alterações não commitadas

---

## 🔹 Remover do staging

'''
git restore --staged arquivo.txt
'''

### 📌 O que faz

- Remove arquivo do stage sem apagar alterações

---

## 🔹 Alterar último commit

'''
git commit --amend -m "nova mensagem"
'''

### 📌 O que faz

- Reescreve último commit

---

# ⚠️ Controle de Histórico (RESET)

## 🔹 git reset --soft

'''
git reset --soft HASH
'''

- Move ponteiro do commit  
- Mantém arquivos no stage  

---

## 🔹 git reset --mixed

'''
git reset --mixed HASH
'''

- Remove do stage  
- Mantém alterações  

---

## 🔹 git reset --hard

'''
git reset --hard HASH
'''

- Apaga alterações  
- Restaura estado do commit  

⚠️ **Perigoso — perda de dados**

---

## 🔹 Recuperação

'''
git reflog
'''

### 📌 O que faz

- Mostra histórico completo de ações
- Permite recuperar commits

---

# 🌿 Branches

## 🔹 Criar branch

'''
git checkout -b nova-branch
'''

### 📌 O que faz

- Cria e troca de branch

---

## 🔹 Trocar branch

'''
git checkout main
'''

---

## 🔹 Listar branches

'''
git branch
'''

---

## 🔹 Merge

'''
git merge branch
'''

### 📌 O que faz

- Junta histórico de duas branches

---

## 🔹 Deletar branch

'''
git branch -d branch
'''

---

# ⚠️ Conflitos de Merge

## Passo a passo real:

1. Alterar arquivo local
2. Alterar mesmo arquivo no GitHub
3. Executar:

'''
git pull
'''

4. Resolver conflito manualmente
5. Finalizar:

'''
git add .
git commit -m "resolvendo conflito"
git push
'''

---

# 📁 .gitignore

'''
echo pasta/ > .gitignore
'''

### 📌 O que faz

- Ignora arquivos/pastas no versionamento

---

# 🧰 Comandos Avançados (Detalhados)

## 🔹 git fetch

'''
git fetch origin main
'''

- Atualiza referências remotas  
- NÃO altera seu código  

---

## 🔹 git diff

'''
git diff main origin/main
'''

- Mostra diferenças entre versões  

---

## 🔹 git stash

'''
git stash
'''

- Salva alterações temporariamente  

---

## 🔹 git stash list

'''
git stash list
'''

- Lista stashes  

---

## 🔹 git stash pop

'''
git stash pop
'''

- Recupera e remove stash  

---

## 🔹 git clone com branch

'''
git clone URL --branch teste --single-branch
'''

- Clona apenas uma branch  

---

# 📊 Boas Práticas

- Commits pequenos e frequentes  
- Mensagens claras  
- Uso de branches  
- Evitar commits diretos na main  
- Sempre usar pull antes de push  
- Revisar mudanças com diff  

---

# 🚀 Próximos Passos

- Git Flow
- Pull Requests
- Code Review
- CI/CD
- Versionamento em pipelines de dados

---

# 📚 Conclusão

Este módulo apresentou o uso completo do Git e GitHub com foco em execução prática e entendimento profundo dos comandos.

O domínio dessas ferramentas é essencial para qualquer profissional de tecnologia, sendo base para colaboração, controle e escalabilidade de projetos.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior](../1-Introducao-Python/README.md) | [⬇ Próximo módulo: Ciência de Dados - Python](../../2-Ciencia-Dados-Python/README.md)