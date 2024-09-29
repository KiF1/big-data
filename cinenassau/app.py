from flask import Flask, request, render_template, jsonify, session, redirect, flash, url_for
from pymongo import MongoClient
import bson
import requests
from argon2 import PasswordHasher
from bson.objectid import ObjectId
from bson import ObjectId, errors


app = Flask(__name__)
argon = PasswordHasher()
app.secret_key = '0f5152fe09bcb82401da522de768581521212121212121'

# Conectar ao MongoDB
client = MongoClient('mongodb://root:example@localhost:27017/')
db = client['filmes_db']
usuarios_collection = db['usuarios']
filmes_collection = db['filmes']

# Chave da API TMDb
TMDB_API_KEY = '0f5152fe09bcb82401da522de7685815'

from flask import jsonify

@app.route('/minhas_avaliacoes_json')
def minhas_avaliacoes_json():
    if 'usuario_id' not in session:
        return jsonify({"error": "Usuário não autenticado"}), 401

    usuario_id = session['usuario_id']
    usuario = usuarios_collection.find_one({"_id": ObjectId(usuario_id)})

    if usuario is None:
        return jsonify({"error": "Usuário não encontrado"}), 404

    # Buscar as avaliações do usuário
    avaliacoes = usuario.get('avaliacoes', [])

    # Retornar as avaliações em formato JSON
    return jsonify(avaliacoes)



# Rota Dashboard
@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/login')  # Redireciona para a página de login se não estiver autenticado

    usuario_id = session['usuario_id']
    usuario = usuarios_collection.find_one({"_id": ObjectId(usuario_id)})

    if usuario is None:
        return redirect('/login')  # Redireciona se o usuário não for encontrado

    # Buscar as avaliações do usuário
    avaliacoes = usuario.get('avaliacoes', [])
    quantidade_filmes_avaliados = len(avaliacoes)
    GENRES_MAP = {
        "Ação": 28,
        "Aventura": 12,
        "Animação": 16,
        "Comédia": 35,
        "Crime": 80,
        "Documentário": 99,
        "Drama": 18,
        "Família": 10751,
        "Fantasia": 14,
        "História": 36,
        "Terror": 27,
        "Música": 10402,
        "Mistério": 9648,
        "Romance": 10749,
        "Ficção Científica": 878,
        "Filme para TV": 10770,
        "Suspense": 53,
        "Guerra": 10752,
        "Faroeste": 37,
    }

    # Buscar detalhes dos filmes avaliados
    filmes_avaliados = []
    generos_recomendados = set()
    for avaliacao in avaliacoes:
        filme_id = avaliacao['filme_id']
        try:
            filme = filmes_collection.find_one({"id": int(filme_id)})
            if filme:
                filme['nota'] = avaliacao['nota']  # Adiciona a nota ao filme
                filmes_avaliados.append(filme)
                generos_recomendados.update(filme['generos'])
        except Exception as e:
            print(f"Erro ao buscar filme com ID {filme_id}: {e}")
            continue  # Ignorar erros de busca

    # Mapeia os gêneros para os IDs correspondentes
    ids_recomendados = [GENRES_MAP[genero] for genero in generos_recomendados if genero in GENRES_MAP]

    # Buscar filmes recomendados com base nos gêneros avaliados
    filmes_recomendados = []
    for id_recomendado in ids_recomendados:
        filmes_recomendados.extend(get_filmes_por_genero(id_recomendado))

    # Remover duplicatas, mantendo os filmes únicos
    filmes_recomendados_unicos = []
    ids_recomendados = set()  # Conjunto para rastrear IDs únicos

    for filme in filmes_recomendados:
        if filme['id'] not in ids_recomendados:
            ids_recomendados.add(filme['id'])  # Adiciona o ID ao conjunto
            filmes_recomendados_unicos.append(filme)  # Adiciona o filme à nova lista
    
    filmes_recomendados = filmes_recomendados_unicos

    # Excluir filmes já avaliados da lista de recomendados
    filmes_recomendados = [filme for filme in filmes_recomendados if filme['id'] not in [f['id'] for f in filmes_avaliados]]


    return render_template('dashboard.html', usuario=usuario, quantidade_filmes_avaliados=quantidade_filmes_avaliados, filmes_avaliados=filmes_avaliados, filmes_recomendados=filmes_recomendados)


def get_filmes_por_genero(genero_id):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres={genero_id}&language=pt-BR'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Retornar apenas os primeiros 4 resultados
    return data['results'][:10]

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

