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
@app.route('/livros',methods=['GET'])  # Adicionado rota para a consulta do livros, com apenas o GET

def obter_livros():
    return jsonify(livros)             # retorna todos os livros

# Consultar (Id)
@app.route('/livros/<int:id>',methods=['GET']) # Adicionado rota para a consulta do livro pelo ID (tipo INT), com apenas o GET

def obter_livros_id(id):
    for livro in livros:                       # percorre todos os livros
        if livro.get('id') == id:              # verifica se o ID foi encontrado
            return jsonify(livro)
        else:
            return "ID não encontrado"

# Editar
@app.route('/livros/<int:id>',methods=['PUT'])    # Adicionado rota para a editar o livro pelo ID (tipo INT), com apenas o PUT

def editar_livro_id(id):
    livro_alterado = request.get_json()           # faz a requisição do JSON e adiciona na var 'livro alterado'
    for indice,livro in enumerate(livros):        # percorre todos os livros usando o método enumerate() para indicar qual o index atual
        if livro.get('id') == id:
            livros[indice].update(livro_alterado) # atualiza com a nova informação
            return jsonify(livros[indice])

# Criar
@app.route('/livros',methods=['POST']) # Adicionado rota para criar novo livro, com apenas o POST

def incluir_livro():
    novo_livro = request.get_json()    # faz a requisição do JSON e adiciona na var 'novo livro'
    livros.append(novo_livro)          # incluir usando o append()

    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>',methods=['DELETE']) # Adicionado rota para excluir livro, com apenas o DELETE

def excluir_livros(id):
    for indice,livro in enumerate(livros):        # percorre todos os livros usando o método enumerate() para indicar qual o index atual
        if livro.get('id') == id:                 # verifica se o ID foi encontrado
            del livros[indice]                    # delete o id indicado

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True) # URL para as requisições = 'http://localhost:5000/livros'
