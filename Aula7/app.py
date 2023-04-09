#Objetos da Requisição
#EX: localhost:5000/?nome=Henrique&Idade=25

from flask import Flask,request
from json import dumps

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    dados = dumps(request.args)
    #print(type(dados))
    return dados

if __name__ == '__main__':
    app.run()