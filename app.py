from flask import Flask, render_template, request
import requests
import os
API_KEY = os.getenv("TMDB_API_KEY")
app = Flask(__name__)

API_KEY = "a9e0293e8cb50db4d70f9e8f03e2aa4c"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"

@app.route('/')
def home():
    url = f"{BASE_URL}/movie/popular?api_key={API_KEY}"
    response = requests.get(url)

    data = response.json()

    movies = []
    for movie in data.get('results', []):
        if movie.get('poster_path'):
            movies.append({
                "title": movie.get('title'),
                "image": IMAGE_URL + movie.get('poster_path')
            })

    return render_template("index.html", movies=movies)


@app.route('/search')
def search():
    query = request.args.get('q')
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}"

    response = requests.get(url)
    data = response.json()

    movies = []
    for movie in data.get('results', []):
        if movie.get('poster_path'):
            movies.append({
                "title": movie.get('title'),
                "image": IMAGE_URL + movie.get('poster_path')
            })

    return render_template("index.html", movies=movies)


@app.route('/health')
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