# Rota Index/home page
@app.route('/', methods=['GET', 'POST'])
def index():
    movie_data = None
    genres = get_genres()  # Obter os gêneros
    error_message = None
    popular_movies = get_popular_movies()  # Buscar os filmes populares
    usuario = session.get('usuario_id')

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

    return render_template('index.html', movie_data=movie_data, usuario=usuario, genres=genres, error_message=error_message, popular_movies=popular_movies, enumerate=enumerate)

# Rota para exibir informacoes do carousel
@app.route('/filme/<int:filme_id>', methods=['GET'])
def detalhes_filme(filme_id):
    # Verifica se o filme já está no banco de dados
    movie_details = filmes_collection.find_one({"id": filme_id})

    if not movie_details:
        # Se o filme não estiver no banco, faça a consulta na API
        url = f'https://api.themoviedb.org/3/movie/{filme_id}?api_key={TMDB_API_KEY}&language=pt-BR'
        response = requests.get(url)
        data = response.json()

        # Verificar se o filme foi encontrado
        if 'status_code' in data and data['status_code'] == 34:
            return render_template('erro.html', mensagem="Filme não encontrado.")

        # Processar os dados para exibição
        movie_details = {
            'id': data['id'],  # Adiciona o ID do filme para identificação
            'titulo': data['title'],
            'resumo': data['overview'],
            'data_lancamento': data['release_date'],
            'generos': [genre['name'] for genre in data['genres']],
            'duracao': data['runtime'],
            'nota_media': data['vote_average'],
            'poster': data['poster_path'],
        }

        # Salvar os detalhes do filme no banco de dados
        filmes_collection.insert_one(movie_details)
    else:
        # Se o filme já está no banco, converte o ObjectId para um dicionário padrão
        movie_details = {k: movie_details[k] for k in movie_details if k != '_id'}

    return render_template('detalhes.html', movie=movie_details)


# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        usuario = usuarios_collection.find_one({"username": username})

        if usuario and argon.verify(usuario['password'], password):
            session['usuario_id'] = str(usuario['_id'])
            return redirect('/')
        else:
            flash('Nome de usuário ou senha inválidos', 'danger')

    return render_template('login.html')

# Rota de Logout
@app.route('/logout')
def logout():
    session.pop('usuario_id', None)  # Remove o ID do usuário da sessão
    return redirect('/')

# Rota de Registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(password) < 6:
            flash("A senha deve ter pelo menos 6 caracteres.")
            return redirect(url_for('register'))

        if usuarios_collection.find_one({"username": username}):
            flash("Nome de usuário já existe.")
            return redirect(url_for('register'))

        hashed_password = argon.hash(password.encode('utf-8'))
        usuarios_collection.insert_one({"username": username, "password": hashed_password})
        return redirect(url_for('login'))

    return render_template('register.html')

# Avaliar filme
@app.route('/avaliar/<filme_id>', methods=['POST'])
def avaliar_filme(filme_id):
    if 'usuario_id' not in session:
        return redirect('/login')  # Redireciona se o usuário não estiver logado
    
    usuario_id = session['usuario_id']
    nota = request.form['nota']
    
    # Salvar a avaliação no banco de dados
    usuarios_collection.update_one(
        {"_id": ObjectId(usuario_id)},
        {"$push": {"avaliacoes": {"filme_id": filme_id, "nota": nota}}}  # Filme ID é uma string, não ObjectId
    )
    
    return redirect(f'/filme/{filme_id}')  # Redireciona de volta para a página de detalhes do filme


#TESTE MOVIESDB /moviesdb para exibir os filmes no BD
@app.route('/moviesdb')
def moviesdb():
    # Buscar todos os filmes do banco de dados
    filmes = list(filmes_collection.find({}))

    # Converter ObjectId para string para evitar problemas no template
    for filme in filmes:
        filme['_id'] = str(filme['_id'])

    return render_template('moviesdb.html', filmes=filmes)


#TESTE /filmes para exibir o json
@app.route('/filmes', methods=['GET'])
def listar_filmes():
    # Buscar todos os filmes no banco de dados
    filmes = filmes_collection.find()  # Isso traz todos os documentos da coleção

    # Converter o cursor em uma lista
    filmes_lista = []
    for filme in filmes:
        # Convertemos o ObjectId para string para que ele seja serializável
        filme['_id'] = str(filme['_id'])
        filmes_lista.append(filme)

    return jsonify(filmes_lista)  # Retorna a lista de filmes como JSON


if __name__ == '__main__':
    app.run(debug=True)
