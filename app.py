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

from flask import flask,jsonify, request

app = flask(__name__)

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

