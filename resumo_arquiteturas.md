# 0. Introdução

    - Data Warehouse, Data Lake e Data Mesh todos estes temas são na verdade tópicos de arquiteturas voltadas para Big Data e Engenharia de Dados. 
    Onde o Data Warehouse é de um repositório unificado para armazenar grandes quantidades de informações de várias fontes dentro de uma organização. 
    Data Lake também trata-se de um repositório de armazenamento centralizado sendo que é altamente flexivel, por armazenar dados brutos em uma quantidade muito grande que podem ser estruturados ou não. 
    Agora com Data Mesh os dados são descentralizados, onde funciona de uma forma totalmente oposta ao Data Lake e o Data Warehouse.
    A seguir, iremos explicar detalhadamente cada tópico.

# 1. Data Warehouse (Armazém de Dados)

    - Como haviamos falado, o Data Warehouse é um repositório de dados unificado para armazenar grandes quantidades de informações de várias fontes dentro de uma organização que podem ser analisados para obter uma melhor tomada de decição. A palavra chave é "Grandes quantidades de várias fontes". Ele reúne dados de diferentes fontes heterogêneas, os organiza e os torna acessíveis para consultas e relatórios avançados. A principal função de um Data Wareh é oferecer suporte ao processo de tomada de decisão estratégica.

    - Ajudam na melhora da tomada de decisão pois reunem dados de todas as fontes em um único lugar elimina
    inconsistências, garantindo informações confiáveis. Também é possivel identificar padrões históricos e prever comportamentos futuros, como prever demanda ou identificar clientes potenciais.

    - Um conceito muito popular do Data Warehouse é o ETL (Extract, Transform, Load)
        - Extração: Os dados são coletados de diversas fontes.
        - Transformação: Dados são limpos, transformados e organizados.
        - Carregamento: Dados processados são inseridos no DW.

## 1.1 Características Principais
    
    - Orientação por Assunto
        - Os dados são organizados em torno de temas específicos (como vendas, clientes, produtos) e não das operações diárias da empresa.

    - Integrado
        - Dados de múltiplas fontes (sistemas transacionais, ERP, CRM, etc.) são integrados em um formato consistente e unificado.

    - Não Volátil
        - Os dados, uma vez armazenados, não são modificados ou excluídos. Novos dados são adicionados sem alterar os existentes.

    - Variável no Tempo
        - O DW armazena dados históricos, permitindo análises de longo prazo. Cada registro possui uma dimensão temporal.

## 1.2 Vantagens

    - Tomada de Decisão Baseada em Dados
        - Oferece dados históricos e consistentes para análises preditivas e relatórios detalhados.

    - Consolidação de Dados
        - Combina e unifica dados dispersos de diferentes departamentos e sistemas.

    - Desempenho
        - Otimizado para consultas complexas e análises multidimensionais.

    - Histórico de Dados
        - Mantém informações históricas que não estão disponíveis nos sistemas operacionais.

## 1.3 Desvantagens

    - Alto Custo
       - Requer investimentos significativos em hardware, software e manutenção.

    - Complexidade de Implementação
        - O processo de ETL e integração de dados pode ser desafiador e demorado.

    - Atualizações Não em Tempo Real
        - Geralmente, os dados são atualizados periodicamente, não em tempo real.

## 1.4 Casos de Uso

    - Análise de Vendas
        - Identificar tendências de compra, sazonalidade e segmentação de clientes.

    - Relatórios Financeiros
        - Consolidação de dados financeiros de várias subsidiárias ou sistemas.

    - Marketing
        - Campanhas segmentadas com base no comportamento do cliente.

    - Manufatura
        - Monitoramento e otimização de processos de produção.

# 2. Data Lake (Lago de Dados)

    - O Data Lake é um repositório centralizado que armazena todos os seus dados estruturados e não estruturados em qualquer escala.
    Isso o torna ideal para empresas que lidam com Big Data e precisam de uma abordagem mais flexível para coletar e analisar dados.

## 2.1 Características Principais

    - Armazenamento de Dados Brutos
        - Dados são armazenados em seu formato original, sem transformação ou limpeza imediata.

    - Alta Escalabilidade
        - Projetado para escalar horizontalmente, lidando com petabytes ou exabytes de dados.

    - Flexibilidade
        - Suporta diversos tipos de dados:
            - Estruturados (ex.: tabelas de banco de dados).
            - Semiestruturados (ex.: JSON, XML).
            - Não Estruturados (ex.: imagens, vídeos, documentos de texto).

    - Esquema na Leitura (Schema-on-Read)
        - O esquema dos dados é aplicado somente quando necessário para análise, permitindo maior agilidade no armazenamento inicial.

    - Acessível para Diferentes Tipos de Usuários
        - Cientistas de dados, analistas e desenvolvedores podem acessar dados em formatos diversos para atender a necessidades específicas.

## 2.2 Vantagens

    - Armazenamento Flexível e Econômico
        - Soluções baseadas em armazenamento distribuído (ex.: S3) oferecem custo-benefício para volumes massivos de dados.

    - Sem Perda de Dados
        - Nenhuma informação é descartada, permitindo análises futuras, mesmo em dados inicialmente considerados irrelevantes.

    - Adaptação a Novas Necessidades
        - Esquema flexível permite a exploração de dados com diferentes abordagens analíticas ao longo do tempo.

    - Suporte a Big Data e IA
        - Capacidades robustas para análise de dados não estruturados, como aprendizado de máquina e mineração de dados.

