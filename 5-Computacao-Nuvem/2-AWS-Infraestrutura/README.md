# 📌 Módulo: Infraestrutura da AWS

Este módulo aborda a infraestrutura global da AWS, incluindo Regiões, Zonas de Disponibilidade, Pontos de Presença e formas de provisionamento de recursos.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Compreender a infraestrutura global de datacenters da AWS
- Diferenciar Regiões, Zonas de Disponibilidade e Pontos de Presença
- Entender as vantagens de alta disponibilidade e tolerância a falhas
- Identificar as formas de interagir com os serviços da AWS
- Conhecer ferramentas de provisionamento como Elastic Beanstalk e CloudFormation

---

# 📚 Conteúdos Abordados

## 🔹 Infraestrutura da AWS

A AWS possui uma infraestrutura de datacenters em todo o mundo que fornece os diversos serviços que você pode utilizar. Esta infraestrutura é composta por Regiões e Zonas de Disponibilidade.

**Principais vantagens:**
- Alta disponibilidade
- Tolerância a falhas
- Baixa latência
- Isolamento de dados

## 🔹 Regiões

Regiões são locais onde são hospedados os data centers da AWS.

**Características:**
- Cada região possui locais isolados chamados Zonas de Disponibilidade
- Todas as regiões são conectadas com rede de alta velocidade
- Isolamento de dados entre regiões
- Regulação de dados local (conformidade com leis locais)
- Escolher região próxima aos usuários reduz latência

**Exemplos de Regiões AWS:**
| Nome da Região | Localização |
|----------------|-------------|
| us-east-1 | Norte da Virgínia, EUA |
| us-west-2 | Oregon, EUA |
| sa-east-1 | São Paulo, Brasil |
| eu-west-1 | Irlanda |
| ap-southeast-1 | Cingapura |

## 🔹 Zonas de Disponibilidade

Também chamadas de **AZs (Availability Zones)**.

São agrupamentos de datacenters isolados dentro de uma região.

**Características:**
- Rede, energia e conectividade redundantes
- Próximas o suficiente para manter baixa latência
- Longe o suficiente para evitar que um desastre afete mais de uma AZ

**Recomendação:** Execute suas aplicações pelo menos em duas Zonas de Disponibilidade para garantir alta disponibilidade.

**Exemplo de estrutura de uma Região:**
'''
Região: sa-east-1 (São Paulo)
├── Zona de Disponibilidade A (sa-east-1a)
├── Zona de Disponibilidade B (sa-east-1b)
└── Zona de Disponibilidade C (sa-east-1c)
'''

## 🔹 Pontos de Presença

Também chamados de **Edge Locations** (Locais de Borda ou Redes de Borda).

Funcionam como pontos específicos pelo globo para distribuir conteúdo de forma rápida.

**Exemplos de serviços que utilizam Pontos de Presença:**
- **Route 53:** Serviço de DNS
- **CloudFront:** CDN (Content Delivery Network)

### Como funciona o CloudFront

O CloudFront cria um sistema de cache mais próximo do usuário, posicionando-se entre o servidor e o usuário final, diminuindo a distância percorrida pela requisição.

**Fluxo:**
'''
Usuário → Edge Location (cache) → Servidor Origem
                ↑                           ↓
            Resposta rápida            Atualização
'''

## 🔹 Provisionamento de Recursos na AWS

Formas de interagir com os serviços da AWS:

| Método | Descrição |
|--------|-----------|
| **Console de Gerenciamento** | Interface web para gerenciamento manual |
| **AWS CLI** | Linha de comando para automação e scripts |
| **AWS SDKs** | Bibliotecas para integrar aplicações com AWS (Python, Java, Node.js, etc.) |

## 🔹 Provisionando Infraestrutura

### Elastic Beanstalk

Serviço que configura uma infraestrutura via configurações locais. Você faz o upload do código e o Elastic Beanstalk cuida automaticamente do deployment, capacidade, balanceamento de carga e escalabilidade.

**Características:**
- Abstração da infraestrutura subjacente
- Foco no código, não na configuração
- Suporte a várias linguagens (Java, .NET, Python, Node.js, etc.)

### CloudFormation

Serviço que configura uma infraestrutura via arquivos JSON ou YAML, aplicando o conceito de **Infraestrutura como Código (Infrastructure as Code - IaC)**.

**Características:**
- Define toda a infraestrutura em arquivos de texto
- Versionamento da infraestrutura (Git)
- Provisionamento repetível e consistente
- Facilita a recuperação de desastres

**Exemplo de arquivo CloudFormation (YAML):**
'''yaml
Resources:
  MeuServidorEC2:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-0c55b159cbfafe1f0
      KeyName: minha-chave
'''

---

# 🧠 Boas Práticas

- Execute suas aplicações em pelo menos duas Zonas de Disponibilidade
- Escolha a região mais próxima dos seus usuários para reduzir latência
- Utilize CloudFront para distribuir conteúdo estático globalmente
- Prefira Infraestrutura como Código (CloudFormation) para ambientes reprodutíveis
- Utilize a AWS CLI para automatizar tarefas repetitivas
- Considere o Elastic Beanstalk para aplicações simples e deployment rápido

---

# ⚠️ Pontos de Atenção

- Nem todos os serviços estão disponíveis em todas as regiões
- Dados transferidos entre regiões têm custo adicional
- Regiões diferentes não compartilham recursos por padrão
- Edge Locations não são adequadas para processamento pesado (apenas cache e distribuição)
- O CloudFormation requer conhecimento de JSON/YAML
- O Elastic Beanstalk pode ter limitações para configurações muito específicas

---

# 🧪 Exemplos Práticos

**Exemplo de arquitetura multi-AZ:**

'''
Internet
    ↓
Load Balancer (distribui entre AZs)
    ↓                    ↓
AZ-a (EC2)           AZ-b (EC2)
    ↓                    ↓
Banco de Dados Multi-AZ (RDS)
'''

**Exemplo de comando AWS CLI para listar regiões:**

'''bash
aws ec2 describe-regions
'''

**Exemplo de comando AWS CLI para listar zonas de disponibilidade:**

'''bash
aws ec2 describe-availability-zones --region sa-east-1
'''

---

# 🚀 Conclusão

Este módulo apresentou a infraestrutura global da AWS, incluindo Regiões, Zonas de Disponibilidade e Pontos de Presença. Aprendemos sobre as vantagens de alta disponibilidade e tolerância a falhas, as formas de interagir com os serviços da AWS (Console, CLI e SDKs), e as ferramentas de provisionamento como Elastic Beanstalk e CloudFormation com conceito de Infraestrutura como Código. Esses conhecimentos são fundamentais para projetar arquiteturas robustas na nuvem.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: Cloud](../1-Cloud/README.md) | [⬇ Próximo módulo: AWS Computação](../3-AWS-Computacao/README.md)