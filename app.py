# API Local para disponibilizar recursos 
# e/ou funcionalidades

# 1 - Objetivo - Disponibilizar a consulta, criação, edição e 
               # exclusão de livros.
# 2 - URL base - localhost
# 3 - Endpoints - 
                # - localhost/livros    (GET)
                # - localhost/livros/id (GET)
                # - localhost/livro/id  (PUT)
                # - localhost/livro/id  (DELETE)
# 4 - Quais os recursos - Livros

from flask import Flask,jsonify, request

app = Flask(__name__)

livros = [
            {
                'id':1,
                'titulo':'O senhor dos Anéis - A sociedade do Anel',
                'autor': 'J.R.R Tolkien'
            },
            {
                'id':2,
                'titulo':'Harry Potter e a Pedra Filosofal',
                'autor': 'J.K Howling'
            },
            {
                'id':3,
                'titulo':'Hábitos Atõmicos',
                'autor': 'James Clear'
            },
         ]
# Consultar (Todos)
@app.route('/livros',methods=['GET']) # Adicionado rota para a consulta do livros, com apenas o GET

def obter_livros():
    return jsonify(livros)

# Consultar (Id)
@app.route('/livros/<int:id>',methods=['GET']) # Adicionado rota para a consulta do livro pelo ID (tipo INT), com apenas o GET

def obter_livros_id(id):
    for livro in livros:                       # percorre todos os livros
        if livro.get('id') == id:              # verifica se o ID foi encontrado
            return jsonify(livro)
        else:
            return "ID não encontrado"
    
# Editar
# Excluir

app.run(port=5000,host='localhost',debug=True) # URL para as requisições = 'http://localhost:5000/livros'
