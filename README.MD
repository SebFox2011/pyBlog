# Projet Python de Blog

## Sujet Python TP Autonomie :
Création d'un blog simple en Python avec Flask. N'hésitez pas à mettre du joli CSS 😀

1. Créez une application Flask vide avec une simple route vers « / » qui affiche un template html simple.
initialisez les migrations à l'aide de la bibliothèque Flask-Migrate
2. Créez un objet « Post » avec un titre, un contenu et une date de création.
_(N'oubliez pas la migration ! )_
3. Créez les pages d'index (liste des posts), d'affichage (affichage en détail d'un post), de création, et de modification d'un Post.
4. Créez un objet « Comment » avec un contenu, une date de création et un nom (pour l'auteur) (et ne pas oublier l'id d'un post pour faire la liaison !)
_(N'oubliez pas la migration ! )_
5. Créez un espace en bas du détails d'un Post pour écrire un commentaire.
6. Listez les commentaires en bas du détail d'un Post


## Installation de l'environnement

Créer un projet Flask sous pyCharm

pip install Flask-SQLAlchemy

pip install Flask-Migrate

flask db init

flask db migrate

flask db upgrade

## Méthodologie,

Dans app, mettre les informations pour créer la bdd, créer ensuite les modèles de classes d'objet qui seront mis dans la bdd
Créer ensuite les routes dans le fichier app puis enfin les vues html

Créer ensuite les classes d'objets pour que populer la base de données

## pour redistribuer l'applicaiton

pip freeze > requirements.txt

permet d'envoyer au fichier texte les librairies dépendantes au projet.

## Configuration de blue_print
créer de nouveaux fichier, importer  Blueprint, redirect, render_template, request, url_for
db et la classe objet

Définir le préfix:
bp_comment = Blueprint('comments', __name__, url_prefix='/blog/comment')


## Appel des api

pip install requests,json

import json

response = response.get('api_url')
content = json.load(response.text)
return jsonify(content)

for item in content:
    Post.create(item)
return jsonify(content)
