
import os
from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)


app.secret_key = os.environ["SECRET_KEY"]




@app.route('/')
def home():

    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.environ.get("TMDB_API_KEY"))
    print(os.environ.get("TMDB_API_KEY"))

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)


    return render_template("home.html", movies=dict["results"])

@app.route("/movies")
def get_movies_list():
    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.environ.get("TMDB_API_KEY"))

    response = urllib.request.urlopen(url)
    movies = response.read()
    dict = json.loads(movies)

    movies = []

    for movie in dict["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }
        
        movies.append(movie)

    return {"results": movies}

if __name__ == "__main__":
    app.env = "development" 
    app.run(debug=True)
