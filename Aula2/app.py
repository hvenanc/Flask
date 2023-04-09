#Aula 2 Criando Rotas

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Pegou na porta nova'

def text():
    return '<h1>Testando o titulo</h1>'

app.add_url_rule('/Teste','Teste',text)

def button():
    return '<button>Apertar</button>'

app.add_url_rule('/botao','botao',button)

if __name__ == '__main__':
    app.run(port=3000)