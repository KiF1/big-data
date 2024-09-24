# 🎬 Cine Nassau

Este projeto desenvolve um **Sistema de Recomendação de Filmes** que utiliza as avaliações dos usuários para sugerir filmes com base em suas preferências. O projeto foi construído utilizando **MongoDB** como banco de dados NoSQL e **Python** para processamento e análise dos dados, aproveitando bibliotecas populares para a criação de sistemas de recomendação.

## 📝 Objetivo

O principal objetivo deste projeto é criar um sistema escalável que possa:
- Armazenar informações sobre filmes, usuários e suas avaliações de forma otimizada.
- Calcular a similaridade entre filmes ou entre usuários para gerar recomendações personalizadas.
- Oferecer uma interface para que os usuários recebam sugestões de filmes com base em seus gostos e comportamentos anteriores.

## 🔧 Tecnologias Utilizadas

### 1. **MongoDB**
- **Motivo da Escolha**: MongoDB foi escolhido por sua flexibilidade na modelagem de dados, sendo ideal para lidar com dados semi-estruturados, como avaliações de filmes e informações de usuários. MongoDB também oferece suporte para consultas complexas e agregações, essenciais para calcular a similaridade entre filmes e usuários.

### 2. **Python**
- **Motivo da Escolha**: Python foi escolhido por sua simplicidade e vasta gama de bibliotecas para ciência de dados. Além disso, bibliotecas como `pymongo` facilitam a integração com MongoDB, enquanto `pandas` é uma ferramenta poderosa para processamento de dados.

### 3. **Flask**
- **Motivo da Escolha**: Flask foi utilizado para criar uma API simples para fornecer as recomendações em tempo real. Ele permite uma integração rápida e eficiente com o MongoDB e outras bibliotecas de Python, caso seja necessário expor as funcionalidades do sistema para uma aplicação web.

## 📂 Estrutura do Projeto

O projeto é estruturado de maneira simples para facilitar o trabalho. A seguir, apresentamos um exemplo de como os arquivos são organizados:

### Estrutura de arquivos
Armazena informações sobre os usuários e suas avaliações dos filmes.
````shell
cinenassau/
│
├── app.py                  # Arquivo principal da aplicação Flask
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
├── templates/              # Diretório de templates HTML
│   ├── index.html          # Página inicial
│   ├── login.html          # Página de login
│   ├── register.html       # Página de registro
│   ├── detalhes.html       # Página de detalhes do filme
│   ├── dashboard.html      # Página de dashboard do usuário
│    
├── docker/
│   ├── docker-compose.yml  # Documentação do projeto 
│   ├── README.md           # Documentação do projeto
│
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
````

## 📊 Cálculo de Similaridade

## 🎯 Geração de Recomendações
