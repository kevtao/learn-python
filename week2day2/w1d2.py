from pymongo import MongoClient
import certifi
import os

connection_string = os.environ['MongoConnection']
client = MongoClient(connection_string, tlsCAFile=certifi.where())
db = client.sample_mflix
collection = db.movies
movie_comments = db.comments
def movietitles():
    query = {"year": 2008}
    movies_2008 = collection.find(query)
    for movie in movies_2008:
        print(movie)

# movietitles()
        
def moviecomments():
    query = {"year": 2008}
    movies_2008 = list(collection.find(query))
    movie = movies_2008[0]
    pipeline = [
        {
            "$match": {'_id': movie['_id']}
        },
        {
            "$lookup": {
                "from": "comments",
                "localField": "_id",
                "foreignField": "movie_id",
                "as": "movie_comments"
            }
        },
        {
            "$unwind": "$movie_comments"
        },
        {
            "$project": {
                "_id": 0,
                "title": 1,
                "movie_comments.name": 1,
                "movie_comments.text": 1
            }
        }
    ]
    results = list(collection.aggregate(pipeline))
    print(results)

# moviecomments()    
def create_movie():
    new_movie = {
        "plot": "Your movie plot description",
        "genres": ["comedy", "drama"],
        "runtime": 120,  # Runtime in minutes
        "cast": ["lan ba", "bob", "bobby"],
        "poster": "https://example.com/poster.jpg",
        "title": "Your Movie Title",
        "fullplot": "Full plot description of your movie",
        "languages": ["English"],
        "released": {
            "$date": "2024-01-01"  # Replace with release date in ISO format
        },
        "directors": ["bill", "joe"],
        "rated": "5",
        "awards": {
            "wins": 0,
            "nominations": 0,
            "text": "No awards yet"
        },
        "lastupdated": "2024-01-01 01:01:01.mmm000000",  # Replace with current date and time
        "year": 2024,  # Replace with release year
        "imdb": {
            "rating": 0.0,  # Replace with IMDb rating
            "votes": 0,     # Replace with number of IMDb votes
            "id": 0         # Replace with IMDb ID
        },
        "countries": ["USA", "UK"],
        "type": "movie",
        "tomatoes": {
            "viewer": {
                "rating": 3.0,
                "numReviews": 200,  
                "meter": 3          
            },
            "fresh": 20,             
            "critic": {
                "rating": 2.4,      
                "numReviews": 40,    
                "meter": 3          
            },
            "rotten": 240,           
            "lastUpdated": {
                "$date": "2024-01-01T01:01:01.000Z"  # Replace with last update date in ISO format
            }
        },
        "num_mflix_comments": 400
    }

    result = collection.insert_one(new_movie)
    print(result)

# create_movie()
    
def update_movie():
    query = {"title": "Your Movie Title"}
    update = {"$set": {"title": "lan lao ba"}}
    result = collection.update_one(query, update)
    print(result)

# update_movie()
    
def delete_movie():
    query = {"title": "lan lao ba"}
    result = collection.delete_one(query)
    print(result)

# delete_movie()