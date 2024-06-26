from flask import Flask, request, jsonify
from pymongo import MongoClient
import certifi
import os
from bson.objectid import ObjectId
from flask_cors import CORS
from bson import json_util
import json

connection_string = os.environ['MongoConnection']
client = MongoClient(connection_string, tlsCAFile=certifi.where())
db = client.sample_mflix
collection = db.movies
app = Flask(__name__)
CORS(app)


def _unused():
    e_indata = collection.find({"year": {"$type": "string"}})
    for doc in e_indata:
        replaced = doc['year'].replace('è', '')
        collection.update_one({"_id": doc["_id"]}, {
                              "$set": {"year": int(replaced)}})


def mongo2json(doc):
    jsonStr = json_util.dumps(doc)
    return json.loads(jsonStr)


@app.route('/movies', methods=['POST'])
# POST: Create a new movie
def create_movie():
    data = request.json
    if not isinstance(data, dict):
        return jsonify({'error': 'Invalid input'}), 400
    result = collection.insert_one(data)
    data['_id'] = str(result.inserted_id)
    return jsonify(data), 201


@app.route('/movies/year/<int:year>', methods=['GET'])
# GET: Retrieve all movies
def get_movies(year):
    movies = list(collection.find({"year": year}))
    movies = [mongo2json(movie) for movie in movies]
    return jsonify(movies)


@app.route('/movies/<string:movie_id>', methods=['GET'])
# GET: Retrieve a single movie by id
def get_movie(movie_id):
    movies = list(collection.aggregate(pipeline=[
        {
            "$match": {
                "_id": ObjectId(movie_id)
            }
        },
        {
            "$lookup": {
                "from": "comments",
                "localField": "_id",
                "foreignField": "movie_id",
                "as": "comments"
            }
        },
    ]))
    if len(movies) == 0:
        return jsonify({'error': 'movie not found'}), 404
    return jsonify(mongo2json(movies[0]))


@app.route('/movies/<string:movie_id>', methods=['PUT'])
# UPDATE: Update an movie by id
def update_movie(movie_id):
    data = request.json
    result = collection.update_one(
        {'_id': ObjectId(movie_id)},
        {'$set': data}
    )
    if result.matched_count == 0:
        return jsonify({'error': 'movie not found'}), 404
    movie = collection.find_one({'_id': ObjectId(movie_id)})
    return jsonify(mongo2json(movie))


@app.route('/movies/<string:movie_id>', methods=['DELETE'])
# DELETE: Delete an movie by id
def delete_movie(movie_id):
    result = collection.delete_one({'_id': ObjectId(movie_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'movie not found'}), 404
    return '', 204


@app.route('/years', methods=['GET'])
# GET: Retrieve all distinct years
def unique_years():
    unique_years = collection.distinct("year")
    return unique_years


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