## 2.3 Desvantagens

    - Risco de "Data Swamp"
        - Sem governança adequada, o Data Lake pode se transformar em um repositório caótico e ineficiente, onde dados não são encontrados ou compreendidos.

    - Complexidade de Gerenciamento
        - Requer ferramentas especializadas para gerenciar e localizar dados, além de profissionais qualificados.

    - Desempenho de Consulta
        - Consultas em dados brutos e não otimizados podem ser mais lentas em comparação a um Data Warehouse.

## 2.4 Casos de Uso

    - Big Data e Machine Learning
        - Processamento de grandes volumes de dados para criar modelos de aprendizado de máquina.

    - Análise de Dados Não Estruturados
        - Processamento de logs, imagens, vídeos ou dados de redes sociais.

    - IoT (Internet das Coisas)
        - Armazenamento e análise de dados contínuos de dispositivos conectados.

    - Exploração de Dados
        - Permite a descoberta de novos insights ao combinar dados de diversas fontes sem restrições de formato.

# 3. Data Mesh (Malha de dados)

    - Já o Data Mesh vai contra as arquiteturas tradicionais como Data Warehouse e Data Lake. O Data Mesh é uma abordagem descentralizada, Ela exige que as equipes de domínio assumam a responsabilidade por seus dados.
    De acordo com este princípio, os dados analíticos devem ser compostos em torno de domínios. Seguindo a arquitetura distribuída orientada por domínio, a propriedade de dados analítica e operacional é movida para as equipes de domínio, longe da equipe de dados central.

## 3.1 Características Principais

    - Dados como Produto
        - Cada conjunto de dados é tratado como um produto, com foco em qualidade, acessibilidade e usabilidade.
        
    - Descentralização Orientada por Domínios
        - Os dados são organizados e gerenciados pelos domínios que os produzem e consomem.

    - Plataforma de Dados Self-Service
        - Fornece ferramentas e infraestrutura padronizadas para que equipes gerenciem seus dados de maneira independente

## 3.2 Vantagens do Data Mesh

    - Escalabilidade Organizacional
        - Com a descentralização, as equipes podem escalar independentemente, sem sobrecarregar uma equipe central de dados.

    - Redução de Gargalos
        - Equipes podem acessar e consumir dados diretamente de seus proprietários, eliminando a dependência de intermediários.

    - Foco no Negócio
        - Cada domínio gerencia seus dados de acordo com suas necessidades de negócios, aumentando a relevância e o impacto das análises.

    - Qualidade de Dados
        - A responsabilidade pela qualidade dos dados é atribuída a quem os entende melhor: os domínios que os geram.

## 3.3 Desvantagens do Data Mesh
    
    - Complexidade Organizacional
        - A abordagem exige uma mudança cultural e estrutural significativa na organização.

    - Implementação Inicial Trabalhosa
        - Montar a infraestrutura para suportar um Data Mesh requer um investimento substancial em tempo, recursos e planejamento.
        
    - Requisitos Técnicos Elevados
        - A implementação do Data Mesh depende de ferramentas avançadas e de profissionais capacitados.

    - Governança Federada Desafiadora
        - A governança descentralizada pode levar a inconsistências e problemas de conformidade.

## 3.4 Casos de Uso

    - E-commerce
        - Domínios como "vendas", "estoque" e "marketing" gerenciam e compartilham seus próprios dados para análises independentes.

    - Setor Financeiro
        - Equipes descentralizadas, como "fraude", "riscos" e "compliance", gerenciam seus dados específicos.

    - Saúde
        - Cada departamento (ex.: oncologia, cardiologia) gerencia dados de pacientes em conformidade com regulações específicas.

# 4. Comparação, Diferenças e Quando usar cada um?

## 4.1 Objetivo

    - Data Warehouse: Gerar insights com dados estruturados e integrados para BI e relatórios.

    - Data Lake: Armazenar grandes volumes de dados brutos para análises exploratórias e avançadas.

    - Data Mesh: Gerenciar dados como produtos, com foco na descentralização e escalabilidade organizacional.

## 4.2 Estrutura de Dados

    - Data Warehouse: Estruturados (ex.: tabelas SQL).

    - Data Lake: Estruturados, semiestruturados e não estruturados (ex.: JSON, imagens, vídeos).

    - Data Mesh: Estruturados e semiestruturados, orientados ao domínio que os produz e consome.

## 4.3 Armazenamento

    - Data Warehouse: Centralizado, projetado para alta performance em consultas complexas.

    - Data Lake: Centralizado, escalável e otimizado para custo.

    - Data Mesh: Distribuído entre domínios, mas com suporte de infraestrutura self-service centralizada.

## 4.4 Performance de Consultas

    - Data Warehouse: Alta performance para consultas predefinidas e estruturadas.

    - Data Lake: Performance variável, especialmente para dados brutos e não otimizados.

    - Data Mesh: Alta performance depende da qualidade dos dados e da interoperabilidade definida por cada domínio.

## 4.4 Flexibilidade

    - Data Warehouse: Baixa: requer estrutura e transformação antes do uso.

    - Data Lake: Alta: armazena dados em estado bruto para múltiplos usos futuros.

    - Data Mesh: Alta: cada domínio adapta os dados às suas necessidades, mas segue padrões organizacionais básicos.

## 4.4 Escalabilidade

    - Data Warehouse: Limitada pela capacidade do sistema central.

    - Data Lake: Altamente escalável para grandes volumes de dados.

    - Data Mesh: Escalabilidade horizontal, gerenciada por domínios independentes.

## 4.5 Quando Usar Cada um?

    - Precisa de relatórios padronizados e dashboards? > Data Warehouse 

    - Lida com Big Data, análise de IA/ML ou dados não estruturados? > Data Lake

    - Organização com múltiplos domínios e necessidade de autonomia? > Data Mesh