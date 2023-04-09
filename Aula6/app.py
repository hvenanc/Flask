#Metódos HTTP

from flask import Flask,request
from json import dumps

app = Flask(__name__, static_folder='web')

@app.route('/app', methods=['POST','GET'])
def submeter():
    if request.method == 'POST':
        return dumps(request.form)
    return 'GET'

if __name__ == '__main__':
    app.run(debug=True,port=5000)