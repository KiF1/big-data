from flask import Flask, request, render_template, redirect, url_for
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

# Obter Lista de filmes em alta
def get_popular_movies():
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=pt-BR'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['results']  # Retorna a lista de filmes populares

# Obter nome do gênero ao inves do ID
def get_genres():
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=pt-BR'
    response = requests.get(url).json()
    return {genre['id']: genre['name'] for genre in response['genres']} # Retorna a lista de gêneros

# Index/home page
@app.route('/', methods=['GET', 'POST'])
def index():
    movie_data = None
    genres = get_genres()  # Obter os gêneros
    error_message = None
    popular_movies = get_popular_movies()  # Buscar os filmes populares

    if request.method == 'POST':
        movie_name = request.form['movie_name']
        url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}&language=pt-BR'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data['results']:
                movie_data = data['results'][0]  # Pega o primeiro resultado
        
                # Converte os IDs de gêneros para nomes
                if movie_data:
                    genre_names = [genres[genre_id] for genre_id in movie_data['genre_ids'] if genre_id in genres]
                    movie_data['genre_names'] = genre_names  # Adiciona os nomes dos gêneros aos dados do filme
                    return redirect(url_for('detalhes_filme', filme_id=movie_data['id']))
            else:
                error_message = "Filme não encontrado. Tente novamente."
                return render_template('index.html', movie_data=None, genres=genres, error_message=error_message, popular_movies=popular_movies, enumerate=enumerate), 404

        except requests.exceptions.RequestException as e:
            error_message = f"Ocorreu um erro ao acessar a API: {str(e)}. Tente novamente mais tarde."
            return render_template('index.html', movie_data=None, genres=genres, error_message=error_message, popular_movies=popular_movies, enumerate=enumerate), 500

    return render_template('index.html', movie_data=movie_data, genres=genres, error_message=error_message, popular_movies=popular_movies, enumerate=enumerate)

# Rota para exibir informacoes do carousel
@app.route('/filme/<int:filme_id>', methods=['GET'])
def detalhes_filme(filme_id):
    url = f'https://api.themoviedb.org/3/movie/{filme_id}?api_key={TMDB_API_KEY}&language=pt-BR'
    response = requests.get(url)
    data = response.json()

    # Verificar se o filme foi encontrado
    if 'status_code' in data and data['status_code'] == 34:
        return render_template('erro.html', mensagem="Filme não encontrado.")

    # Processar os dados para exibição
    movie_details = {
        'titulo': data['title'],
        'resumo': data['overview'],
        'data_lancamento': data['release_date'],
        'generos': [genre['name'] for genre in data['genres']],
        'duracao': data['runtime'],
        'nota_media': data['vote_average'],
        'poster': data['poster_path'],
    }

    return render_template('detalhes.html', movie=movie_details)

if __name__ == '__main__':
    app.run(debug=True)
