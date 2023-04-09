#Arquivos estáticos

from flask import Flask

app = Flask(__name__, static_folder='web')

if __name__ == '__main__':
    app.run(debug=True)