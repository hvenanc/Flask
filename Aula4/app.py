#Construção de URL's

from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/admin')
def admin():
    return '<h1>Seja Bem-vindo Administrador</h1>'

@app.route('/acesso/<nome>')
def acesso(nome):
    return f'Seja Bem-Vindo {nome}'

@app.route('/usuario/<nome>')
def usuario(nome):
    if nome == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect('https://github.com/hvenanc') 

if __name__ == '__main__':
    app.run(debug=True)