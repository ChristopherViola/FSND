import config
import media
import requests
import json
from flask import Flask, render_template, url_for

app = Flask(__name__)

api_url = r'https://api.themoviedb.org/3/'
api_key = 'api_key=' + config.api_key

nav = [
	("/", "home", "Home"),
	("/populars/", "populars", "Populars")
]


@app.route("/")
def home():
	req = requests.get(api_url + 'list/47599?' + api_key)
	movies = req.json()
	req.close()
	movie_list = list()
	for item in movies["items"]:
	    req = requests.get(api_url + 'movie/' + str(item['id']) + '/videos?' + api_key)
	    videos = req.json()
	    trailer = ''
	    for video in videos['results']:
	        if (video['type'] == 'Trailer' and video['site'] == "YouTube"):
	            trailer = video['key']
	            break
	    image = 'https://image.tmdb.org/t/p/w500' + item['poster_path']
	    movie_list.append(media.Movie(item['title'], item['overview'], image, trailer))
	return render_template("media.html", navbar=nav, title='Home', active_page="home", medias=movie_list)

@app.route("/populars/")
def populars():
	req = requests.get(api_url + 'discover/movie?sort_by=popularity.desc&' + api_key)
	movies = req.json()
	req.close()
	movie_list = list()
	for item in movies["results"]:
	    req = requests.get(api_url + 'movie/' + str(item['id']) + '/videos?' + api_key)
	    videos = req.json()
	    trailer = ''
	    for video in videos['results']:
	        if (video['type'] == 'Trailer' and video['site'] == "YouTube"):
	            trailer = video['key']
	            break
	    image = 'https://image.tmdb.org/t/p/w500' + item['poster_path']
	    movie_list.append(media.Movie(item['title'], item['overview'], image, trailer))
	return render_template("media.html", navbar=nav, title='Populars', active_page="populars", medias=movie_list)
