# 🎬 Sistema de Recomendação de Filmes

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
- **Motivo da Escolha**: Python foi escolhido por sua simplicidade e vasta gama de bibliotecas para ciência de dados. Além disso, bibliotecas como `pymongo` facilitam a integração com MongoDB, enquanto `pandas` e `scikit-learn` são ferramentas poderosas para processamento de dados e cálculos de similaridade.

### 3. **Flask (Opcional)**
- **Motivo da Escolha**: Flask pode ser utilizado para criar uma API simples para fornecer as recomendações em tempo real. Ele permite uma integração rápida e eficiente com o MongoDB e outras bibliotecas de Python, caso seja necessário expor as funcionalidades do sistema para uma aplicação web.

### 4. **Pandas e NumPy**
- **Motivo da Escolha**: Essas bibliotecas serão usadas para manipulação e análise dos dados. `Pandas` oferece uma interface eficiente para transformar e filtrar grandes volumes de dados, enquanto `NumPy` facilita operações matemáticas e cálculos de similaridade.

## 📂 Estrutura do Projeto

O projeto é estruturado de maneira a armazenar informações dos filmes e avaliações de usuários em coleções do MongoDB. A seguir, apresentamos um exemplo de como os dados são organizados:

### Coleção de Filmes
Armazena as informações básicas sobre os filmes, como título e gênero.
```json
{
  "_id": ObjectId(),
  "movie_id": "1",
  "title": "The Matrix",
  "genres": ["Action", "Sci-Fi"]
}
