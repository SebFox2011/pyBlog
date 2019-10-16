from application import app
from flask import jsonify, redirect
import json
import requests
from models.post import Post

@app.route('/test_json')
def test_json():
    dic = {
        'type': 'Dictionnaire',
        'liste': [
            'un', 'deux', 'trois'
        ],
        'nombre': 12,
        'Booléen': True
    }
    return jsonify(dic)

@app.route('/test_requests')
def test_requests():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    content = json.loads(response.text)
    for item in content:
        Post.create(item)
    return redirect('https://google.fr')

@app.route('/unsplash')
def unsplash():
    response = requests.get('https://api.unsplash.com/photos/random?client_id=9838ead1b3ff626e5c216427d4d41cbef2344367ddc7cde9a1e04c13f2efbcb1')
    content = json.loads(response.text)
    url = content['links']['html']
    return redirect(url)

"""
1 : Récupérer le contenu de l'url : https://api.unsplash.com/photos/random?client_id=9838ead1b3ff626e5c216427d4d41cbef2344367ddc7cde9a1e04c13f2efbcb1
2 : Parser le résultat en JSON
3 : Récupérer l'url contenue dans links -> self
4 : rediriger vers cette url
"""
