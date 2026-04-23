# 📌 Módulo: Computação na AWS

Este módulo aborda os principais serviços de computação da AWS, incluindo EC2, Auto Scaling, Elastic Load Balancing, serviços de mensageria, computação sem servidor e containers.

---

# 🎯 Objetivos do Módulo

Ao final deste módulo, você será capaz de:

- Compreender o serviço EC2 e os diferentes tipos de instâncias
- Implementar escalabilidade com EC2 Auto Scaling
- Distribuir tráfego com Elastic Load Balancing (ELB)
- Utilizar serviços de mensageria (SQS, SNS, MQ, Kinesis, Pinpoint)
- Entender os conceitos de computação sem servidor (Lambda, Fargate, EventBridge)
- Conhecer os serviços de containers na AWS (ECS e EKS)

---

# 📚 Conteúdos Abordados

## 🔹 Elastic Compute Cloud - EC2

O Amazon EC2 (Elastic Compute Cloud) é um serviço da AWS que permite criar e gerenciar servidores virtuais na nuvem de forma escalável e sob demanda.

O Amazon EC2 oferece capacidade computacional flexível, permitindo que você execute **instâncias**, que são máquinas virtuais configuráveis com diferentes quantidades de CPU, memória, armazenamento e rede, sem precisar investir em hardware físico. Cada instância pode ser personalizada de acordo com a necessidade do seu aplicativo, escolhendo o sistema operacional, software adicional e tipo de instância, que define o equilíbrio entre recursos de computação, memória, armazenamento e rede.

### Tipos de Instância

| Tipo | Descrição |
|------|-----------|
| **Uso geral** | Configuração padrão que visa o equilíbrio entre computação, memória e rede |
| **Otimizados para computação** | Uso geral melhorado, com processamento de melhor desempenho |
| **Otimizados para memória** | Projetado para alto desempenho com grandes quantidades de informações na memória |
| **Computação acelerada** | Usa aceleração de hardware e coprocessadores para executar funções de forma eficiente |
| **Otimizadas para armazenamento** | Ideais para carga de trabalho que exigem acesso de leitura e gravação com grande volume de dados |

## 🔹 EC2 Auto Scaling

O EC2 Auto Scaling provê escalabilidade horizontal para seus serviços, melhora a tolerância a falhas com identificação de instâncias indisponíveis e implantação multi-AZ, e oferece melhor gerenciamento de custos.

Configuramos o Auto Scaling com configurações básicas como (configuração mínima, máxima, etc.)

### Abordagens de Scaling

| Abordagem | Descrição |
|-----------|-----------|
| **Scaling Preditivo** | Utiliza machine learning para prever demanda futura e escalar antecipadamente |
| **Scaling Dinâmico** | Escala com base em métricas em tempo real (CPU, memória, etc.) |

É possível combinar as duas abordagens.

## 🔹 Elastic Load Balancing - ELB

O Elastic Load Balancing (ELB) é um serviço da AWS que distribui automaticamente o tráfego de entrada de aplicações entre múltiplos destinos, como instâncias EC2, contêineres e endereços IP, em uma ou mais zonas de disponibilidade (AZs). Ele monitora a integridade dos destinos registrados e direciona o tráfego apenas para aqueles que estão saudáveis.

### Benefícios do ELB

- Aumenta a disponibilidade e a tolerância a falhas das aplicações
- Permite que cargas de trabalho sejam distribuídas entre vários recursos computacionais
- Oferece escalabilidade automática
- Descarrega tarefas de criptografia e descriptografia

### Tipos de Balanceadores de Carga

| Tipo | Descrição |
|------|-----------|
| **Application Load Balancer (ALB)** | Ideal para aplicações baseadas em HTTP/HTTPS, com roteamento avançado e integração com contêineres |
| **Network Load Balancer (NLB)** | Projetado para cargas de trabalho que exigem baixa latência e alta performance |
| **Gateway Load Balancer (GLB)** | Facilita a implantação de dispositivos de rede de terceiros |
| **Classic Load Balancer (CLB)** | Geração anterior, recomendada apenas para migração de sistemas legados |

## 🔹 Serviços de Mensageria

A mensageria na AWS oferece serviços robustos para comunicação entre sistemas, permitindo o envio e recebimento de mensagens de forma confiável e escalável. Esses serviços são amplamente utilizados em arquiteturas modernas, como microsserviços, sistemas distribuídos e aplicações serverless.

### Principais Serviços de Mensageria

| Serviço | Descrição | Exemplo de Uso |
|---------|-----------|----------------|
| **Amazon SQS** | Serviço de filas gerenciado para comunicação assíncrona (Standard ou FIFO) | Comunicação entre microsserviços |
| **Amazon SNS** | Serviço de publicação/assinatura para notificações a múltiplos endpoints | Notificações push para dispositivos móveis |
| **Amazon MQ** | Serviço gerenciado para agentes de mensagens (compatível com ActiveMQ) | Integração de sistemas híbridos |
| **Amazon Kinesis** | Processamento de dados em tempo real | Análise de logs em tempo real |
| **Amazon Pinpoint** | Plataforma de engajamento multicanal | Campanhas de marketing direcionadas |

