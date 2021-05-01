import sklearn
import joblib
import pandas as pd

from WF_AUTOML_FonctionsMetier import extraire_la_premiere_lettre

from flask import Flask, request

print ("scikit-learn=="+sklearn.__version__)
print ("joblib=="+joblib.__version__)
print ("pandas=="+pd.__version__)

# Load model
pipeline = joblib.load('final.model')

# Démarrer l'appli Flask
app = Flask('__name__')

# Test de l'API
@app.route('/ping', methods=['GET'])
def ping():
  return ('API en ligne', 200)

# API /Predict
@app.route('/predict', methods=['POST'])
def predict():
  print ("JSON RECU : " + str(request.json))
  #print ("DE TYPE : " + str(type(request.json)))
  
  # si récupération d'une chaine : 
  #df = pd.read_json(request.json, typ='frame', orient='columns')
  # si récupération directement d'un dict (type(request.json) grace à Flask
  df = pd.DataFrame(request.json)
  print("Type du DF récupéré : " + str(type(df)))
  print ("Détail du DF récupéré : ")
  print(df)
  
  result = pipeline.predict(df)[0]
  print (result)

  return (str(result), 201)

# Page d'accueil
@app.route('/')
def index():
  return "<h1> Test API DEEP LEARNING - Prévision de ventes MAGASIN=13800 - SIGMA=030176. Utiliser /predict en POST pour faire une prévision sur ce périmètre</h1>"

if __name__ == "__main__":
 app.run(host='0.0.0.0')    
