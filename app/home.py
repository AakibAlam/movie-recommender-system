import os
import pymongo
import requests
from flask import Blueprint, render_template, Blueprint, request

api_key = os.environ.get('TMDB_API_KEY')

home = Blueprint('home', __name__)

def recommended_movies_by_similarity(movie_name):
    from app import db
    from .model import get_similarity_matrix
    similarity = get_similarity_matrix()
    result = db.movies.find_one({'name': movie_name})
    index_of_the_movie = int(result['id'])
    similarity_score = similarity[index_of_the_movie]
    similarity_score = list(enumerate(similarity_score))
    similarity_score.sort(key = lambda x:x[1], reverse = True)
    recommended_movie_posters = []
    for [idx, similar_score] in similarity_score:
        res = db.movies.find_one({'id': idx})
        if not res:
            continue
        idx1 = int(res['id'])
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(res['movie_id'], api_key))
        data = response.json()
        if not data['poster_path']:
            continue
        recommended_movie_posters.append("https://image.tmdb.org/t/p/w500/" + data['poster_path'])
        if len(recommended_movie_posters)==12:
            break
    return recommended_movie_posters


def recommended_movies_by_genre(genre):
    from app import db
    recommended_movie_posters = []
    movies = db.movies.find(
        {'genre': {"$in": [genre]}},
        sort = [('popularity', pymongo.DESCENDING)]
        )
    for movie in movies:
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie['movie_id'], api_key))
        data = response.json()
        if not data['poster_path']:
            continue
        recommended_movie_posters.append("https://image.tmdb.org/t/p/w500/" + data['poster_path'])
        if len(recommended_movie_posters)==12:
            break
    return recommended_movie_posters


@home.route('/', methods=['GET', 'POST'])
def homepage():
    from app import db
    if request.method == 'POST' and len(request.form.get('movie_name')) > 0:
        movie_name = request.form.get('movie_name')
        movie = db.movies.find_one({'name': movie_name})
        if movie is not None:
            recommended_movie_posters = recommended_movies_by_similarity(movie_name)
            return render_template("result.html", title = "Movies related to "+ movie_name, movie_list = recommended_movie_posters)
        else:
            return render_template("error.html", name=movie_name)
    else:
        return render_template("home.html")


@home.route('/Adventure', methods=['GET'])
def Adventurepage():
    recommended_movie_posters = recommended_movies_by_genre("Adventure")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Adventure Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Adventure Movies")
    
@home.route('/Action', methods=['GET'])
def Actionpage():
    recommended_movie_posters = recommended_movies_by_genre("Action")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Action Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Action Movies")

 
@home.route('/Fantasy', methods=['GET'])
def Fantasypage():
    recommended_movie_posters = recommended_movies_by_genre("Fantasy")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Fantasy Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Fantasy Movies")

@home.route('/Science', methods=['GET'])
def Sciencepage():
    recommended_movie_posters = recommended_movies_by_genre("Science")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Science Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Science Movies")
    
@home.route('/Fiction', methods=['GET'])
def Fictionpage():
    recommended_movie_posters = recommended_movies_by_genre("Fiction")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Fiction Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Fiction Movies")
    
@home.route('/Crime', methods=['GET'])
def Crimepage():
    recommended_movie_posters = recommended_movies_by_genre("Crime")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Crime Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Crime Movies")
    
@home.route('/Drama', methods=['GET'])
def Dramapage():
    recommended_movie_posters = recommended_movies_by_genre("Drama")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Drama Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Drama Movies")
    
@home.route('/Thriller', methods=['GET'])
def Thrillerpage():
    recommended_movie_posters = recommended_movies_by_genre("Thriller")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Thriller Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Thriller Movies")
    
@home.route('/Animation', methods=['GET'])
def Animationpage():
    recommended_movie_posters = recommended_movies_by_genre("Animation")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Animation Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Animation Movies")

@home.route('/Family', methods=['GET'])
def Familypage():
    recommended_movie_posters = recommended_movies_by_genre("Family")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Family Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Family Movies")
    
@home.route('/Western', methods=['GET'])
def Westernpage():
    recommended_movie_posters = recommended_movies_by_genre("Western")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Western Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Western Movies")

@home.route('/Romance', methods=['GET'])
def Romancepage():
    recommended_movie_posters = recommended_movies_by_genre("Romance")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Romance Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Romance Movies")

@home.route('/Horror', methods=['GET'])
def Horrorpage():
    recommended_movie_posters = recommended_movies_by_genre("Horror")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Horror Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Horror Movies")

@home.route('/Mystery', methods=['GET'])
def Mysterypage():
    recommended_movie_posters = recommended_movies_by_genre("Mystery")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Mystery Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Mystery Movies")

@home.route('/History', methods=['GET'])
def Historypage():
    recommended_movie_posters = recommended_movies_by_genre("History")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="History Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="History Movies")

@home.route('/War', methods=['GET'])
def Warpage():
    recommended_movie_posters = recommended_movies_by_genre("War")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="War Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="War Movies")

@home.route('/Music', methods=['GET'])
def Musicpage():
    recommended_movie_posters = recommended_movies_by_genre("Music")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Music Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Music Movies")

@home.route('/Documentary', methods=['GET'])
def Documentarypage():
    recommended_movie_posters = recommended_movies_by_genre("Documentary")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Documentary Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Documentary Movies")

@home.route('/Foreign', methods=['GET'])
def Foreignpage():
    recommended_movie_posters = recommended_movies_by_genre("Foreign")
    if len(recommended_movie_posters) > 0:
        return render_template("result.html", title="Foreign Movies", movie_list = recommended_movie_posters)
    else:
        return render_template("error.html", title="Foreign Movies")