from flask import Flask, request, jsonify
from pymongo import MongoClient
import certifi
import os
from bson.objectid import ObjectId

connection_string = os.environ['MongoConnection']
client = MongoClient(connection_string, tlsCAFile=certifi.where())
db = client.sample_mflix
collection = db.movies

app = Flask(__name__)


def serialize_doc(doc):
    doc['_id'] = str(doc['_id'])
    return doc


@app.route('/items', methods=['POST'])
# POST: Create a new item
def create_item():
    data = request.json
    if not isinstance(data, dict):
        return jsonify({'error': 'Invalid input'}), 400
    result = collection.insert_one(data)
    data['_id'] = str(result.inserted_id)
    return jsonify(data), 201

@app.route('/items/year/<int:year>', methods=['GET'])
# GET: Retrieve all items
def get_items(year):
    movies = list(collection.find({"year": year}))
    movies = [serialize_doc(movie) for movie in movies]
    return jsonify(movies)


@app.route('/items/<string:item_id>', methods=['GET'])
# GET: Retrieve a single item by id
def get_item(item_id):
    movie = collection.find_one({"_id": ObjectId(item_id)})
    if movie is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(serialize_doc(movie))


@app.route('/items/<string:item_id>', methods=['PUT'])
# UPDATE: Update an item by id
def update_item(item_id):
    data = request.json
    result = collection.update_one(
        {'_id': ObjectId(item_id)},
        {'$set': data}
    )
    if result.matched_count == 0:
        return jsonify({'error': 'Item not found'}), 404
    item = collection.find_one({'_id': ObjectId(item_id)})
    return jsonify(serialize_doc(item))


@app.route('/items/<string:item_id>', methods=['DELETE'])
# DELETE: Delete an item by id
def delete_item(item_id):
    result = collection.delete_one({'_id': ObjectId(item_id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Item not found'}), 404
    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
