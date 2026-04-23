# 📌 Projeto Prático: Infraestrutura Cloud AWS

Este projeto prático consiste na implementação de serviços AWS para a empresa Abstergo Industries, com foco na redução de custos operacionais e aumento da eficiência da infraestrutura de TI.

---

# 🎯 Objetivo do Projeto

Elencar 3 serviços AWS com a finalidade de realizar diminuição de custos imediatos na empresa Abstergo Industries, garantindo alta disponibilidade, escalabilidade e desempenho para seus sistemas críticos.

---

# 📋 Relatório de Implementação de Serviços AWS

**Data:** 23/04/2026

**Empresa:** Abstergo Industries

**Responsável:** Rodrigo da Silva Pereira

---

## Introdução

Este relatório apresenta o processo de implementação de ferramentas na empresa Abstergo Industries, realizado por Rodrigo da Silva Pereira. O objetivo do projeto foi elencar 3 serviços AWS, com a finalidade de realizar diminuição de custos imediatos.

---

## Descrição do Projeto

O projeto de implementação de ferramentas foi dividido em 3 etapas, cada uma com seus objetivos específicos. A seguir, serão descritas as etapas do projeto:

---

### Etapa 1: Amazon EC2 (Elastic Compute Cloud)

| Item | Descrição |
|------|-----------|
| **Ferramenta** | Amazon EC2 |
| **Foco principal** | Fornecer capacidade de computação escalável na nuvem, permitindo que a empresa execute suas aplicações e serviços de forma eficiente e flexível |
| **Caso de uso** | A farmacêutica trabalha com distribuição de medicamentos a nível nacional, possuindo diversas redes de distribuição, e precisa de uma infraestrutura de TI que possa se adaptar rapidamente às mudanças na demanda, garantindo alta disponibilidade e desempenho para seus sistemas críticos |
| **Solução** | Amazon EC2 oferece ampla variedade de tipos de instância, escalabilidade automática e integração com outros serviços AWS, permitindo otimização de recursos e redução de custos operacionais |

---

### Etapa 2: EC2 Auto Scaling

| Item | Descrição |
|------|-----------|
| **Ferramenta** | EC2 Auto Scaling |
| **Foco principal** | Garantir que a empresa tenha a quantidade certa de instâncias EC2 em execução para atender à demanda de tráfego, ajustando automaticamente a capacidade conforme necessário |
| **Caso de uso** | A farmacêutica pode enfrentar variações significativas na demanda, especialmente durante períodos de alta demanda, como campanhas de vacinação ou surtos de doenças |
| **Solução** | EC2 Auto Scaling permite escalar a infraestrutura de TI de forma eficiente e econômica, ajustando automaticamente a capacidade para atender à demanda, garantindo alta disponibilidade e desempenho |

---

### Etapa 3: Elastic Load Balancing (ELB)

| Item | Descrição |
|------|-----------|
| **Ferramenta** | Elastic Load Balancing (ELB) |
| **Foco principal** | Distribuir automaticamente o tráfego de entrada de aplicações entre múltiplos destinos (instâncias EC2, contêineres, endereços IP) em uma ou mais zonas de disponibilidade (AZs), aumentando a disponibilidade e tolerância a falhas |
| **Caso de uso** | Utilizamos ferramentas como EC2 e Auto Scaling, porém é necessário um serviço para realizar a devida distribuição das demandas, garantindo alta disponibilidade e desempenho para sistemas críticos |
| **Solução** | Elastic Load Balancing (ELB) oferece escalabilidade automática, monitoramento de integridade dos destinos registrados e suporte a diferentes tipos de balanceadores de carga, permitindo otimização de recursos e redução de custos operacionais |

---

## Conclusão

A implementação de ferramentas na empresa Abstergo Industries tem como esperado:

- **Redução de custos operacionais** com o pagamento conforme uso (pay-as-you-go)
- **Aumento da eficiência** com escalabilidade automática
- **Alta disponibilidade** com distribuição de tráfego entre múltiplas AZs
- **Melhor desempenho** com ajuste automático de capacidade
- **Maior resiliência** com tolerância a falhas integrada

O que aumentará a eficiência e a produtividade da empresa. Recomenda-se a continuidade da utilização das ferramentas implementadas e a busca por novas tecnologias que possam melhorar ainda mais os processos da empresa.

---

## Anexos

### Documentação das ferramentas implementadas:

- [Amazon EC2](https://aws.amazon.com/ec2/)
- [EC2 Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/)

---

## Assinatura do Responsável pelo Projeto

**Rodrigo da Silva Pereira**

---

# 🏗️ Arquitetura Proposta

'''
                    ┌─────────────────────────────────────┐
                    │         USUÁRIOS (Internet)          │
                    └─────────────────┬───────────────────┘
                                      ↓
                    ┌─────────────────────────────────────┐
                    │      Elastic Load Balancing (ELB)    │
                    │         Distribui o tráfego          │
                    └─────────────────┬───────────────────┘
                                      ↓
        ┌─────────────────────────────┼─────────────────────────────┐
        ↓                             ↓                             ↓
┌───────────────┐             ┌───────────────┐             ┌───────────────┐
│  EC2 (AZ-a)   │             │  EC2 (AZ-b)   │             │  EC2 (AZ-c)   │
│   Instância   │             │   Instância   │             │   Instância   │
│    Ativa      │             │    Ativa      │             │    Ativa      │
└───────────────┘             └───────────────┘             └───────────────┘
        ↓                             ↓                             ↓
└─────────────────────────────┼─────────────────────────────┘
                              ↓
              ┌─────────────────────────────────────┐
              │        EC2 Auto Scaling Group        │
              │   Ajusta capacidade automaticamente  │
              │   (Mín: 2, Máx: 10, Desejado: 3)     │
              └─────────────────────────────────────┘
'''

---

# 🧠 Benefícios Esperados

| Serviço | Benefício de Custo |
|---------|-------------------|
| **Amazon EC2** | Pagamento apenas pelo tempo de uso, sem investimento inicial em hardware |
| **EC2 Auto Scaling** | Redução de custos em períodos de baixa demanda (diminui instâncias) |
| **Elastic Load Balancing** | Distribuição eficiente evita desperdício de recursos |

---

# 📊 Métricas de Sucesso

- Redução de **30-40%** nos custos de infraestrutura no primeiro trimestre
- Disponibilidade dos sistemas críticos mantida em **99,9%**
- Escala automática funcional com resposta em **menos de 5 minutos**
- Balanceamento de carga distribuindo tráfego entre **mínimo de 2 AZs**

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: AWS Armazenamento](../../5-Computacao-Nuvem/5-AWS-Armazenamento/README.md) | [⬇ Próximo módulo: Machine Learning](../../6-Machine_Learning/README.md)