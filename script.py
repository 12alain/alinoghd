import os
import requests
import pandas as pd

def download(url, dataset='data_file.csv'):
    # Créez le répertoire 'data/raw' s'il n'existe pas
    os.makedirs('data/raw', exist_ok=True)

    # Téléchargez le fichier depuis l'URL
    response = requests.get(url)
    
    # Déterminez le chemin du fichier
    file_path = os.path.join('data/raw', dataset)
    
    # Écrivez le contenu du fichier dans le chemin spécifié
    with open(file_path, 'wb') as file:
        file.write(response.content)
    
    print(f"Fichier téléchargé et enregistré à : {file_path}")

    # Chargez le fichier CSV dans un DataFrame
    df = pd.read_csv(file_path)
    
    # Retournez le DataFrame
    return df


