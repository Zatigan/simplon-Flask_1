from flask import Flask
from flask import jsonify
from faker import Faker

# Création d'une instance Flask avec __name__ qui est un raccourci valide dans la plupart des cas
app = Flask(__name__)

# Création d'une instance Faker et configuration pour qu'il retourne des valeurs françaises
fake = Faker(locale='fr_FR')

# Quand on arrive sur le site
@app.route('/')
def hello_world():
 return "<p>Hello, World!</p>"

# Quand on veut tester l'affichage de JSON
@app.route('/data')
def data():
 return jsonify({'name': 'Pikachu', 'power': 20, 'life': 50})

# Test d'ajout d'un lien en HTML
@app.route('/funky')
def funky():
 return "<a href='https://www.youtube.com/watch?v=NqFO9J3Sv1U&list=PLchGsFtT6nrSwPAve39lPdeKr1OWWAk5j&index=30'>Let's get funky</a>"

# Test d'adaptation de l'exercice précédent au format JSON
@app.route('/faked')
def faked():
 # Déclaration d'un tableau vide
 fakedPeople = []

 # Déclaration d'une boucle qui génère 3 paires de clés : nom, mail, ville et l'insère dans le tableau
 for i in range(10):
  fakedPeople.append({'name': fake.name(), 'email': fake.email(), 'city': fake.city()})

 # Retourne le tableau Jsonifié
 return jsonify(fakedPeople)