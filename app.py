from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        'id': 1,
        'question_text': 'Qual o nome da mãe de Isaque?',
        'options': ['Penina', 'Sara', 'Raquel', 'Hagar'],
        'answer': 'Sara'
    },
    {
        'id': 2,
        'question_text': 'Qual o maior livro da Biblia?',
        'options': ['Gênesis', 'Eclesiastes', 'Salmos', 'Mateus'],
        'answer': 'Salmos'
    },
    {
        'id': 3,
        'question_text': 'Quem reconstruiu os muros de Jerusalém em 52 dias?',
        'options': ['Ester', 'Naamã', 'Elias', 'Neemias'],
        'answer': 'Neemias'
    },
    {
        'id': 4,
        'question_text': 'Qual o maior capitulo da Biblia?',
        'options': ['Salmos 119', 'João 16', 'Mateus 25', 'Neemias 2'],
        'answer': 'Salmo 119'
    },
    {
        'id': 5,
        'question_text': 'Quem dos discipulos era cobrador de impostos?',
        'options': ['Mateus', 'Felipe', 'Pedro', 'João'],
        'answer': 'Mateus'
    },
    {
        'id': 6,
        'question_text': 'Quem são os pais de João Batista?',
        'options': ['Jose e Maria', 'Abraao e Sara', 'Ana e Elcana', 'Isabel e Zacarias'],
        'answer': 'Isabel e Zacarias'
    },
    {
        'id': 7,
        'question_text': 'Qual o nome do Imperador da Babilonia que destruiu Jerusalém?',
        'options': ['Ciro', 'Nabucodonosor', 'Xerxes', 'Darius'],
        'answer': 'Nabucodonosor'
    },
    {
        'id': 8,
        'question_text': 'Quem foi o judeu que recebeu a promessa que não morreria antes de contemplar o Senhor ?',
        'options': ['Mateus', 'Felipe', 'Simeão', 'João'],
        'answer': 'Mateus'
    },
    {
        'id': 9,
        'question_text': 'Quem ficou temporariamente mudo??',
        'options': ['Mateus', 'Zacarias', 'Pedro', 'João'],
        'answer': 'Zacarias'
    },
    {
        'id': 10,
        'question_text': 'Qual profeta era calvo e chegou a ser zombado pela sua aparência?',
        'options': ['Eliseu', 'Jonas', 'Samuel', 'Elias'],
        'answer': 'Eliseu'
    },
]

@app.route('/')
def quiz():
    return render_template('quiz.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    for question in questions:
        if request.form.get(str(question['id'])) == question['answer']:
            score += 1
    return render_template('result.html', score=score, total_questions=len(questions)) 

if __name__ == '__main__':
    app.run(debug=True) 

