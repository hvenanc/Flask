#1- Aplicação Mínima

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Rota Index'

if __name__ == '__main__':
    app.run()