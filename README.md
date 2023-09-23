# Questions Example
Este repositório contém alguns exemplos de JSON de questões para a API [QuestionsAPI](https://github.com/tuliobaruk/QuestionsAPI).

As questões são estruturadas da seguinte forma:

```json
[
    {
        "question": "What is the primary purpose of Amazon S3 in AWS?",
        "description": null,
        "category": "AWS",
        "difficulty": "Easy",
        "answers": {
            "answer_a": "To launch EC2 instances",
            "answer_b": "To store and retrieve data",
            "answer_c": "To manage virtual networks",
            "answer_d": "To create relational databases",
            "answer_e": null,
            "answer_f": null
        },
        "correct_answer": "answer_b",
        "multiple_correct_answers": "false",
        "correct_answers": {
            "answer_a_correct": "false",
            "answer_b_correct": "true",
            "answer_c_correct": "false",
            "answer_d_correct": "false",
            "answer_e_correct": "false",
            "answer_f_correct": "false"
        },
        "explanation": null,
        "tip": null
    }
]
```

**Descrição dos Campos**:

Os seguintes campos estão disponíveis para cada questão:

- **question**: A pergunta em si.
- **description**: (Opcional) Uma descrição opcional para a pergunta (pode ser nulo).
- **category**: A categoria à qual a pergunta pertence (por exemplo, "AWS").
- **difficulty**: A dificuldade da pergunta (por exemplo, "Easy").
- **answers**: Um conjunto de opções de resposta, representadas como um objeto.
- **correct_answer**: A opção de resposta correta.
- **multiple_correct_answers**: Indica se há várias respostas corretas (true/false).
- **correct_answers**: Um conjunto de respostas corretas, representadas como um objeto.
- **explanation**: (Opcional) Uma explicação sobre a resposta correta (pode ser nulo).
- **tip**: (Opcional) Uma dica opcional relacionada à pergunta (pode ser nulo).

---

# Python script

Este script Python está disponível neste repositório para facilitar a importação de dados em servidores MongoDB. Ele automatiza o processo de importação de arquivos JSON presentes na mesma pasta em que o script está localizado. 

Certifique-se de configurar a conexão com o servidor MongoDB, o banco de dados e a coleção de destino conforme necessário antes de executar o script. Isso pode ser útil para importar dados em lote de arquivos JSON para o MongoDB em seu ambiente de desenvolvimento ou produção.

```python
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
```