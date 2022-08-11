
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
    print(response)
    data = response.read()
    print(data)
    dict = json.loads(data)
    print(dict)


    weather = f"https://api.weatherapi.com/v1/forecast.json?key={os.environ['WEATHER_KEY']}&q=Chicago&days=1&aqi=no&alerts=no"

    weather_response = urllib.request.urlopen(weather)

    weather_data = weather_response.read()

    weather_dict = json.loads(weather_data)


    return render_template("home.html", movies=dict["results"], weather_info=weather_dict["results"])

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
