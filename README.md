# Flask ou mon 1er serveur web en Python

## But du projet
Dans le prolongement de l'initiation à Python, l'objectif du projet est de créer un premier serveur web simple en Python en utilisant le framework Flask.

## Utiliser le projet

### Cloner le repo
A l'endroit de votre choix, vous pouvez copier le présent dépôt selon les modalités de votre choix (SSH, HTTPS).

```bash
git clone lien-de-votre-choix-pour-cloner-le-repo
```

### Installer les dépendances
Le projet utilise une dépendance et un framework : Faker et Flask. Pour les installer, ouvrez un Terminal et saisissez la commande suivante : 
```bash
pip install -r requirements.txt
```

### Lancer le projet
Maintenant que vous avez toutes les dépendances d'installées, vous pouvez lancer la commande suivante qui va vous permettre d'accéder au serveur local :
```bash
flask --app script run --port 5050
```

### Tester dans votre navigateur
Vous pouvez désormais ouvrir votre navigateur préféré et vous rendre à l'adresse _http://localhost:5050/_ pour découvrir le projet. Vous avez plusieurs routes à votre disposition : 
- l'adresse de base (ci-dessus) pour un magnifique message d'accueil,
- /data pour un test d'affichage d'un json,
- /funky pour s'ambiancer un petit peu,
- /faked pour découvrir 10 profils générés aléatoirement en json.

-----
-----
## Project purpose
In continuation of Python discovery, the project purpose is to create my first web server in Python using Flask framework.

## How to use

### Clone the repo
On a convenient folder, you can clone the repository following your preferences (SSH, HTTPS).

```bash
git clone the-appropriate-link-you-chose-to-clone-the-repo
```

### Install dependancies
The current projet uses one dependancy and one framework: Faker and Flask. To install them, open a bash window and use the following command: 
```bash
pip install -r requirements.txt
```

### Start the project
Now that you have all the required dependancies, you can start the project using the following command that will allow you to access the local server:
```bash
flask --app script run --port 5050
```

### Test in your browser
You can now open your favorite browser and reach the following URL  _http://localhost:5050/_ to discover the project. You have several routes at your disposal: 
- Base URL (above) to get a beautiful welcome message,
- /data to test de display of data as json,
- /funky to enlight your day a little bit,
- /faked to discover 10 faked profiles randomly generated as json file.