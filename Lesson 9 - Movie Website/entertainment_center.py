import config
import media
import fresh_tomatoes
import requests
import json

api_url = r'https://api.themoviedb.org/3/'
api_key = '?api_key=' + config.api_key

req = requests.get(api_url + 'list/47599' + api_key)

movies = req.json()

req.close()

movie_list = list()

for item in movies["items"]:
    req = requests.get(api_url + 'movie/' + str(item['id']) + '/videos' + api_key)
    videos = req.json()
    trailer = ''
    for video in videos['results']:
        if (video['type'] == 'Trailer' and video['site'] == "YouTube"):
            trailer = 'http://www.youtube.com/watch?v=' + video['key']
            break
    image = 'https://image.tmdb.org/t/p/w500' + item['poster_path']
    movie_list.append(media.Movie(item['title'], item['overview'], image, trailer))

    
fresh_tomatoes.open_movies_page(movie_list)
