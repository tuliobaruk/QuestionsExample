import os
import json

# a bliblioteca pymongo é essencial para o script funcionar
from pymongo import MongoClient

# Conecte-se ao servidor MongoDB (certifique-se de que o servidor MongoDB esteja em execução)
client = MongoClient('mongodb://localhost:27017/')

# Acesse o banco de dados e a coleção onde você deseja importar os dados
db = client['QuestionsAPI'] # O Nome do Banco de dados que será criado
collection = db['Questions'] # O Nome da Collection que será criada

# Diretório onde os arquivos JSON estão localizados (pasta atual do arquivo .py)
json_directory = os.path.dirname(__file__)

# Criação de uma lista com todos os arquivos .json na pasta
json_files = [f for f in os.listdir(json_directory) if f.endswith('.json')]

# Itera sobre os arquivos .json e insere os dados na coleção
for json_file in json_files:
    with open(os.path.join(json_directory, json_file), 'r') as file:
        data = json.load(file)
        collection.insert_many(data)

# Feche a conexão com o servidor MongoDB
client.close()