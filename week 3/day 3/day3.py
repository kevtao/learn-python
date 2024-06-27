from flask import jsonify
from pymongo import MongoClient
import certifi
import os
from bson.objectid import ObjectId
from bson import json_util
import json

connection_string = os.environ['MongoConnection']
client = MongoClient(connection_string, tlsCAFile=certifi.where())
db = client.sample_mflix
collection = db.movies
    
def mongo2json(doc):
    jsonStr = json_util.dumps(doc)
    return json.loads(jsonStr)

def lambda_handler(event, context):
    path = event['path']
    http_method = event['httpMethod']
    
    if path == '/years' and http_method == 'GET':
        return unique_years()
    elif path.startswith('/movies/') and http_method == 'GET':
        if path.startswith('/movies/year/'):
            year = path.split('/')[-1]
            return get_movies(year)
        else:
            movie_id = path.split('/')[-1]
            return get_movie(movie_id)
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Not Found'})
        }



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

def unique_years():
    unique_years = collection.distinct("year")
    return unique_years

def get_movies(year):
    movies = list(collection.find({"year": year}))
    movies = [mongo2json(movie) for movie in movies]
    return jsonify(movies)