import requests
import os

def download(url,dataset='data_file.csv'):
    response=requests.get(url)
    file_path = os.path.join('data/raw', dataset)
    with open(file_path,'wb') as file:

        file.write(response.content)
     