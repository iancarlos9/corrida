from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

inscricoes = []  # Lista para armazenar as inscrições


@app.route('/', methods=['GET', 'POST'])
def inscricao():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        idade = request.form['idade']
        distancia = request.form['distancia']

        inscricao = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'idade': idade,
            'distancia': distancia
        }

        inscricoes.append(inscricao)

        return redirect(url_for('lista_inscricoes'))

    return render_template('formulario.html')


@app.route('/lista_inscricoes')
def lista_inscricoes():
    return render_template('lista_inscricoes.html', inscricoes=inscricoes)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


