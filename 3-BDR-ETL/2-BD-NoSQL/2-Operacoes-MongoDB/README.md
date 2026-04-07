# 📌 Módulo: Operações MongoDB

Este módulo aborda as operações práticas no MongoDB, incluindo criação de databases, collections, inserção, consulta, atualização e exclusão de documentos.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Criar databases e collections no MongoDB
- Inserir documentos individuais ou múltiplos utilizando insertOne e insertMany
- Consultar documentos com find, findOne e operadores lógicos/comparação
- Atualizar documentos com updateOne, updateMany e operadores como $set, $inc, $rename
- Excluir documentos com deleteOne e deleteMany
- Aplicar projeção, ordenação, limitação e paginação em consultas

---

# 📚 Conteúdos Abordados

## 🔹 Criando um Database

```javascript
use {{nome_do_banco}}
```

Enquanto o database não tiver uma collection ele não será apresentado na lista.

**Para criar um database no Compass é necessário criar uma collection também** devido a interface.

Abra a opção do mongosh para acessar a linha de comando do banco.

## 🔹 Criando Collection

```javascript
db.createCollection("usuarios")
db.createCollection("destinos")
```

Ou você pode inserir diretamente um documento e ele já irá criar a collection:

```javascript
db.usuarios_novo.insertOne({});
```

## 🔹 Mostrando Collections

```javascript
show collections
```

## 🔹 Inserindo Dados em uma Collection

Você pode inserir apenas um documento por vez:

```javascript
db.usuarios.insertOne(
    {   
        "nome": "nome",
        "data_nascimento": "1990-10-05",
        "email": "pamela.apolinario.borges@gmail.com",
        "endereco": "Av Manoel Marques de Jesus, 380 - Vila Xavier, Araraquara/SP"
    });

db.destinos.insertOne({"nome":"Praia do Rosa", "descricao":"Linda praia"})
```

Ou vários documentos por vez:

```javascript
db.usuarios.insertMany([
    {   
        "nome": "Pamela",
        "idade": 30,
        "email": "pamela.apolinario.borges@gmail.com",
        "endereco": "Av Manoel Marques de Jesus, 380 - Vila Xavier, Araraquara/SP"
    },
    {   
        "nome": "Pamela",
        "idade": 31,
        "email": "pamela.apolinario.borges.outra@gmail.com",
        "endereco": "Av Manoel Marques de Jesus, 380 - Vila Xavier, Araraquara/SP"
    }
]);
```

## 🔹 Listar Documentos de uma Coleção

Exemplo:

```javascript
// Lista todos os documentos da coleção "clientes"
db.usuarios.find()
```

Se quiser exibir de forma mais legível no shell:

```javascript
db.usuarios.find().pretty()
```

**Observações:** Para filtrar resultados, passe um objeto de consulta:

```javascript
db.usuarios.find({ idade: { $gte: 18 } })
```

Para limitar a quantidade de documentos retornados:

```javascript
db.usuarios.find().limit(10)
```

## 🔹 Populando nosso Banco de Dados para Próximas Operações

```javascript
// Inserir documentos na coleção "usuarios"
db.usuarios.insertMany([{
    nome: "João",
    idade: 25,
    cidade: "São Paulo",
    estado: "SP",
    endereco: {
      rua: "Avenida Principal",
      numero: 123,
      cidade: "São Paulo",
      estado: "SP"
    }
  }, {
    nome: "Maria",
    idade: 30,
    cidade: "Rio de Janeiro",
    estado: "RJ",
    endereco: {
      rua: "Rua Secundária",
      numero: 456,
      cidade: "Rio de Janeiro",
      estado: "RJ"
    }
},{
    nome: "Carlos",
    idade: 20,
    cidade: "São Paulo",
    estado: "SP",
    endereco: {
      rua: "Rua Principal",
      numero: 789,
      cidade: "São Paulo",
      estado: "SP"
    }
  },{
    nome: "Ana",
    idade: 35,
    cidade: "São Paulo",
    estado: "SP",
    endereco: {
      rua: "Avenida Secundária",
      numero: 1011,
      cidade: "São Paulo",
      estado: "SP"
    }
    },  
    {
    nome: "Pedro",
    idade: 28,
    cidade: "Belo Horizonte",
    estado: "MG",
    endereco: {
      rua: "Rua Principal",
      numero: 1314,
      cidade: "Belo Horizonte",
      estado: "MG"
    }
  }]);
```

## 🔹 Mais Comandos Find

```javascript
db.usuarios.find({});
db.usuarios.find({"nome": "João"});
db.usuarios.findOne({"nome": "João"});
db.usuarios.findOneAndUpdate({ nome: "João" }, { $set: { idade: 26 } });
db.usuarios.findOneAndDelete({ nome: "João" });
```

## 🔹 Realizando Update

```javascript
db.usuarios.updateOne(
  { nome: "João" },
  { $set: { idade: 26 } }
);

db.usuarios.updateMany(
  { cidade: "São Paulo" },
  { $set: { estado: "SP" } }
);

db.usuarios.replaceOne(
  { nome: "João" },
  {
    nome: "John",
    idade: 27,
    cidade: "São Paulo",
    estado: "SP",
    endereco: {
      rua: "Avenida Principal",
      numero: 123
    }
  }
);
```

### Update Operadores

