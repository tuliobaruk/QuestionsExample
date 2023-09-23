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