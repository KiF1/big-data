# 🎬 Sistema de Recomendação de Filmes - Execução e Teste das Rotas do CRUD
Para iniciar o aplicativo Flask, execute o seguinte comando:
````bash
python app.py
````

## 🚀 Teste das Rotas do CRUD

Exemplos de como testar as rotas utilizando **cURL** e **Postman**.

### 📚 Filmes

#### 1. **Obter todos os filmes**
   - **Descrição**: Retorna a lista de todos os filmes armazenados.
   - **Método HTTP**: `GET`
   - **Rota**: `/movies`
   - **Exemplo cURL**:
     ```bash
     curl -X GET http://localhost:5000/movies
     ```
   - **Exemplo de Resposta**:
     ```json
     [
       {
         "id": "614a1b5b48d7c5b5b49df784",
         "title": "The Matrix",
         "genres": ["Action", "Sci-Fi"]
       }
     ]
     ```

#### 2. **Adicionar um filme**
   - **Descrição**: Adiciona um novo filme ao banco de dados.
   - **Método HTTP**: `POST`
   - **Rota**: `/movies`
   - **Exemplo cURL**:
     ```bash
     curl -X POST http://localhost:5000/movies \
       -H "Content-Type: application/json" \
       -d '{"title": "The Matrix", "genres": ["Action", "Sci-Fi"]}'
     ```
   - **Exemplo de Resposta**:
     ```json
     {
       "id": "614a1b5b48d7c5b5b49df784"
     }
     ```

#### 3. **Obter um filme específico**
   - **Descrição**: Retorna as informações de um filme pelo seu ID.
   - **Método HTTP**: `GET`
   - **Rota**: `/movies/<id>`
   - **Exemplo cURL**:
     ```bash
     curl -X GET http://localhost:5000/movies/<id>
     ```
   - **Exemplo de Resposta**:
     ```json
     {
       "id": "614a1b5b48d7c5b5b49df784",
       "title": "The Matrix",
       "genres": ["Action", "Sci-Fi"]
     }
     ```

#### 4. **Atualizar um filme**
   - **Descrição**: Atualiza as informações de um filme pelo seu ID.
   - **Método HTTP**: `PUT`
   - **Rota**: `/movies/<id>`
   - **Exemplo cURL**:
     ```bash
     curl -X PUT http://localhost:5000/movies/<id> \
       -H "Content-Type: application/json" \
       -d '{"title": "The Matrix Reloaded", "genres": ["Action", "Sci-Fi"]}'
     ```
   - **Exemplo de Resposta**:
     ```json
     {
       "message": "Filme atualizado com sucesso"
     }
     ```

#### 5. **Excluir um filme**
   - **Descrição**: Exclui um filme pelo seu ID.
   - **Método HTTP**: `DELETE`
   - **Rota**: `/movies/<id>`
   - **Exemplo cURL**:
     ```bash
     curl -X DELETE http://localhost:5000/movies/<id>
     ```
   - **Exemplo de Resposta**:
     ```json
     {
       "message": "Filme excluído com sucesso"
     }
     ```

### 👥 Usuários

#### 1. **Obter todos os usuários**
   - **Descrição**: Retorna a lista de todos os usuários armazenados.
   - **Método HTTP**: `GET`
   - **Rota**: `/users`
   - **Exemplo cURL**:
     ```bash
     curl -X GET http://localhost:5000/users
     ```
   - **Exemplo de Resposta**:
     ```json
     [
       {
         "id": "614a1c2f48d7c5b5b49df785",
         "name": "John Doe",
         "ratings": []
       }
     ]
     ```

#### 2. **Adicionar um usuário**
   - **Descrição**: Adiciona um novo usuário ao banco de dados.
   - **Método HTTP**: `POST`
   - **Rota**: `/users`
   - **Exemplo cURL**:
     ```bash
     curl -X POST http://localhost:5000/users \
       -H "Content-Type: application/json" \
       -d '{"name": "John Doe", "ratings": []}'
     ```
   - **Exemplo de Resposta**:
     ```json
     {
       "id": "614a1c2f48d7c5b5b49df785"
     }
     ```

#### 3. **Obter um usuário específico**
   - **Descrição**: Retorna as informações de um usuário pelo seu ID.
   - **Método HTTP**: `GET`
   - **Rota**: `/users/<id>`
   - **Exemplo cURL**:
     ```bash
     curl -X GET http://localhost:5000/users/<id>
     ```
   - **Exemplo de Resposta**:
     ```json
     {
       "id": "614a1c2f48d7c5b5b49df785",
       "name": "John Doe",
       "ratings": []
     }
     ```

#### 4. **Atualizar um usuário**
   - **Descrição**: Atualiza as informações de um usuário pelo seu ID.
   - **Método HTTP**: `PUT`
   - **Rota**: `/users/<id>`
   - **Exemplo cURL**:
     ```bash
     curl -X PUT http://localhost:5000/users/<id> \
       -H "Content-Type: application/json" \
       -d '{"name": "Jane Doe", "ratings": []}'
     ```
   - **Exemplo de Resposta**:
     ```json
     {
       "message": "Usuário atualizado com sucesso"
     }
     ```

#### 5. **Excluir um usuário**
   - **Descrição**: Exclui um usuário pelo seu ID.
   - **Método HTTP**: `DELETE`
   - **Rota**: `/users/<id>`
   - **Exemplo cURL**:
     ```bash
     curl -X DELETE http://localhost:5000/users/<id>
     ```
   - **Exemplo de Resposta**:
     ```json
     {
       "message": "Usuário excluído com sucesso"
     }
     ```

---
