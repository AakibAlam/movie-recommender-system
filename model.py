from os import path
import pandas as pd
from flask import Flask
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

movie_data = pd.read_csv('movies_data.csv')
movie_data.dropna(inplace=True)

# selected_features:    genres, keywords, overview, cast and director

combined_features = movie_data['genres']+movie_data['keywords']+movie_data['overview']+movie_data['cast']+movie_data['director']

vectorizer = TfidfVectorizer()
combined_features = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(combined_features)

def get_similarity_matrix():
    return similarity

def insert_into_db():
    from app import db
    for index, row in movie_data.iterrows():
        movie = {
            "id": index,
            "name": row['title'],
            "movie_id": row['movie_id'],
            "popularity": row['popularity'],
            "genre": row['genres'].split(' ')
        }
        db.movies.insert_one(movie)
        print(index)

    total_entries = db.movies.count_documents({})

    print(f'Total number of entries in the collection: {total_entries}')