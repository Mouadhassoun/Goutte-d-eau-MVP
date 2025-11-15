Projet Goutte d’Eau — MVP

Prédiction du risque de pluie en Bretagne via un modèle de Machine Learning exposé avec FastAPI et une interface Streamlit.

1. Structure du projet
```
Goutte-d-eau-MVP/
│
├── data/
│   ├── climat_data.csv
│   └── meteo_beragne.db
├── models/
│   ├── voting_model.pkl
│   └── scaler.pkl
│
├── api/
│   └── api_server.py
│
├── interface/
│   └── streamlit_app.py
│
├── notebooks/
│   └── model_experiments.ipynb
│
├── requirements.txt
└── README.md
```
3. Installation

Assurez-vous d’avoir Python 3.9+.

```
git clone https://github.com/Mouadhassoun/Goutte-d-eau-MVP.git
cd Goutte-d-eau-MVP
python -m venv goutte
goutte\Scripts\activate
pip install -r requirements.txt
```
3. Lancement de l’API FastAPI

Dans le dossier du projet :
```
uvicorn api.api_server:app --reload
```

L’API sera disponible ici : 
```
http://127.0.0.1:8000/ ==> Affiche un message propre
```
Documentation interactive (Swagger UI) :
```
http://127.0.0.1:8000/docs
```
4. Endpoint disponible :
5. 
POST /predict

Entrée JSON :
```
{
  "temperature": 22.4,
  "humidite": 80,
  "pression": 1012,
  "vent": 3.2
}
```
Sortie :
```
{
  "probabilite_pluie": 0.68
}
````
5. Lancement de l’interface Streamlit

Dans un second terminal :
```
streamlit run interface/streamlit_app.py
```

L’interface s’ouvrira dans votre navigateur.

6. Modèle utilisé

Le modèle final est un VotingClassifier combinant :
```
Régression Logistique

Random Forest

Gradient Boosting
```
L’objectif : maximiser le rappel sur la classe pluie, essentiel pour détecter les épisodes pluvieux.

Les fichiers du modèle :
```
models/voting_model.pkl  
models/scaler.pkl  
```
7. Notebook d’expérimentation

Le dossier notebooks/ contient :
```
les tests de plusieurs modèles

l’analyse des scores

la création du modèle final

l’export du modèle en .pkl
```
8. Éco-responsabilité et accessibilité

Dans le cadre du MVP :

l’API et Streamlit fonctionnent en local,

le stockage SQLite est prévu pour une future extension,

le code est léger et optimise les ressources,

l’interface suit des principes d’accessibilité (contrastes, simplicité, lisibilité).

Des recommandations pour le futur :

hébergement sur un VPS alimenté en énergie verte,

mise en cache des prédictions pour réduire les appels au modèle.

9. Licence

Projet académique — usage pédagogique.