```javascript
// Usando o operador $set para definir o valor de um campo específico
db.usuarios.updateOne({ nome: "João" }, { $set: { idade: 26 } });

// Usando o operador $inc para incrementar o valor de um campo numérico
db.usuarios.updateOne({ nome: "João" }, { $inc: { idade: 1 } });

// Usando o operador $rename para renomear um campo existente
db.usuarios.updateOne({ nome: "João" }, { $rename: { "endereco.rua": "endereco.nomeRua" } });

// Usando o operador $unset para remover um campo específico de um documento
db.usuarios.updateOne({ nome: "João" }, { $unset: { endereco: "" } });
```

## 🔹 Realizando Delete

```javascript
// Usando o método deleteOne() para excluir o primeiro documento que corresponde ao filtro especificado
db.usuarios.deleteOne({ nome: "João" });

// Usando o método deleteMany() para excluir todos os documentos que correspondem ao filtro especificado
db.usuarios.deleteMany({ cidade: "São Paulo" });
```

## 🔹 Operadores Lógicos

```javascript
db.usuarios.find({ $and: [{ idade: { $gte: 18 } }, { cidade: "São Paulo" }] });

db.usuarios.find({ $or: [{ idade: { $lt: 18 } }, { cidade: "Rio de Janeiro" }] });

db.usuarios.find({ idade: { $not: { $eq: 25 } } });
```

## 🔹 Operadores de Comparação

```javascript
db.usuarios.find({ idade: { $eq: 25 } });

db.usuarios.find({ idade: { $ne: 30 } });

db.usuarios.find({ idade: { $gt: 30 } });

db.usuarios.find({ idade: { $gte: 30 } });

db.usuarios.find({ idade: { $lt: 30 } });

db.usuarios.find({ idade: { $lte: 30 } });

db.usuarios.find({ cidade: { $in: ["São Paulo", "Rio de Janeiro"] } });

db.usuarios.find({ cidade: { $nin: ["São Paulo", "Rio de Janeiro"] } });
```

## 🔹 Projeção

```javascript
db.usuarios.find({}, { nome: 1, idade: 1 })
```

## 🔹 Ordenação

```javascript
db.usuarios.find().sort({ idade: 1 })
```

## 🔹 Limitação

```javascript
db.usuarios.find().limit(10)
```

## 🔹 Paginação

```javascript
db.usuarios.find().skip(10).limit(5)
```

---

# 🧠 Boas Práticas

- Utilizar `insertMany` para inserir múltiplos documentos de uma só vez, reduzindo chamadas ao banco
- Utilizar `pretty()` no shell para melhor legibilidade dos resultados
- Especificar filtros precisos em operações de update e delete para evitar modificações indesejadas
- Utilizar operadores como `$set` ao invés de substituir o documento inteiro quando apenas alguns campos precisam ser atualizados
- Utilizar projeção para retornar apenas os campos necessários, reduzindo tráfego de rede
- Combinar `skip()` e `limit()` para implementar paginação eficiente
- Utilizar `findOne` quando apenas um documento é esperado como resultado

---

# ⚠️ Pontos de Atenção

- O database só aparece na lista após ter pelo menos uma collection criada
- `insertOne` e `insertMany` não funcionam se a collection não existir (ela é criada automaticamente)
- `findOneAndUpdate` e `findOneAndDelete` retornam o documento original por padrão
- `replaceOne` substitui o documento inteiro, não apenas campos específicos
- `deleteMany` sem filtro remove TODOS os documentos da coleção
- O operador `$unset` remove o campo especificado do documento
- `skip()` pode ser ineficiente em grandes volumes de dados, pois precisa percorrer documentos ignorados

---

# 🧪 Exemplos Práticos

**Exemplo de consulta com múltiplos operadores de comparação:**

```javascript
// Usuários com idade entre 25 e 35 anos, exceto 30 anos
db.usuarios.find({
    idade: { $gte: 25, $lte: 35, $ne: 30 }
});
```

**Exemplo de atualização combinando múltiplos operadores:**

```javascript
// Incrementar idade em 1 e adicionar campo "atualizado_em" com a data atual
db.usuarios.updateMany(
    { cidade: "São Paulo" },
    { 
        $inc: { idade: 1 },
        $set: { atualizado_em: new Date() }
    }
);
```

**Exemplo de consulta com projeção e ordenação:**

```javascript
// Retornar apenas nome e idade, ordenado por idade decrescente
db.usuarios.find({}, { nome: 1, idade: 1, _id: 0 }).sort({ idade: -1 });
```

**Exemplo de exclusão condicional com $or:**

```javascript
// Excluir usuários de São Paulo OU com menos de 21 anos
db.usuarios.deleteMany({
    $or: [
        { cidade: "São Paulo" },
        { idade: { $lt: 21 } }
    ]
});
```

---

# 🚀 Conclusão

Este módulo apresentou as principais operações do MongoDB para manipulação de dados. Foram abordados a criação de databases e collections, inserção de documentos com `insertOne` e `insertMany`, consultas com `find` utilizando operadores lógicos e de comparação, atualizações com `updateOne`, `updateMany` e operadores como `$set`, `$inc`, `$rename` e `$unset`, exclusões com `deleteOne` e `deleteMany`, além de técnicas de projeção, ordenação, limitação e paginação. Essas operações formam a base para trabalhar com MongoDB em aplicações reais.

---

> [🏠 Voltar ao índice](../../../README.md) | [⬆ Módulo anterior: Introdução ao MongoDB](../1-Introducao-MongoDB/README.md) | [⬇ Próximo módulo: Fundamentos ETL](../../3-Fundamentos-ETL/README.md)