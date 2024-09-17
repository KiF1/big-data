from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Configuração do MongoDB
app.config["MONGO_URI"] = "mongodb://root:example@localhost:27017/moviesdb?authSource=admin"
mongo = PyMongo(app)

# Rota inicial
@app.route('/')
def index():
    return "API de Sistema de Recomendação de Filmes"

# CRUD para Filmes
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = mongo.db.movies.find()
    result = []
    for movie in movies:
        result.append({
            'id': str(movie['_id']),
            'title': movie['title'],
            'genres': movie['genres']
        })
    return jsonify(result)

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    movie_id = mongo.db.movies.insert_one({
        'title': data['title'],
        'genres': data['genres']
    })
    return jsonify({'id': str(movie_id.inserted_id)})

@app.route('/movies/<id>', methods=['GET'])
def get_movie(id):
    movie = mongo.db.movies.find_one({'_id': ObjectId(id)})
    if movie:
        return jsonify({
            'id': str(movie['_id']),
            'title': movie['title'],
            'genres': movie['genres']
        })
    else:
        return jsonify({'error': 'Filme não encontrado'}), 404

@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    data = request.json
    mongo.db.movies.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'title': data['title'],
            'genres': data['genres']
        }}
    )
    return jsonify({'message': 'Filme atualizado com sucesso'})

@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    mongo.db.movies.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Filme excluído com sucesso'})

# CRUD para Usuários
@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    result = []
    for user in users:
        result.append({
            'id': str(user['_id']),
            'name': user['name'],
            'ratings': user['ratings']
        })
    return jsonify(result)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = mongo.db.users.insert_one({
        'name': data['name'],
        'ratings': data['ratings']
    })
    return jsonify({'id': str(user_id.inserted_id)})

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if user:
        return jsonify({
            'id': str(user['_id']),
            'name': user['name'],
            'ratings': user['ratings']
        })
    else:
        return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    mongo.db.users.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'name': data['name'],
            'ratings': data['ratings']
        }}
    )
    return jsonify({'message': 'Usuário atualizado com sucesso'})

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Usuário excluído com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