### Benefícios da Mensageria na AWS

Os serviços de mensageria da AWS oferecem alta disponibilidade, escalabilidade automática e resiliência. Eles permitem desacoplar sistemas, reduzir dependências e melhorar a confiabilidade das aplicações.

## 🔹 Computação Sem Servidor (Serverless)

Crie e execute aplicações sem se preocupar com servidores.

### Visão Geral

A AWS oferece tecnologias para executar código, gerenciar dados e integrar aplicações, tudo isso sem a necessidade de gerenciar servidores. As tecnologias sem servidores contam com escalabilidade automática, alta disponibilidade integrada e um modelo de faturamento pago por utilização para aumentar a agilidade e otimizar os custos.

### Benefícios da Tecnologia Serverless

- Avance da ideia para o mercado com mais rapidez
- Diminua os custos
- Adaptação em escala
- Crie melhores aplicações, com mais facilidade

### Serviços Serverless na AWS

#### Computação

| Serviço | Descrição |
|---------|-----------|
| **AWS Lambda** | Serviço computacional orientado por eventos que permite executar código sem provisionar servidores |
| **AWS Fargate** | Mecanismo de computação serverless para ECS e EKS |

#### Integração de Aplicações

| Serviço | Descrição |
|---------|-----------|
| **Amazon EventBridge** | Barramento de eventos serverless para desenvolvimento de aplicações orientadas a eventos |

## 🔹 Containers em AWS

Os serviços de contêineres da AWS oferecem orquestração totalmente gerenciada, permitindo que as equipes se concentrem na inovação e gerem valor comercial rapidamente.

| Serviço | Descrição |
|---------|-----------|
| **Amazon ECS** | Serviço nativo da AWS para executar, gerenciar e escalar aplicações em contêineres |
| **Amazon EKS** | Permite a implementação de Kubernetes na AWS, oferecendo maneira robusta de gerenciar contêineres |

### Benefícios dos Containers na AWS

- Aplicações podem ser escaladas rapidamente
- Melhoram a segurança com patches e atualizações automatizadas
- Oferecem isolamento granular
- Reduzem custos operacionais
- Aumentam a eficiência

---

# 🧠 Boas Práticas

- Execute instâncias EC2 em pelo menos duas Zonas de Disponibilidade
- Configure Auto Scaling para ajustar capacidade conforme demanda
- Utilize Application Load Balancer (ALB) para aplicações web
- Prefira serviços serverless (Lambda) para cargas de trabalho esporádicas
- Utilize SQS para desacoplar componentes da aplicação
- Combine SNS com SQS para arquiteturas de eventos distribuídas
- Considere Fargate para simplificar o gerenciamento de containers

---

# ⚠️ Pontos de Atenção

- Instâncias EC2 têm custo contínuo, mesmo sem uso (diferente de Lambda)
- Auto Scaling pode demorar alguns minutos para reagir a picos de demanda
- SQS FIFO tem throughput menor que SQS Standard (300 msg/segundo)
- Lambda tem limite de tempo de execução (15 minutos máximo)
- EKS tem custo adicional de plano de controle (diferente de ECS)
- Escolha o tipo de instância correto para evitar desperdício de recursos

---

# 🧪 Exemplos Práticos

**Exemplo de arquitetura com EC2, ALB e Auto Scaling:**

'''
Internet
    ↓
Application Load Balancer (ALB)
    ↓                    ↓
EC2 (AZ-a)           EC2 (AZ-b)
    ↓                    ↓
Auto Scaling Group (mín:2, máx:10)
'''

**Exemplo de arquitetura serverless com Lambda e SQS:**

'''
Fila SQS
    ↓
Lambda (processa mensagens)
    ↓
Banco de dados DynamoDB
'''

**Exemplo de comando AWS CLI para criar instância EC2:**

'''bash
aws ec2 run-instances \
    --image-id ami-0c55b159cbfafe1f0 \
    --instance-type t2.micro \
    --key-name MinhaChave \
    --security-group-ids sg-12345678 \
    --subnet-id subnet-12345678
'''

---

# 🚀 Conclusão

Este módulo apresentou os principais serviços de computação da AWS, incluindo EC2, Auto Scaling e Elastic Load Balancing para escalabilidade e alta disponibilidade, serviços de mensageria (SQS, SNS, MQ, Kinesis, Pinpoint) para arquiteturas desacopladas, computação serverless com Lambda e Fargate, e orquestração de containers com ECS e EKS. Esses conhecimentos são fundamentais para projetar aplicações modernas, escaláveis e resilientes na nuvem.

---

> [🏠 Voltar ao índice](../../README.md) | [⬆ Módulo anterior: AWS Infraestrutura](../2-AWS-Infraestrutura/README.md) | [⬇ Próximo módulo: AWS Redes](../4-AWS-Redes/README.md)