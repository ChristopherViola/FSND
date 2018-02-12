import config
import media
import fresh_tomatoes
import requests
import json
from pprint import pprint

api_url = r'https://api.themoviedb.org/3/'
api_key = '?api_key=' + config.api_key

req = requests.get(api_url + 'list/47599' + api_key)
#json_mov = req.content
movies = req.json() #json.loads(json_mov)
#pprint(movies["items"][0])
req.close()

movie_list = list()

for item in movies["items"]:
    #pprint(item)

    req = requests.get(api_url + 'movie/' + str(item['id']) + '/videos' + api_key)
    #print api_url + 'movie/' + str(item['id']) + '/videos/' + api_key
    videos = req.json()
    #pprint(videos)
    trailer = ''
    for video in videos['results']:
        if (video['type'] == 'Trailer' and video['site'] == "YouTube"):
            #print 'video= http://www.youtube.com/watch?v=' + video['key'] 
            trailer = 'http://www.youtube.com/watch?v=' + video['key']
            break
    image = 'https://image.tmdb.org/t/p/w500' + item['poster_path']

    #print item['id'], item['title'], '\n', item['overview'], '\n', trailer
    #print image

    movie_list.append(media.Movie(item['title'], item['overview'], image, trailer))
    
fresh_tomatoes.open_movies_page(movie_list)
