# Projet 9 -   Développez une application Web en utilisant Django



## Introduction
Ce projet a pour but la création d'une application web permettant à des utilisateurs de demander ou de publier des critiques sur des livres ou des articles. 
Cette application utilise le framework **Django** ainsi qu'une base de donnée **sqlite3**.

## Installation
####  Cloner ce dépôt : 
```
git clone https://github.com/batshanti/Projet9.git
cd Projet9/
```
####  Créer un environnement virtuel pour le projet :
(Linux or Mac)
```
 python3 -m venv venv
 source venv/bin/activate
```
(Windows)
```
 python -m venv env
 env\Scripts\activate
```
#### Installer les packages :
```
pip install -r requirements.txt
```
#### Démarrer le serveur  :
````
python manage.py runserver
````
##  Lancement de l'application web
Se rendre sur un navigateur web et entrer l'url :
http://127.0.0.1:8000/

La base de donnée est déjà présente et possède plusieurs utilisateurs, demande de critique et avis.

#### Utilisateur de test : 
| Utilisateur | Mot de passse |
|--|--|
| tom | Password#1 |
| greg| Password#2 |
| lily| Password#3 |