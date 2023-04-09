#Criando URL's Dinâmicas

from flask import Flask

app = Flask(__name__)

@app.route('/nome/<nome>')
def saudar(nome):
    return f'Olá {nome}'

@app.route('/id/<int:id>')
def id_pagina(id):
    if id != 0:
        return f'Página de id número {id}'
    else:
        return 'Página Inicial'

if __name__ == '__main__':
    app.run(debug=True,port=3000)