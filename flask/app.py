from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import requests

app = Flask(__name__)

# Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['filmes_db']
usuarios_collection = db['usuarios']
filmes_collection = db['filmes']

# Chave da API TMDb
TMDB_API_KEY = '0f5152fe09bcb82401da522de7685815'

#Obter nome do gênero
def get_genres():
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=pt-BR'
    response = requests.get(url).json()
    return {genre['id']: genre['name'] for genre in response['genres']}

# Index
@app.route('/', methods=['GET', 'POST'])
def index():
    movie_data = None
    genres = get_genres()  # Obter os gêneros
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}&language=pt-BR'
        response = requests.get(url).json()
        
        if response['results']:
            movie_data = response['results'][0]  # Pega o primeiro resultado

    # Converte os IDs de gêneros para nomes
    if movie_data:
        genre_names = [genres[genre_id] for genre_id in movie_data['genre_ids'] if genre_id in genres]
        movie_data['genre_names'] = genre_names  # Adiciona os nomes dos gêneros aos dados do filme
    
    return render_template('index.html', movie_data=movie_data, genres=genres)

# ENDPOINT: Cadastrar um novo usuário
@app.route('/usuario', methods=['POST'])
def cadastrar_usuario():
    dados = request.json
    usuarios_collection.insert_one(dados)
    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201

# ENDPOINT: Registrar uma avaliação de filme
@app.route('/avaliacao', methods=['POST'])
def avaliar_filme():
    usuario_id = request.json['usuario_id']
    filme_id = request.json['filme_id']
    nota = request.json['nota']
    
    # Verificar se o filme já está no MongoDB
    filme = filmes_collection.find_one({"_id": filme_id})
    if not filme:
        # Buscar o filme da TMDb
        url = f'https://api.themoviedb.org/3/movie/{filme_id}?api_key={TMDB_API_KEY}&language=pt-BR'
        response = requests.get(url).json()
        filme = {
            "_id": filme_id,
            "titulo": response['title'],
            "genero": response['genres'],
            "ano": response['release_date']
        }
        filmes_collection.insert_one(filme)
    
    # ENDPOINT: Atualizar a avaliação do usuário
    usuarios_collection.update_one(
        {"_id": usuario_id},
        {"$push": {"avaliacoes": {"filme_id": filme_id, "nota": nota}}}
    )
    
    return jsonify({"message": "Avaliação registrada com sucesso!"}), 201

# Sugerir filmes (exemplo básico)
@app.route('/recomendacoes/<usuario_id>', methods=['GET'])
def recomendar_filmes(usuario_id):
    usuario = usuarios_collection.find_one({"_id": usuario_id})
    if not usuario:
        return jsonify({"message": "Usuário não encontrado"}), 404
    
    # Exemplo simples: recomendar filmes do mesmo gênero
    avaliacoes = usuario.get("avaliacoes", [])
    generos = []
    for avaliacao in avaliacoes:
        filme = filmes_collection.find_one({"_id": avaliacao['filme_id']})
        generos.extend(filme['genero'])
    
    # Buscar outros filmes do mesmo gênero
    recomendacoes = filmes_collection.find({"genero": {"$in": generos}}).limit(5)
    filmes_recomendados = [{"titulo": filme['titulo'], "ano": filme['ano']} for filme in recomendacoes]
    
    return jsonify(filmes_recomendados)

if __name__ == '__main__':
    app.run(debug=True)
