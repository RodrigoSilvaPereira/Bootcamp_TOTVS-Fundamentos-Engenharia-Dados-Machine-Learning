# 📌 Módulo: Redes na AWS

Este módulo aborda os principais conceitos de redes na AWS, incluindo Amazon VPC, sub-redes, gateways, ACLs e grupos de segurança.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Compreender o conceito de Amazon VPC e suas características
- Diferenciar sub-redes públicas e privadas
- Entender as opções de conectividade com a AWS
- Configurar Network ACLs para controle de tráfego
- Configurar Security Groups como camada adicional de segurança

---

# 📚 Conteúdos Abordados

## 🔹 Amazon VPC (Virtual Private Cloud)

A Amazon Virtual Private Cloud (VPC) é um serviço da AWS que permite criar uma **rede virtual isolada** dentro da infraestrutura da AWS. Isso significa que você pode iniciar recursos da AWS, como instâncias EC2, em uma rede virtual que você define, semelhante a uma rede tradicional em seu data center.

### Principais Características do Amazon VPC

| Característica | Descrição |
|----------------|-----------|
| **Controle total sobre a rede** | Você pode definir o intervalo de endereços IP, configurar sub-redes e roteamento |
| **Segurança e isolamento** | Oferece camadas de segurança, permitindo controlar o tráfego de rede entre instâncias e serviços |
| **Flexibilidade** | Você pode criar sub-redes públicas e privadas, além de usar gateways de Internet e VPNs para conectar seu VPC à internet ou a redes corporativas |

## 🔹 Conectividade com AWS

Podemos aplicar o conceito de VPC e Gateway Privado Virtual em sub-redes na AWS para tornar o serviço apenas privado, ou podemos aplicar o AWS Direct Connect.

| Opção | Descrição |
|-------|-----------|
| **Gateway Privado Virtual (VPN)** | Conexão criptografada pela internet entre a rede on-premise e a VPC |
| **AWS Direct Connect** | Conexão dedicada e privada entre o data center local e a AWS (mais performática e estável) |

## 🔹 Sub-redes e Listas de Controle de Acesso

Os dados trafegam em uma VPC através dos **Gateways de Internet**. A VPC possui Network ACLs (Access Control Lists) para controlar as requisições que estão chegando no seu serviço.

### Network ACLs

| Característica | Descrição |
|----------------|-----------|
| **Função** | Controla tráfego de entrada e saída de sub-redes |
| **Comportamento** | **Stateless** (não mantém estado da conexão) |
| **Regra padrão** | Por padrão, permite todo tráfego de entrada e saída |
| **Escopo** | Aplica-se a toda a sub-rede |

### Security Groups

Os Security Groups podem ser aplicados diretamente nos serviços (como instâncias EC2), promovendo uma camada adicional de segurança.

| Característica | Descrição |
|----------------|-----------|
| **Função** | Controla tráfego de entrada e saída no nível da instância |
| **Comportamento** | **Stateful** (mantém estado da conexão) |
| **Regra padrão** | Por padrão, nega todo o tráfego de entrada e permite todo o tráfego de saída |
| **Escopo** | Aplica-se a cada instância individualmente |

### Diferença entre Stateless e Stateful

| Aspecto | Stateless (Network ACL) | Stateful (Security Group) |
|---------|------------------------|---------------------------|
| **Memória de conexão** | Não lembra da conexão anterior | Remember the connection |
| **Tráfego de resposta** | Precisa de regra explícita de saída | Permite automaticamente |
| **Regras** | Separadas para entrada e saída | Única regra para ambos os sentidos |

---

# 🧠 Boas Práticas

- Utilize sub-redes públicas para recursos que precisam de acesso à internet (ex: load balancers)
- Utilize sub-redes privadas para bancos de dados e aplicações internas
- Configure Security Groups com o princípio de menor privilégio (permitir apenas o necessário)
- Prefira Security Groups para regras no nível da instância e Network ACLs para regras no nível da sub-rede
- Utilize AWS Direct Connect para workloads que exigem alta performance e baixa latência
- Documente as regras de entrada e saída da sua VPC

---

# ⚠️ Pontos de Atenção

- Network ACLs são stateless - lembre-se de configurar regras de entrada E saída
- Security Groups são stateful - regras de entrada automaticamente permitem resposta
- Por padrão, Security Groups negam todo o tráfego de entrada
- Por padrão, Network ACLs permitem todo o tráfego
- VPCs são regionais - não se estendem entre regiões diferentes
- O AWS Direct Connect tem custo mais elevado que VPN

---

# 🧪 Exemplos Práticos

**Exemplo de arquitetura VPC com sub-redes:**

'''
Internet
    ↓
Internet Gateway
    ↓
VPC (10.0.0.0/16)
├── Sub-rede Pública (10.0.1.0/24)
│   └── Load Balancer / NAT Gateway
└── Sub-rede Privada (10.0.2.0/24)
    └── Banco de Dados / Aplicação
'''

**Exemplo de regra de Security Group (Stateful):**

| Tipo | Protocolo | Porta | Origem | Descrição |
|------|-----------|-------|--------|-----------|
| Entrada | TCP | 22 | 0.0.0.0/0 | SSH |
| Entrada | TCP | 80 | 0.0.0.0/0 | HTTP |
| Entrada | TCP | 443 | 0.0.0.0/0 | HTTPS |
| Saída | Todos | Todas | 0.0.0.0/0 | Saída livre |

**Exemplo de regra de Network ACL (Stateless):**

| Regra | Tipo | Protocolo | Porta | Origem/Destino | Ação |
|-------|------|-----------|-------|----------------|------|
| 100 | Entrada | TCP | 80 | 0.0.0.0/0 | PERMITIR |
| 110 | Saída | TCP | 32768-65535 | 0.0.0.0/0 | PERMITIR |

---

# 🚀 Conclusão

Este módulo apresentou os principais conceitos de redes na AWS, com foco no Amazon VPC para criação de redes virtuais isoladas, opções de conectividade (VPN e Direct Connect), sub-redes públicas e privadas, além de Network ACLs (stateless) e Security Groups (stateful) para controle de tráfego e segurança. Esses conhecimentos são fundamentais para projetar arquiteturas seguras e bem estruturadas na AWS.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: AWS Computação](../3-AWS-Computacao/README.md) | [⬇ Próximo módulo: AWS Armazenamento](../5-AWS-Armazenamento/README.md)